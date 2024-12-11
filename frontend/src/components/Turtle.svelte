<script module>
  import { emitRun, emitStop } from "./Socket.svelte";

  let turtle;

  export function runTurtle(code) {
    emitRun(code);
  }

  export function stopTurtle() {
    emitStop();
  }

  export function resetTurtle() {
    turtle.goto(0, 0);
    turtle.setColor("black");
    turtle.setAngle(0);
    turtle.putPenDown();
    turtle.show();
    turtle.clear();
  }

  export function executeTurtleCommand(command) {
    switch (command.name) {
      case "forward":
        turtle.forward(command.value);
        break;
      case "backward":
        turtle.left(180);
        turtle.forward(command.value);
        turtle.left(180);
        break;
      case "left":
        turtle.left(command.value);
        break;
      case "right":
        turtle.right(command.value);
        break;
      case "penup":
        turtle.putPenUp();
        break;
      case "pendown":
        turtle.putPenDown();
        break;
      case "hideturtle":
        turtle.hide();
        break;
      case "showturtle":
        turtle.show();
        break;
    }
  }
</script>

<script>
  import { onMount } from "svelte";
  import { Turtle } from "better-turtle";

  let turtleCanvas;

  let turtleOptions = {
    defaultColor: "black",
  };

  onMount(() => {
    const ctx = turtleCanvas.getContext("2d", { willReadFrequently: true });
    turtle = new Turtle(ctx, turtleOptions);
    turtle.draw();
  });
</script>

<div
  class="right-container d-flex flex-col align-items-center justify-content-center p-5"
>
  <canvas bind:this={turtleCanvas} width="600" height="600"></canvas>
</div>

<style>
  .right-container {
    flex: 1;
    width: 100%;
  }
  canvas {
    width: 100%;
    max-height: calc(90vh - 160px);
    max-width: calc(90vh - 160px);
    background-color: #cae5be;
    border-radius: 10px;
    z-index: 0;
  }
</style>
