<template>
  <div class="container">
    <n-card title="付款失敗">
      
      交易失敗，請確認付款資料是否正確 <br /><n-button type="tertiary"><router-link to="/order">返回首頁</router-link>  </n-button>
    </n-card>
  </div>
</template>

<script>
import { defineComponent } from "vue";
export default defineComponent({
  setup() {},
  data() {
    return {};
  },
  mounted() {},
  methods: {},
});
</script>
