<template>
  <div class="container">
    <div class="row">
      <n-alert style="margin-top: 30px" title="請推薦免費的網路空間" type="default" v-on:click="test">
        <template #icon>
          <n-icon>
            hh
          </n-icon>
        </template>
        decat 
      </n-alert>
      
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
//import { useMessage } from "naive-ui";

export default defineComponent({
  setup() {
    return {};
  },
  methods:
  {
    test()
    {
      console.log("2")
    }
  }
});
</script>