<script module>
  import { emitRun, emitStop } from "./Socket.svelte";
  import { logToConsole } from "./Textarea.svelte";

  let turtle;

  export function runTurtle(code) {
    emitRun(code);
  }

  export function stopTurtle() {
    emitStop();
  }

  export function resetTurtle() {
    turtle.goto(0, 0);
    turtle.setColor("white");
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
      case "setpencolor":
        turtle.setColor(command.color);
        break;
      case "setpensize":
        turtle.setWidth(command.value);
        break;
      case "setpos":
        turtle.goto(command.x, command.y);
        break;
      case "print":
        logToConsole(command.value);
        console.log(command.value);
        break;
    }
  }
</script>

<script>
  import themeColor from "../storeThemes.js";
  import { onMount } from "svelte";
  import { Turtle } from "better-turtle";

  let turtleCanvas;

  const turtleVertices = [
    { x: -5, y: 9 },
    { x: -3, y: 10 },
    { x: -2, y: 13 },
    { x: 0, y: 14 },
    { x: 2, y: 13 },
    { x: 3, y: 10 },
    { x: 5, y: 9 },
    { x: 10, y: 10 },
    { x: 8, y: 3 },
    { x: 9, y: 0 },
    { x: 8, y: -3 },
    { x: 10, y: -9 },
    { x: 5, y: -8 },
    { x: 3, y: -9 },
    { x: -3, y: -9 },
    { x: -5, y: -8 },
    { x: -10, y: -9 },
    { x: -8, y: -3 },
    { x: -9, y: 0 },
    { x: -8, y: 3 },
    { x: -10, y: 10 },
    { x: -5, y: 9 },
  ];

  let turtleOptions = {
    defaultColor: "white",
    shape: turtleVertices,
  };

  onMount(() => {
    const ctx = turtleCanvas.getContext("2d", { willReadFrequently: true });
    turtle = new Turtle(ctx, turtleOptions);
    turtle.draw();
    const turtleCanvasId = document.getElementById("turtle");
    turtleCanvasId.style.border = "none";
    turtleCanvasId.style.outline = "none";
  });
</script>

<div
  class="right-container d-flex flex-col align-items-center justify-content-center p-5"
>
  <canvas class={$themeColor} bind:this={turtleCanvas} width="600" height="600"
  ></canvas>
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
    border-radius: 10px;
    z-index: 0;
    &.light {
      background-color: var(--canvas-light);
    }
    &.dark {
      background-color: var(--canvas-dark);
    }
  }
</style>
