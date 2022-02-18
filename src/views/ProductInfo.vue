<template>
  <div class="container">
    <div class="row">
      <div class="col-6">
        <img
          style="height: 400px; weight: 50px"
          clsss="img-fluid"
          v-bind:src="productdata.product_img"
        />
      </div>
      <div class="col-6 align-middle">
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
          <div class="row" v-html="productdata.product_describe">
          </div>
        </div>
      </n-tab-pane>
      <n-tab-pane name="the beatles" tab="配送說明"> Hey Jude </n-tab-pane>
    </n-tabs>
  </n-card>
</template>

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
        product_name: "口袋",
        product_price: "30",
        product_count: "",
        product_img:
          "https://shoplineimg.com/54a230f9e37ec655ce00000d/60f585307a44430011cdb0d1/800x.webp?source_format=jpg",
        product_describe: "",
        num: [],
        opt: [],
        selnum:"", //使用者選擇數量
        selopt:"" // 使用者選擇規則
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
        this.productdata.product_img = ret.productdata.product_img;
        this.productdata.product_describe = ret.productdata.product_describe;
        

        this.productdata.opt = ret.productdata.opt;
        this.productdata.num = ret.productdata.num;
      });
  },
  methods:
  {
    addtocard()
    {
      console.log(this.selopt)
      console.log(this.selnum)
    }
  }
});
</script>
