<script module>
  import ButtonBar from "./ButtonBar.svelte";
  import Textarea from "./Textarea.svelte";
  import Console from "./Console.svelte";
  import Turtle from "./Turtle.svelte";
  import InfoBar from "./InfoBar.svelte";
  import themeColor from "../storeThemes.js";
  import { PaneGroup, Pane, PaneResizer } from "paneforge";
</script>

<div class="container-fluid p-0 m-0">
  <PaneGroup
    direction="horizontal"
    class="w-full"
    style="min-height: calc(100vh - 80px)"
  >
    <Pane defaultSize={50} minSize={35}>
      <ButtonBar />
      <PaneGroup direction="vertical" style="height: calc(100vh - 140px)">
        <Pane defaultSize={60} minSize={30}>
          <Textarea />
        </Pane>
        <PaneResizer class="relative flex" tabindex="-1">
          <div class="resizer-ver {$themeColor}"></div>
        </PaneResizer>
        <Pane defaultSize={35} minSize={30}>
          <Console />
        </Pane>
      </PaneGroup>
    </Pane>
    <PaneResizer class="relative flex" tabindex="-1">
      <div class="resizer-hor {$themeColor}"></div>
    </PaneResizer>
    <Pane defaultSize={50} minSize={35}>
      <Turtle />
      <InfoBar />
    </Pane>
  </PaneGroup>
</div>

<style>
  .container-fluid {
    height: calc(100vh - 80px);
  }

  .resizer-hor {
    width: 10px;
    height: 100%;
    cursor: ew-resize;
    z-index: 10;
    &.light {
      background: var(--ter-pri-light);
    }
    &.dark {
      background: var(--ter-pri-dark);
    }
  }

  .resizer-ver {
    height: 10px;
    cursor: ns-resize;
    &.light {
      background: var(--ter-pri-light);
    }
    &.dark {
      background: var(--ter-pri-dark);
    }
  }
</style>
