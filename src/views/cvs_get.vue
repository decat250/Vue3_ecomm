<template>
  <p>Enter name</p>

  <input type="text" id="CVSAddress" v-bind:value="CVSAddress" />
  <input type="text" id="CVSStoreName" v-bind:value="CVSStoreName" />
  <input type="text" id="CVSTelephone" v-bind:value="CVSTelephone" />

  <br /><br />
</template>
<script>
import { defineComponent } from "vue";
import { useRoute } from "vue-router";

export default defineComponent({
  data() {
    return {
      CVSAddress: "",
      CVSStoreName: "",
      CVSTelephone: "",
    };
  },
  mounted() {
    const route = useRoute();
    this.CVSAddress = route.params.CVSAddress;
    this.CVSStoreName = route.params.CVSStoreName;
    this.CVSTelephone = route.params.CVSTelephone;
    if (window.opener != null && !window.opener.closed) {
      var address = window.opener.document.getElementById("CVSAddress");
      var storename = window.opener.document.getElementById("CVSStoreName");
      storename.innerHTML = "取貨門市：" + this.CVSStoreName;
      address.innerHTML = "取貨地址：" + this.CVSAddress;
    }
    window.close();
  },
  methods: {},
});
</script>
