<template>
  <div class="home">
    <n-carousel autoplay show-dots="false">
      <img
        class="carousel-img"
        src="https://naive-ui.oss-cn-beijing.aliyuncs.com/carousel-img/carousel1.jpeg"
      />
      <img
        class="carousel-img"
        src="https://naive-ui.oss-cn-beijing.aliyuncs.com/carousel-img/carousel2.jpeg"
      />
      <img
        class="carousel-img"
        src="https://naive-ui.oss-cn-beijing.aliyuncs.com/carousel-img/carousel3.jpeg"
      />
      <img
        class="carousel-img"
        src="https://naive-ui.oss-cn-beijing.aliyuncs.com/carousel-img/carousel4.jpeg"
      />
    </n-carousel>
    <n-space vertical>
      <n-layout has-sider>
        <n-layout-sider
          bordered
          collapse-mode="width"
          :collapsed-width="64"
          :width="240"
          :collapsed="trigger"
          show-trigger
          @collapse="true"
          @expand="true"
        >
          <n-menu
            :collapsed="collapsed"
            :collapsed-width="64"
            :collapsed-icon-size="22"
            :options="menuOptions"
            :render-label="renderMenuLabel"
            :render-icon="renderMenuIcon"
            :expand-icon="expandIcon"
          />
        </n-layout-sider>
        <n-layout>
          <span>
            <div class="row" style="margin-top: 10px">
              <router-link :to = "`/ProductInfo/${item.product_id}`"
                v-for="item in productlist"
                v-bind:key="item.id"
                
                class="col-4"
                
                style="text-decoration: none"
             
              >
                <n-card
                  title=""
                  :segmented="{
                    content: true,
                    footer: 'soft',
                  }"
                >
                  <template #header-extra> #header-extra </template>
                  <img
                    class="img-fluid"
                    v-bind:src="item.product_img"
                  />
  
                  <template #footer>
                    {{item.product_name}}</template
                  >
                  <template #action>
                    <h5 style="color: red">NT $ {{item.product_price}}</h5></template
                  >
                </n-card>
              </router-link>

              <div
                class="col-12 text-center"
                style="margin-top: 30px; margin-buttom: 100px"
              >
                <n-pagination v-model:page="page" :page-count="100" />
              </div></div
          ></span>
        </n-layout>
      </n-layout>
    </n-space>
  </div>
</template>
<style>
.carousel-img {
  width: 100%;
  height: 300px;

  object-fit: cover;
}
</style>
<script>
import { h, defineComponent } from "vue";

const menuOptions = [
  {
    label: "全部商品",
    key: "a",
  },
  {
    label: "【新品上市】口袋相簿3代",
    key: "b",
  },
  {
    label: "Qubii備份豆腐全系列",
    key: "c",
  },
  {
    label: "Hear the Wind Sing",
    key: "d",
  },
];
export default defineComponent({
  data() {
    return {
      productlist: [
        {
          product_count: "30",
          product_id: "1",
          product_img:
            "https://shoplineimg.com/54a230f9e37ec655ce00000d/6204d657a1efde0a05bacba7/800x.webp?source_format=jpg",
          product_name:
            "\u3010\u9810\u8cfc\u3011\u53e3\u888b\u76f8\u7c3f\u4e09\u4ee3Piconizer3 128G \u73ab\u7470\u91d1 \u2605\u9001\u4fdd\u8b77\u5957\uff06\u8f49\u63a5\u982d",
          product_price: "1000",
        },
        {
          product_count: "30",
          product_id: "1",
          product_img:
            "https://shoplineimg.com/54a230f9e37ec655ce00000d/6204d657a1efde0a05bacba7/800x.webp?source_format=jpg",
          product_name:
            "\u3010\u9810\u8cfc\u3011\u53e3\u888b\u76f8\u7c3f\u4e09\u4ee3Piconizer3 128G \u73ab\u7470\u91d1 \u2605\u9001\u4fdd\u8b77\u5957\uff06\u8f49\u63a5\u982d",
          product_price: "1000",
        },
        
      ],
    };
  },
  setup() {
    
    return {
      menuOptions,
      renderMenuLabel(option) {
        console.log(option);
        if ("href" in option) {
          return h("a", { href: option.href, target: "_blank" }, option.label);
        }
        return option.label;
      },
    };
  },
  mounted()
  {
    fetch("http://127.0.0.1/api/getproductlist", {
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
        console.log(ret.productlist);
        this.productlist = ret.productlist
        
      });
  }
 
});
</script>