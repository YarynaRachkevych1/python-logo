import contextlib

import eventlet
from flask import current_app as app
from flask import request
from flask_socketio import SocketIO

from .exceptions import (
    InterpreterInvalidCommandError,
    InterpreterInvalidTreeError,
    InterpreterUnboundVariableError,
    ParserInvalidCommandError,
    ParserUnexpectedTokenError,
)
from .utils import run

workers = {}


class _Worker:
    """Worker class that runs the Logo code in a background thread.

    Args:
        socketio (SocketIO): The socketio object.
        client_id (str): The client's socketio ID.
        code (str): The Logo code to run.
    """

    def __init__(self, socketio: SocketIO, client_id: str, code: str) -> None:
        """Initializes the Worker instance."""
        self.socketio = socketio
        self.client_id = client_id
        self.code = code
        self._switch = True

    def start(self) -> None:
        """Starts the Logo code execution and emits the commands to the client."""
        self.socketio.emit("task", {"status": "running"}, to=self.client_id)
        eventlet.sleep(0.01)
        try:
            logo_runner = run(self.code)
            for command in logo_runner:
                if not self._switch:
                    break
                self.socketio.emit("execute", command, to=self.client_id)
                eventlet.sleep(0.01)
        except (
            InterpreterInvalidCommandError,
            InterpreterInvalidTreeError,
            InterpreterUnboundVariableError,
            ParserInvalidCommandError,
            ParserUnexpectedTokenError,
        ) as err:
            self.socketio.emit(
                "task",
                {"status": "failed", "message": str(err)},
                to=self.client_id,
            )
            eventlet.sleep(0.01)
            return
        except Exception as err:
            self.socketio.emit(
                "task",
                {"status": "failed", "message": str(err)},
                to=self.client_id,
            )
            eventlet.sleep(0.01)
            app.logger.exception()
            return

        self.socketio.emit("task", {"status": "done"}, to=self.client_id)
        eventlet.sleep(0.01)
        self._switch = False

    def is_running(self) -> bool:
        """Returns whether the Logo code execution is running.

        Returns:
            bool: True if the code execution is running, False otherwise.
        """
        return self._switch

    def stop(self) -> None:
        """Stops the Logo code execution."""
        self._switch = False
        self.socketio.emit("task", {"status": "done"}, to=self.client_id)
        eventlet.sleep(0.01)


def register_events(socketio: SocketIO) -> None:
    """Registers the socketio events for the application.

    Args:
        socketio (SocketIO): The socketio object.
    """

    @socketio.on("connect")
    def on_connect() -> None:
        """Event handler for when a client connects."""
        app.logger.info("Client with IP %s has connected.", request.remote_addr)

    @socketio.on("disconnect")
    def on_disconnect() -> None:
        """Event handler for when a client disconnects."""
        with contextlib.suppress(KeyError):
            del workers[request.sid]
        app.logger.info("Client with IP %s has disconnected.", request.remote_addr)

    @socketio.on("run")
    def on_run(code: str) -> None:
        """Event handler for when a client sends a run event.
        Starts the Logo code execution in a background thread.

        Args:
            code (str): The Logo code to run.
        """
        worker = _Worker(socketio, request.sid, code)
        workers[request.sid] = worker

        app.logger.info(
            "Starting Logo task for client with IP %s.", request.remote_addr
        )
        socketio.start_background_task(worker.start)

        while worker.is_running():
            eventlet.sleep(0.1)

        with contextlib.suppress(KeyError):
            del workers[request.sid]
        app.logger.info(
            "Logo task for client with IP %s has finished.", request.remote_addr
        )

    @socketio.on("stop")
    def on_stop() -> None:
        """Event handler for when a client sends a stop event."""
        if request.sid in workers:
            app.logger.info(
                "Stopping Logo task for client with IP %s.", request.remote_addr
            )
            workers[request.sid].stop()
            with contextlib.suppress(KeyError):
                del workers[request.sid]
