<template>
  <div class="row">
    <div class="col-10">
      <n-input placeholder="請輸入標籤名稱" v-model:value="newitemcont" />
    </div>
    <n-button class="col-2" type="info" v-on:click="newtype">
      新增標籤
    </n-button>

    <hr style="margin-top: 10px" />
    <n-select
      class="col-10"
      v-model:value="selecttypelist"
      :options="type_list"
      @update:value="selecttype"
    />

    <n-button class="col-2" type="error" v-on:click="deltype"
      >刪除目前選擇標籤</n-button
    >
    <div class="col-10" style="margin-top: 10px">
      <n-input
      v-bind:disabled="value==null"
        placeholder="請輸入修改後標籤名稱"
        v-model:value="changeitemcont"
      />
    </div>
    <n-button
      v-bind:disabled="value==null"
      class="col-2"
      style="margin-top: 10px"
      type="primary"
      v-on:click="changetype"
      >修改目前選擇標籤名稱</n-button
    >

    <hr style="margin-top: 10px" />
    <n-transfer
      v-bind:disabled="value==null"
      ref="transfer"
      filterable
      source-title="所有商品"
      target-title="標籤內商品"
      v-model:value="value"
      :options="product_list"
    />

    <n-button class="col-12"  v-bind:disabled="value==null" style="margin-top:20px" v-on:click="debug" type="primary">修改標籤商品</n-button>
  </div>
</template>

<script>
import axios from "axios";
import { useMessage } from "naive-ui";

import { defineComponent } from "vue";


export default defineComponent({
  setup() {
    window.$message = useMessage();
    return {};
  },
  mounted() {
    this.gettype();
  },
  data() {
    return {
      product_list: [],
      type_list: [],
      selecttypelist: null,
      newitemcont: "", //新增類別input
      changeitemcont: "", //修改標籤input
      value: null,
    };
  },
  methods: {
    selecttype()
    {
      const formData = new FormData();
      formData.append("typeid", this.selecttypelist);
      axios.post("http://localhost/api/get_typecont", formData, {}).then((res) => {
        this.value = res.data.data
        console.log(res.data.data);
      });
    },
    debug() {
      if (this.selecttypelist == undefined)
      {
        window.$message.error("請由下拉選單選擇要修改之標籤名稱");
        return
      }
      console.log(this.value)
      const formData = new FormData();
      formData.append("productlist", this.value);
      formData.append("typeid", this.selecttypelist);
      axios.post("http://localhost/api/change_typecont", formData, {}).then((res) => {
        window.$message.success(res.data.Message)
        this.selecttypelist=null;
        this.gettype();
      });
    },
    deltype() {
      if (this.selecttypelist == undefined)
      {
        window.$message.error("請由下拉選單選擇要刪除之標籤名稱");
        return
      }
      const formData = new FormData();
      formData.append("typeid", this.selecttypelist);
      axios.post("http://localhost/api/type_del", formData, {}).then((res) => {
        window.$message.success(res.data.Message);
        this.selecttypelist = null;
        this.gettype();
      });
    },
    newtype() {
      if (this.newitemcont == "")
      {
        window.$message.error("請由輸入新增標籤名稱");
        return
      }
      const formData = new FormData();
      formData.append("type", this.newitemcont);
      axios.post("http://localhost/api/type_new", formData, {}).then((res) => {
        window.$message.success(res.data.Message);
        this.newitemcont = "";
        this.gettype();
      });
    },
    gettype() {
      axios.post("http://localhost/api/type_get", {}).then((res) => {
        this.product_list = res.data.data[1];
        this.type_list = res.data.data[0];
        this.value=null
      });
    },
    changetype() {
      const formData = new FormData();
      console.log(this.selecttypelist)
      if (this.selecttypelist == undefined)
      {
        window.$message.error("請由下拉選單選擇要修改之標籤名稱");
        return
      }
      else if (this.changeitemcont =="")
      {
        window.$message.error("請由要修改之標籤名稱");
        return
      }
      formData.append("typeid", this.selecttypelist);
      formData.append("type", this.changeitemcont);
      axios
        .post("http://localhost/api/type_change", formData, {})
        .then((res) => {
          window.$message.success(res.data.Message);
          
          this.gettype();
          this.changeitemcont = "";
          this.selecttypelist = null;
          
        });
    },
  },
});
</script>