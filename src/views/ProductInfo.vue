<template>
  <div class="container">
    <div class="row">
      <div class="col-md-8 col-xl-6">
        <div class="imgwrapper">
          <img
            style="max-width: 280px"
            class="img-responsive d-block mx-auto"
            v-bind:src="productdata.product_img"
          />
        </div>

        <div class="container testimonial-group" style="margin-top:10px">
          <div class="row text-center">
            <div class="col-4" v-for="item in product_imglist" v-bind:key="item.id">
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
        <n-card ti v-bind:title="productdata.product_name">
          <template #header-extra> </template>
          規格
          <n-select
            v-model:value="selopt"
            placeholder="規格"
            :options="productdata.opt"
          />

          數量
          <n-select
            v-model:value="selnum"
            placeholder="請選擇數量"
            :options="productdata.num"
          />
          <span class="align-left" style="color: red; font-size: 30px"
            >NT${{ productdata.product_price }}</span
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
                <n-button type="error" block secondary strong v-on:click="login"
                  >立即購買
                </n-button>
              </div>
            </div></template
          >
        </n-card>
      </div>
    </div>
  </div>
  <n-card title="" style="margin-bottom: 16px">
    <n-tabs default-value="oasis" justify-content="space-evenly" type="line">
      <n-tab-pane name="oasis" tab="商品描述">
        <div class="container">
          <div class="row" v-html="productdata.product_describe"></div>
        </div>
      </n-tab-pane>
      <n-tab-pane name="the beatles" tab="配送說明"> Hey Jude </n-tab-pane>
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
  min-height: 100%;  /* Fallback for browsers do NOT support vh unit */

  display: flex;
  align-items: center;
}
</style>
<script>
import { defineComponent, ref } from "vue";
import { useRoute } from "vue-router";
export default defineComponent({
  setup() {
    return {
      value: ref(null),
    };
  },
  data() {
    return {
      productdata: {
        product_imglist:[],
        product_name: "",
        product_price: "30",
        product_count: "",
        product_img:"",
        product_describe: "",
        num: [],
        opt: [],
        selnum: "", //使用者選擇數量
        selopt: "", // 使用者選擇規則
      },
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
        this.productdata.product_name = ret.productdata.product_name;
        this.productdata.product_price = ret.productdata.product_price;
        this.productdata.product_img = ret.productdata.product_img[0].src;
        this.productdata.product_describe = ret.productdata.product_describe;
        this.productdata.opt = ret.productdata.opt;
        this.productdata.num = ret.productdata.num;
        this.product_imglist = ret.productdata.product_img
      });
  },
  methods: {
    clicking($event) { //商品圖片列表點擊
      this.productdata.product_img = $event.currentTarget.src;
    },
    addtocard() {
      console.log(this.selopt);
      console.log(this.selnum);
    },
  },
});
</script>
