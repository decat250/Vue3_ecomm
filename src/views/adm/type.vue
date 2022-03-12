<template>
  <div class="row">
    <n-select v-model:value="value" :options="options" />

    <n-transfer ref="transfer" v-model:value="value" :options="options" />
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";

function createOptions() {
  return Array.from({ length: 100 }).map((v, i) => ({
    label: "Option " + i,
    value: i,
    disabled: i % 5 === 0,
  }));
}

function createValues() {
  return Array.from({ length: 50 }).map((v, i) => i);
}

export default defineComponent({
  setup() {
    return {
      options: createOptions(),
      value: ref(createValues()),
    };
  },
});
</script>