<script module>
  let runningState = $state(false);

  export function setRunningState(state) {
    runningState = state;
  }
</script>

<script>
  import Icon from "./Icon.svelte";
  import { getCode, setCode } from "./Textarea.svelte";
  import { runTurtle, stopTurtle, resetTurtle } from "./Turtle.svelte";
  import { toastSuccess } from "./Toast.svelte";

  let input;
  let files = $state();

  function handleRun() {
    runTurtle(getCode());
  }

  function handleStop() {
    stopTurtle();
  }

  function handleReset() {
    stopTurtle();
    resetTurtle();
  }

  // handleUpload
  $effect(() => {
    if (files) {
      const reader = new FileReader();
      reader.onload = (event) => {
        setCode(event.target.result);
        toastSuccess("Code uploaded successfully.");
      };
      reader.readAsText(files[0]);
      input.value = "";
    }
  });

  function handleDownload() {
    const blob = new Blob([getCode().trim()], { type: "text/plain" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "logo_code.txt";
    a.click();
    URL.revokeObjectURL(a.href);
    a.remove();
    toastSuccess("Code downloaded successfully.");
  }
</script>

<div>
  <div class="button-bar d-flex align-items-center justify-content-around">
    <div class="d-flex space-around p-0 gap-2">
      {#if !runningState}
        <button class="p-0 m-0" title="Run" onclick={handleRun}>
          <Icon name="run" />
        </button>
      {:else}
        <button class="p-0 m-0" title="Stop" onclick={handleStop}>
          <Icon name="pause" />
        </button>
      {/if}
      <button class="p-0 m-0" title="Run debug" disabled>
        <Icon name="runDebug" />
      </button>
      <button class="p-0 m-0" title="Stop debug" disabled>
        <Icon name="pause" />
      </button>
      <button class="p-0 m-0" title="Reset" onclick={handleReset}>
        <Icon name="reset" />
      </button>
    </div>
    <div class="d-flex p-0 gap-2">
      <button
        class="p-0 m-0"
        title="Download code"
        disabled={!getCode().trim()}
        onclick={handleDownload}
      >
        <Icon name="downloadCode" />
      </button>
      <button class="p-0 m-0" title="Upload code">
        <input
          id="upload-code-input"
          type="file"
          accept=".txt"
          bind:files
          bind:this={input}
          hidden
        />
        <label for="upload-code-input">
          <Icon name="uploadCode" />
        </label>
      </button>
    </div>
  </div>
</div>

<style>
  .button-bar {
    background-image: url("/src/assets/button-bar.svg");
    height: 60px;
    z-index: 1;
  }
  label {
    cursor: pointer;
  }
  button {
    user-select: none;
    border: none;
    background-color: transparent;
    color: #cae5be;
    transition:
      scale 0.2s,
      color 0.05s;
  }
  button:enabled:hover {
    scale: 1.1;
    color: #92da8c;
  }
  button:enabled:active {
    scale: 1.05;
    color: #92da8c;
  }
  button:disabled {
    opacity: 0.5;
  }
</style>
