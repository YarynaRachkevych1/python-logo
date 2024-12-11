<script>
  import Icon from "./Icon.svelte";
  import Modal from "./Modal.svelte";

  let showLicenseModal = false;
  let showContactModal = false;
</script>

<div
  class="info-bar footer d-flex align-items-center justify-content-end w-100"
>
  <div class="d-flex gap-4 p-0 me-5">
    <button
      class="p-0 m-0 text-nowrap"
      title="License"
      onclick={() => (showLicenseModal = true)}
    >
      <Icon name="license" message="License" />
    </button>
    <button
      class="p-0 m-0 text-nowrap"
      title="Contact"
      onclick={() => (showContactModal = true)}
    >
      <Icon name="contact" message="Contact" />
    </button>
    <a
      href="https://github.com/YarynaRachkevych1/python-logo"
      target="_blank"
      rel="noopener noreferrer"
    >
      <button class="p-0 m-0 text-nowrap" title="Visit our GitHub">
        <Icon name="github" message="Visit our GitHub" />
      </button>
    </a>
  </div>
</div>

{#if showLicenseModal}
  <Modal title="License" closeEvent={() => (showLicenseModal = false)}>
    This software is licensed under the MIT license.
  </Modal>
{/if}

{#if showContactModal}
  <Modal title="Contact us" closeEvent={() => (showContactModal = false)}>
    If you have any questions or suggestions, feel free to contact us:
    <ul>
      <li>Krystian Ćwikliński: krystian.samaa@gmail.com</li>
      <li>Mikołaj Kalitka: mikolaj.kalitka@proton.me</li>
      <li>Yaryna Rachkevych: rarynka28@gmail.com</li>
      <li>Magda Tytoń: magdaeelna@gmail.com</li>
    </ul>
  </Modal>
{/if}

<style>
  .info-bar {
    background-image: url("/src/assets/info-bar.svg");
    height: 60px;
    z-index: 1;
  }
  button {
    user-select: none;
    border: none;
    cursor: pointer;
    background-color: transparent;
    color: #cae5be;
    font-weight: bold;
    transition:
      scale 0.2s,
      color 0.05s;
  }
  button:hover {
    scale: 1.1;
    color: #92da8c;
  }
  button:active {
    scale: 1.05;
    color: #92da8c;
  }
</style>
