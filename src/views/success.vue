<template>
  <div class="te">
    <n-card title="付款成功">
      感謝您的付款 <br /><n-button type="tertiary"
        ><router-link to="/order">回訂單查詢</router-link>
      </n-button>
    </n-card>
  </div>
</template>
<style>
.te {
  position: absolute;
  top: 50%;
  left: 50%;
  -moz-transform: translateX(-50%) translateY(-50%);
  -webkit-transform: translateX(-50%) translateY(-50%);
  transform: translateX(-50%) translateY(-100%);
}
</style>
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
