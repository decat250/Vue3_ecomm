<template>
  <div class="container">
    <div class="row">
      <div class="col-md-8 col-xl-6">
        <div class="imgwrapper">
          <img
            style="max-width: 280px"
            class="img-responsive d-block mx-auto"
            v-bind:src="product_img"
          />
        </div>

        <div class="container testimonial-group" style="margin-top: 10px">
          <div class="row text-center">
            <div
              class="col-4"
              v-for="item in product_imglist"
              v-bind:key="item.id"
            >
              <img
                v-on:click="clicking($event)"
                ref="referenceMe"
                style="max-width: 100px"
                v-bind:src="item.src"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-4 col-xl-6 vertical-center">
        <n-form ref="formRef" :model="model" :rules="rules">
          <n-card ti v-bind:title="product_name">
            <n-form-item path="selopt" label="規格">
              <n-select
                v-model:value="model.selopt"
                placeholder="規格"
                :options="opt"
                :on-update:value="updateopt"
              />
            </n-form-item>

            <n-form-item path="selnum" label="數量">
              <n-input-number v-model:value="model.selnum" max="50" clearable />
            </n-form-item>

            <span class="align-left" style="color: red; font-size: 30px"
              >NT${{ product_price }}</span
            >
            <template #footer
              ><div class="row">
                <div class="col-6">
                  <n-button
                    type="success"
                    block
                    secondary
                    strong
                    v-on:click="addtocard"
                    >加入購物車
                  </n-button>
                </div>
                <div class="col-6">
                  <n-button type="error" block secondary strong @click="buyitem"
                    >立即購買
                  </n-button>
                </div>
              </div></template
            >
          </n-card>
        </n-form>
      </div>
    </div>
  </div>
  <n-card title="" style="margin-bottom: 16px">
    <n-tabs default-value="oasis" justify-content="space-evenly" type="line">
      <n-tab-pane name="oasis" tab="商品描述">
        <div class="container" id="product_describe">
          <div class="row" v-html="product_describe"></div>
        </div>
      </n-tab-pane>
      <n-tab-pane name="the beatles" tab="配送說明"> Hey Jude </n-tab-pane>
      <n-tab-pane name="the beatles" tab="評價"> </n-tab-pane>
    </n-tabs>
  </n-card>
</template>
<style>
.testimonial-group > .row {
  display: block;
  overflow-x: auto;
  white-space: nowrap;
}
.testimonial-group > .row > .col-4 {
  display: inline-block;
}

.vertical-center {
  min-height: 100%; /* Fallback for browsers do NOT support vh unit */

  display: flex;
  align-items: center;
}
</style>
<script>
//import $ from "jquery";

import { defineComponent, ref } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";
export default defineComponent({
  setup() {
    const formRef = ref(null);
    //const message = useMessage();
    const modelRef = ref({
      selopt: null,
      selnum: null,
    });
    const rules = {
      selopt: [
        {
          required: true,
          trigger: ["input", "blur"],
          message: "這個欄位是必填的",
        },
      ],
      selnum: [
        {
          type: "number",
          required: true,
          trigger: ["input", "blur"],
          message: "這個欄位是必填的",
        },
      ],
    };
    return {
      formRef,
      model: modelRef,
      rules,
    };
  },
  data() {
    return {
      product_imglist: [],
      product_name: "",
      product_price: "",
      product_count: "",
      product_img: "",
      product_describe: "",
      num: [],
      opt: [],
    };
  },
  mounted() {
    const route = useRoute();
    fetch("http://127.0.0.1/api/getproductinfo/" + route.params.id, {
      method: "get",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    })
      .then((data) => {
        return data.json();
      })
      .then((ret) => {
        this.product_id = ret.productdata.product_id;
        this.product_name = ret.productdata.product_name;
        this.product_price = ret.productdata.product_price;
        this.product_img = ret.productdata.product_img[0].src;
        this.product_describe = ret.productdata.product_describe;
        var html = ret.productdata.product_describe.replaceAll(
          "img src",
          "img class='img-fluid' src"
        );
        //console.log($(ret.productdata.product_describe).find("img"))
        console.log(html);
        this.product_describe = html;
        this.opt = ret.productdata.opt;
        this.product_imglist = ret.productdata.product_img;
      });
  },
  methods: {
    updateopt(v) {
      this.model.selopt = v;
      console.log(v);
      axios.get("http://localhost/api/getproductprice/" + v, {}).then((res) => {
        if (res.data.Status == "Success") {
          this.model.selnum = null;
          this.model.num = res.data.productdata.opt;
          this.product_price = res.data.price;
        }
      });
    },
    buyitem() {
      this.formRef.validate((valid) => {
        if (!valid) {
          const isLogin = localStorage.getItem("account");

          if (isLogin == null) {
            window.$message.error("您尚未登入");
            return;
          }
          const formData = new FormData();
          formData.append("product_id", this.product_id);
          formData.append("selopt", this.model.selopt);
          formData.append("product_count", this.model.selnum);
          formData.append("userid", localStorage.getItem("id"));

          axios
            .post("http://localhost/api/addtocart", formData, {})
            .then((res) => {
              if (res.data.Status == "Success") {
                window.$message.success(res.data.Message);
                this.$router.push({ path: "/Shopcart" });
                //$("#example").DataTable().ajax.reload();
              }
            });
        } else {
          return false;
        }
      });
    },
    clicking($event) {
      //商品圖片列表點擊
      this.product_img = $event.currentTarget.src;
    },
    addtocard(e) {
      e.preventDefault();
      this.formRef.validate((valid) => {
        if (!valid) {
          const isLogin = localStorage.getItem("account");
          if (isLogin == null) {
            window.$message.error("您尚未登入");
            return;
          }
          const formData = new FormData();
          formData.append("product_id", this.product_id);
          formData.append("selopt", this.model.selopt);
          formData.append("product_count", this.model.selnum);
          formData.append("userid", localStorage.getItem("id"));

          axios
            .post("http://localhost/api/addtocart", formData, {})
            .then((res) => {
              if (res.data.Status == "Success") {
                window.$message.success(res.data.Message);
                //$("#example").DataTable().ajax.reload();
              }
            });
          window.$message.success("Valid");
        } else {
          return;
        }
      });
    },
  },
});
</script>
