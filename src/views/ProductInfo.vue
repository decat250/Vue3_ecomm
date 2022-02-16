<template>
  <div class="container">
    <div class="row">
      <div class="col-6">
        <img
          style="height: 400px; weight: 50px"
          clsss="img-fluid"
          src="https://shoplineimg.com/54a230f9e37ec655ce00000d/6204d657a1efde0a05bacba7/800x.webp?source_format=jpg"
        />
      </div>
      <div class="col-6 align-middle">
        <n-card
          title="【預購】口袋相簿三代Piconizer3 128G 玫瑰金
            ★送保護套＆轉接頭"
        >
          <template #header-extra> </template>
          規格
          <n-select v-model:value="selopt" placeholder="規格" :options="opt" />

          數量
          <n-select
            v-model:value="selnum"
            placeholder="請選擇數量"
            :options="num"
          />
          <span class="align-left" style="color:red;font-size:30px">NT$1,190</span>

        
          <template #footer><div class="row">
              <div class="col-6">
                <n-button
                  type="success"
                  block
                  secondary
                  strong
                  v-on:click="login"
                  >加入購物車
                </n-button>
              </div>
               <div class="col-6">
                <n-button
                  type="error"
                  block
                  secondary
                  strong
                  v-on:click="login"
                  >立即購買
                </n-button>
              </div>
            </div></template>
         
        </n-card>
      </div>
    </div>
  </div>
  <n-card title="" style="margin-bottom: 16px">
    <n-tabs default-value="oasis" justify-content="space-evenly" type="line">
      <n-tab-pane name="oasis" tab="商品描述">
        <div class="container">
          <div class="row">
            <img
              src="https://shoplineimg.com/54a230f9e37ec655ce00000d/external-e75b336de14ef24ce0fbfc76d2693947/original?image_url=https%3A%2F%2Fimg.shoplineapp.com%2Fmedia%2Fimage_clips%2F615bd6595e8d77001a84b4a0%2Foriginal.jpg%3F1633408601"
            />
          </div>
        </div>
      </n-tab-pane>
      <n-tab-pane name="the beatles" tab="配送說明"> Hey Jude </n-tab-pane>
    </n-tabs>
  </n-card>
</template>

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    return {
      value: ref(null),
      num: [
        {
          label: "1",
          value: "1",
        },
        {
          label: "2",
          value: "2",
        },
        {
          label: "3",
          value: "3",
        },
        {
          label: "4",
          value: "4",
        },
        {
          label: "5",
          value: "5",
        },
        {
          label: "6",
          value: "6",
        },
        {
          label: "7",
          value: "7",
        },
        {
          label: "8",
          value: "8",
        },
      ],
      opt: [
        {
          label: "藍色",
          value: "1",
        },
        {
          label: "紅色",
          value: "2",
        },
      ],
    };
  },
  data() {
    return {
      selnum: "",
      selopt: "",
    };
  },
});
</script>
