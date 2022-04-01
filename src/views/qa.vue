<template>
  <n-alert title="Default Text" type="default">
    <template #icon>
      <n-icon>
        <ios-airplane />
      </n-icon>
    </template>
    Gee it's good to be back home
  </n-alert>
</template>

<script>
import { defineComponent } from "vue";
//import { useMessage } from "naive-ui";

export default defineComponent({
  setup() {
    return {};
  },
});
</script>