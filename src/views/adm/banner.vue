<template>
  商品頁banner管理

  <input
    type="file"
    accept="image/*"
    multiple
    @change="previewMultiImage"
    class="form-control-file"
    id="my-file"
    ref="fileInput"
    style="display: none"
  />
  <n-button type="primary" onclick="document.getElementById('my-file').click();"
    >瀏覽檔案
  </n-button>

  <div class="container testimonial-group" style="margin-top: 10px">
    <div class="row text-center">
      <div
        class="col-4"
        style="margin-bottom: 30px"
        v-for="(item, index) in preview_list"
        :key="index"
      >
        <img
          :src="item"
          class="img-fluid"
          v-on:click="clicking($event)"
          style="max-width: 100px"
        />
        <br />
        <n-button type="error" v-on:click="deleteimg(index)"> 刪除 </n-button>
      </div>
    </div>
    <n-button type="primary" @click="newproduct()" block secondary strong
      >確認修改
    </n-button>
  </div>
</template>
<style>
.btn-file input[type="file"] {
  position: absolute;
  top: 0;
  right: 0;
  min-width: 100%;
  min-height: 100%;
  font-size: 100px;
  text-align: right;
  filter: alpha(opacity=0);
  opacity: 0;
  outline: none;
  background: white;
  cursor: inherit;
  display: block;
}
</style>
<script>
import { defineComponent } from "vue";
import axios from "axios";
export default defineComponent({
  components: {},

  setup() {
    return {};
  },
  data() {
    return {
      productlist: [],
      preview: "",
      image_list: [],
      preview_list: [],
    };
  },
  mounted() {
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
        for (var i = 0; i < ret.bannerimg.length; i++) {
          this.getfileimg(ret.bannerimg[i].item);
        }
      });
  },
  methods: {
    getfileimg(url) {
      fetch(url, { mode: "cors" })
        .then((res) => res.blob())
        .then((blob) => {
          const file = new File([blob], "url.jpg", { type: "image/png" });
          this.image_list.push(file);

          var fr = new FileReader();
          fr.onload = (e) => {
            this.preview_list.push(e.target.result);
          };
          fr.readAsDataURL(blob);
        });
    },

    deleteimg(index) {
      console.log(index);
      this.preview_list.splice(index, 1);
      this.image_list.splice(index, 1);
    },
    previewMultiImage: function (event) {
      //this.imagesArray = event.target.files;
      var input = event.target;
      var count = input.files.length;
      var index = 0;
      if (input.files) {
        while (count--) {
          var reader = new FileReader();
          reader.onload = (e) => {
            this.preview_list.push(e.target.result);
          };
          this.image_list.push(input.files[index]);
          reader.readAsDataURL(input.files[index]);
          index++;
        }
      }
    },
    newproduct() {

      const formData = new FormData();

      for (var i = 0; i < this.image_list.length; i++) {
        formData.append("file[]", this.image_list[i]);
      }

      axios.post("http://localhost/api/bannering", formData, {}).then((res) => {
        console.log(res.data.Status)
        if (res.data.Status == "Success") {      
          window.$message.success("資料修改完成");
        } else {
          window.$message.error(res.Message);
        }
      });
    },
  },
});
</script>