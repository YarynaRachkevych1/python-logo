<script>
  import logo from "../assets/logo.png";
</script>

<header
  class="header d-flex w-100 justify-content-center align-items-center user-select-none"
>
  <img
    class="m-1 user-select-none"
    alt="Logo"
    src={logo}
    style="width: 60px; height: 60px;"
  />
  <h1 style="font-weight: bold; margin: 5px;">Logo Playground</h1>
</header>

<style>
  .header {
    background: linear-gradient(90deg, #70f1c9 20%, #26b1b7 100%);
    color: white;
    height: 80px;
    z-index: 10;
  }
</style>
