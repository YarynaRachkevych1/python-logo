import pytest

from python_logo import create_app, socketio


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    socketio_client = socketio.test_client(app)
    yield socketio_client
    socketio_client.disconnect()


def test_connect(client):
    client.connect()
    assert client.is_connected() is True


def test_run(client):
    client.emit("run", "fd 100")
    received = client.get_received()
    assert received[0]["name"] == "task"
    assert received[0]["args"][0] == {"status": "running"}
    assert received[1]["name"] == "execute"
    assert received[1]["args"][0] == {"name": "forward", "value": 100}
    assert received[2]["name"] == "task"
    assert received[2]["args"][0] == {"status": "done"}
