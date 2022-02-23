<template>
  商品管理
  <n-button type="primary" @click="showModal = true"> 新增商品 </n-button>

  <n-data-table
    :columns="columns"
    :data="productlist"
    :pagination="pagination"
    :bordered="false"
  />

  <n-modal v-model:show="showModal">
    <n-card
      style="width: 600px"
      title="Modal"
      :bordered="false"
      size="huge"
      role="dialog"
      aria-modal="true"
    >
      <n-form :model="model" ref="formRef" :rules="rules">
        <n-form-item path="product_name" label="商品名稱">
          <n-input
            placeholder="請輸入商品名稱"
            clearable
            v-model:value="model.password"
            type=""
          />
        </n-form-item>
        {{ fileList }}
        <div class="row">
          <n-form-item class="col-6" path="product_price" label="價格">
            <n-input-number
              v-model:value="model.price"
              placeholder="請輸入商品價格"
              clearable
            />
          </n-form-item>

          <n-form-item class="col-6" path="product_count" label="數量">
            <n-input-number
              placeholder="請輸入商品數量"
              v-model:value="model.count"
              clearable
            />
          </n-form-item>
        </div>
        <hr />

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
        <n-button
          type="primary"
          onclick="document.getElementById('my-file').click();"
          >瀏覽檔案
        </n-button>

        <div class="container testimonial-group" style="margin-top: 10px">
          <div class="row text-center">
            <div
              class="col-4"
              v-for="(item, index) in preview_list"
              :key="index"
            >
              <img
                :src="item"
                class="img-fluid"
                v-on:click="clicking($event)"
                style="max-width: 100px"
              />
              <p class="mb-0">file name: {{ image_list[index].name }}</p>

              <n-button type="error" v-on:click="deleteimg(index)">
                刪除
              </n-button>
            </div>
          </div>
        </div>

        <hr />
        商品描述
        <vue-editor v-model="content" />
        {{ content }}

        <n-button type="primary" @click="newproduct()" block secondary strong
          >新增商品
        </n-button>

        <n-modal
          v-model:show="showpicModal"
          preset="card"
          style="width: 600px"
          title=""
        >
          <img :src="previewImageUrl" style="width: 100%" />
        </n-modal>
      </n-form>
    </n-card>
  </n-modal>
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
import { h, defineComponent, ref } from "vue";
import { NButton, useMessage } from "naive-ui";
import { VueEditor } from "vue3-editor";
import axios from "axios";
const createColumns = ({ play }) => {
  return [
    {
      title: "代號",
      key: "product_id",
    },
    {
      title: "商品名稱",
      key: "product_name",
    },
    {
      title: "數量",
      key: "product_count",
    },
    {
      title: "價格",
      key: "product_price",
    },
    {
      title: "操作",
      key: "actions",
      render(row) {
        return h(
          NButton,
          {
            strong: true,
            type: "primary",
            tertiary: true,
            size: "small",
            onClick: () => play(row),
          },
          { default: () => "Play" }
        );
      },
    },
  ];
};

export default defineComponent({
  components: { VueEditor },

  setup() {
    const message = useMessage();
    const formRef = ref(null);
    const rPasswordFormItemRef = ref(null);
    const modelRef = ref({});

    return {
      showModal: ref(false),
      columns: createColumns({
        play(row) {
          this.showModal = true;
          message.info(`Play ${row.product_id}`);
        },
      }),
      pagination: { pageSize: 10 },
      formRef,
      rPasswordFormItemRef,
      model: modelRef,
      rules: {},
    };
  },
  data() {
    return {
      content: "<h1>Some initial content</h1>",
      productlist: [],
      preview: "",
      image_list: [],
      preview_list: [],
    };
  },
  mounted() {
    fetch("http://127.0.0.1/api/getproductlist", {
      method: "get",
    })
      .then((data) => {
        return data.json();
      })
      .then((ret) => {
        this.productlist = ret.productlist;
      });
  },
  methods: {
    deleteimg(index) {
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
        console.log(this.image_list[i]);
        formData.append("file[]", this.image_list[i]);
      }

      formData.append('file[]', 6);


      console.log(formData);
      axios
        .post("http://localhost/api/upload_file", formData, {})
        .then((res) => {
          console.log(res);
        });
    },
  },
});
</script>