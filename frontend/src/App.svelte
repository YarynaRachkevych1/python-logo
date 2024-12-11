<script lang="js">
  import ButtonBar from "./components/ButtonBar.svelte";
  import Header from "./components/Header.svelte";
  import InfoBar from "./components/InfoBar.svelte";
  import ResizableContainer from "./components/ResizableContainer.svelte";
  import Socket from "./components/Socket.svelte";
  import Textarea from "./components/Textarea.svelte";
  import Toast from "./components/Toast.svelte";
  import Turtle from "./components/Turtle.svelte";
</script>

<main>
  <Header />
  <div
    class="container-fluid p-0 overflow-hidden d-flex flex-column"
    style="height: calc(100vh - 80px);"
  >
    <div class="row flex-grow-1">
      <div class="d-flex justify-content-center align-items-streach">
        <ResizableContainer>
          <ButtonBar />
          <Textarea />
        </ResizableContainer>
        <div
          class="right-container w-100 d-flex flex-column align-items-center justify-content-center overflow-hidden"
        >
          <Turtle />
          <InfoBar />
        </div>
      </div>
    </div>
  </div>
  <Toast />
  <Socket />
</main>

<style>
  :global(body) {
    background-color: #0a273b;
  }
  :global(*) {
    font-family: "Ubuntu", sans-serif;
  }
  .right-container {
    min-width: 550px;
    flex: 1;
  }
</style>
