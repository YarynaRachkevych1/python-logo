<script module>
  import { toast } from "@zerodevx/svelte-toast";
  import Icon from "./Icon.svelte";

  export function toastSuccess(message) {
    toast.push({
      component: {
        src: Icon,
        props: { name: "check", style: "color: white", message: message },
      },
      theme: {
        "--toastWidth": "24rem",
        "--toastBackground": "#74e344",
        "--toastColor": "white",
        "--toastBorderRadius": "1rem",
        "--toastBarBackground": "darkGreen",
        "--toastPadding": "0.75rem",
      },
    });
  }

  export function toastError(message) {
    toast.push({
      component: {
        src: Icon,
        props: { name: "alert", style: "color: white", message: message },
      },
      theme: {
        "--toastWidth": "24rem",
        "--toastBackground": "#ff3931",
        "--toastColor": "white",
        "--toastBorderRadius": "1rem",
        "--toastBarBackground": "darkRed",
        "--toastPadding": "0.75rem",
      },
    });
  }
</script>

<script>
  import { SvelteToast } from "@zerodevx/svelte-toast";
</script>

<SvelteToast />
