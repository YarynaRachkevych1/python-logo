<script>
  import Icon from "./Icon.svelte";
  import { getCode, setCode } from "./Textarea.svelte";
  import { runTurtle, resetTurtle } from "./Turtle.svelte";
  import { toastSuccess } from "./Toast.svelte";

  let input;
  let files = $state();

  function handleRun() {
    runTurtle(getCode());
  }

  function handleReset() {
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
      <button class="p-0 m-0" title="Run code" onclick={handleRun}>
        <Icon name="run" />
      </button>
      <button class="p-0 m-0" title="Run command">
        <Icon name="runDebug" />
      </button>
      <button class="p-0 m-0" title="Pause">
        <Icon name="pause" />
      </button>
      <button class="p-0 m-0" title="Reset" onclick={handleReset}>
        <Icon name="reset" />
      </button>
    </div>
    <div class="d-flex p-0 gap-2">
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
      <button
        class="p-0 m-0"
        title="Download code"
        disabled={!getCode().trim()}
        onclick={handleDownload}
      >
        <Icon name="downloadCode" />
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
    transition:
      scale 0.2s,
      filter 0.05s;
    filter: invert(90%) sepia(3%) saturate(1480%) hue-rotate(53deg)
      brightness(113%) contrast(106%);
  }

  button:enabled:hover {
    scale: 1.1;
    filter: invert(90%) sepia(16%) saturate(674%) hue-rotate(62deg)
      brightness(103%) contrast(96%);
  }
  button:enabled:active {
    scale: 1.05;
    filter: invert(90%) sepia(16%) saturate(674%) hue-rotate(62deg)
      brightness(113%) contrast(96%);
  }
  button:disabled {
    filter: invert(90%) sepia(3%) saturate(1480%) hue-rotate(53deg)
      brightness(113%) contrast(106%);
    opacity: 0.5;
  }
</style>
