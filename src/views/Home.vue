<template>
  <div class="home">
    <n-carousel autoplay show-dots="false">
      <img
        v-for="item in bannerimg"
        v-bind:key="item.banner_id"
        class="carousel-img"
        v-bind:src="item.item"
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
            @update:value="test"
            :collapsed="collapsed"
            :collapsed-width="64"
            :collapsed-icon-size="22"
            :options="menuOptions"
          />
        </n-layout-sider>
        <n-layout>
          <span>
            <div class="row" style="margin-top: 10px">
              <router-link
                :to="`/ProductInfo/${item.product_id}`"
                v-for="item in productlistshow"
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
                  <img class="img-fluid" v-bind:src="item.product_img" />

                  <template #footer> {{ item.product_name }}</template>
                  <template #action>
                    <h5 style="color: red">
                      NT $ {{ item.product_price }}
                    </h5></template
                  >
                </n-card>
              </router-link>

              <div
                class="col-12"
                style="margin-top: 30px; margin-left: auto; margin-right: auto"
              >
                <n-pagination
                  v-model:page="page"
                  @update:page="showitem"
                  :page-count="totalpage"
                  show-quick-jumper
                />
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
import {  defineComponent } from "vue";


export default defineComponent({
  data() {
    return {
      totalpage: 0,
      page: 1,
      bannerimg: [],
      productlist: [],
      menuOptions: [
        {
          label: "Hear the Wind Sing",
          key: "d",
        },
       
      ],
      productlistshow: [],
      
    };
  },

  setup() {
    
  },
  mounted() {
    fetch("http://127.0.0.1/api/getproductlist/null", {
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
        this.menuOptions = ret.type
        this.bannerimg = ret.bannerimg;
        this.productlist = ret.productlist;
        this.totalpage = ret.page;
        var data = [];
        for (var j = 0; j < ret.productlist.length; j++) {
          data.push(this.productlist[j]);
        }
        console.log(data);
        this.productlistshow = data;
        //this.productlistshow = ret.productlist;
      });
  },
  methods: {
    test(value)
    {
      fetch("http://127.0.0.1/api/getproductlist/"+value, {
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
        this.menuOptions = ret.type
        this.bannerimg = ret.bannerimg;
        this.productlist = ret.productlist;
        this.totalpage = ret.page;
        console.log(ret.productlist.length);
        var data = [];
        for (var j = 0; j < ret.productlist.length; j++) {
          data.push(this.productlist[j]);
        }
        console.log(data);
        this.productlistshow = data;
        //this.productlistshow = ret.productlist;
      });
    },
    showitem() {
      var data = [];

      if (this.page == this.totalpage) {
        for (var i = (this.page - 1) * 10; i < this.productlist.length; i++) {
          data.push(this.productlist[i]);
        }
      } else if (this.page == 1) {
        for (var j = 0; j < this.page * 10; j++) {
          data.push(this.productlist[j]);
        }
      } else {
        for (var z = (this.page - 1) * 10; z < this.page * 10; z++) {
          data.push(this.productlist[z]);
        }
      }

      this.productlistshow = data;
    },
  },
});
</script>