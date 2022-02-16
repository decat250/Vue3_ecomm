<template>
  <div class="home">
    <!--<img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <n-carousel autoplay show-dots=false>
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
    <div class="row" style="margin-top:10px">
      <router-link  class="col-3" style="text-decoration: none;" to="/ProductInfo" >
        <n-card
          title=""
          :segmented="{
            content: true,
            footer: 'soft',
          }"
        >
          <template #header-extra> #header-extra </template>
          <img class="img-fluid" src="https://shoplineimg.com/54a230f9e37ec655ce00000d/6204d657a1efde0a05bacba7/600x.webp?source_format=jpg">

          <template #footer> 【預購】口袋相簿三代Piconizer3 128G 玫瑰金 ★送保護套＆轉接頭</template>
          <template #action> <h5  style="color:red"> NT $ 2990 </h5></template>
        </n-card>
      </router-link>
      <div class="col-3">
        <n-card
          title=""
          :segmented="{
            content: true,
            footer: 'soft',
          }"
        >
          <template #header-extra> #header-extra </template>
          <img class="img-fluid" src="https://shoplineimg.com/54a230f9e37ec655ce00000d/6204d657a1efde0a05bacba7/600x.webp?source_format=jpg">

          <template #footer> 【預購】口袋相簿三代Piconizer3 128G 玫瑰金 ★送保護套＆轉接頭</template>
          <template #action> <h5  style="color:red"> NT $ 2990 </h5></template>
        </n-card>
      </div>
      <div class="col-3">
        <n-card
          title=""
          :segmented="{
            content: true,
            footer: 'soft',
          }"
        >
          <template #header-extra> #header-extra </template>
          <img class="img-fluid" src="https://shoplineimg.com/54a230f9e37ec655ce00000d/6204d657a1efde0a05bacba7/600x.webp?source_format=jpg">

          <template #footer> 【預購】口袋相簿三代Piconizer3 128G 玫瑰金 ★送保護套＆轉接頭</template>
          <template #action> <h5  style="color:red"> NT $ 2990 </h5></template>
        </n-card>
      </div>
      <div class="col-3">
        <n-card
          title=""
          :segmented="{
            content: true,
            footer: 'soft',
          }"
        >
          <template #header-extra> #header-extra </template>
          <img class="img-fluid" src="https://shoplineimg.com/54a230f9e37ec655ce00000d/6204d657a1efde0a05bacba7/600x.webp?source_format=jpg">

          <template #footer> 【預購】口袋相簿三代Piconizer3 128G 玫瑰金 ★送保護套＆轉接頭</template>
          <template #action> <h5  style="color:red"> NT $ 2990 </h5></template>
        </n-card>
      </div>
      <div class="col-3">
        <n-card
          title=""
          :segmented="{
            content: true,
            footer: 'soft',
          }"
        >
          <template #header-extra> #header-extra </template>
          <img class="img-fluid" src="https://shoplineimg.com/54a230f9e37ec655ce00000d/6204d657a1efde0a05bacba7/600x.webp?source_format=jpg">

          <template #footer> 【預購】口袋相簿三代Piconizer3 128G 玫瑰金 ★送保護套＆轉接頭</template>
          <template #action> <h5  style="color:red"> NT $ 2990 </h5></template>
        </n-card>
      </div>
      <div class="col-3">
        <n-card
          title=""
          :segmented="{
            content: true,
            footer: 'soft',
          }"
        >
          <template #header-extra> #header-extra </template>
          <img class="img-fluid" src="https://shoplineimg.com/54a230f9e37ec655ce00000d/6204d657a1efde0a05bacba7/600x.webp?source_format=jpg">

          <template #footer> 【預購】口袋相簿三代Piconizer3 128G 玫瑰金 ★送保護套＆轉接頭</template>
          <template #action> <h5  style="color:red"> NT $ 2990 </h5></template>
        </n-card>
      </div>
      <div class="col-3">
        
        <n-card
          title=""
          :segmented="{
            content: true,
            footer: 'soft',
          }"
        >
          <template #header-extra> #header-extra </template>
          <img class="img-fluid" src="https://shoplineimg.com/54a230f9e37ec655ce00000d/6204d657a1efde0a05bacba7/600x.webp?source_format=jpg">

          <template #footer> 【預購】口袋相簿三代Piconizer3 128G 玫瑰金 ★送保護套＆轉接頭</template>
          <template #action> <h5  style="color:red"> NT $ 2990 </h5></template>
        </n-card>
      </div>
      
      
    </div>
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
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: "Home",
  components: {
    //HelloWorld
  },
};
</script>
