<script module>
  import { io } from "socket.io-client";
  import { toastSuccess, toastError } from "./Toast.svelte";
  import { executeTurtleCommand } from "./Turtle.svelte";
  import { setRunningState } from "./ButtonBar.svelte";

  const socket = io();

  let connected = false;

  export function emitRun(code) {
    socket.emit("run", code);
  }

  export function emitStop() {
    socket.emit("stop");
  }

  socket.on("connect", () => {
    if (!connected) {
      console.log("Connected to the server.");
      connected = true;
    } else {
      console.log("Reconnected to the server.");
      toastSuccess("Reconnected to the server.");
    }
  });

  socket.on("connect_error", () => {
    toastError("Cannot connect to the server.");
  });

  socket.on("disconnect", () => {
    console.error("Server connection closed.");
    toastError("Server connection closed.");
  });

  socket.on("task", (data) => {
    if (data.status === "running") {
      setRunningState(true);
    } else if (data.status === "done") {
      setRunningState(false);
    } else if (data.status === "failed") {
      setRunningState(false);
      toastError(data.message);
      console.log("Error: ", data.message);
    }
  });

  socket.on("execute", (command) => {
    executeTurtleCommand(command);
  });
</script>
