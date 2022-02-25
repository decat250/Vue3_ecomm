<template>
  商品管理
  <n-button type="primary" @click="showModal = true"> 新增商品 </n-button>
  <table class="table table-hover table-bordered" id="example">
    <thead>
      <tr>
        <th>ID</th>
        <th>名稱</th>
        <th>價格</th>
        <th>數量</th>
        <th>操作</th>
      </tr>
    </thead>
    <tbody></tbody>
  </table>
  <n-button
    id="deletebtn"
    style="display: None"
    @click="showDeleteModalRef = true"
    >123</n-button
  >
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
        <n-form-item path="" label="商品名稱">
          <n-input
            placeholder="請輸入商品名稱"
            clearable
            v-model:value="product_name"
            type=""
          />
        </n-form-item>
        {{ fileList }}
        <div class="row">
          <n-form-item class="col-6" path="" label="價格">
            <n-input-number
              v-model:value="product_price"
              placeholder="請輸入商品價格"
              clearable
            />
          </n-form-item>

          <n-form-item class="col-6" path="product_count" label="數量">
            <n-input-number
              placeholder="請輸入商品數量"
              v-model:value="product_count"
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

              <n-button type="error" v-on:click="deleteimg(index)">
                刪除
              </n-button>
            </div>
          </div>
        </div>

        <hr />
        商品描述
        <vue-editor v-model="product_describe" />

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

  <n-modal
    v-model:show="showDeleteModalRef"
    :mask-closable="false"
    preset="dialog"
    title="確認視窗"
    content="您確定要刪除嗎?"
    positive-text="確定刪除"
    negative-text="取消"
    @positive-click="onPositiveClick"
    @negative-click="onNegativeClick"
    transform-origin="center"
  />
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
import { defineComponent, ref } from "vue";
import { VueEditor } from "vue3-editor";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import "jquery/dist/jquery.min.js";
import "datatables.net-dt/js/dataTables.dataTables";
import "datatables.net-dt/css/jquery.dataTables.min.css";
import $ from "jquery";
export default defineComponent({
  components: { VueEditor },

  setup() {
    const formRef = ref(null);
    const rPasswordFormItemRef = ref(null);
    const modelRef = ref({});

    return {
      showModal: ref(false),
      showDeleteModalRef: ref(false),
      pagination: { pageSize: 10 },
      formRef,
      rPasswordFormItemRef,
      model: modelRef,
      rules: {},
    };
  },
  data() {
    return {
      productlist: [],
      preview: "",
      image_list: [],
      preview_list: [],

      product_count: 0,
      product_price: 0,
      product_name: "1",
      product_describe: "<h1>Some initial content</h1>",

      editid: 0,
    };
  },
  mounted() {
    var table = $("#example").DataTable({
      ajax: "http://localhost/api/productadmgetlist",
      columnDefs: [
        {
          targets: [0],
          visible: false,
        },
        {
          targets: [1],
        },
        {
          targets: [2],
        },
        {
          targets: [3],
        },
        {
          targets: [4],
          defaultContent:
            "<button id='edit'>編輯</button><button id='del'>刪除</button>",
        },
      ],
    });
    let proxy = this;
    $("#example tbody").on("click", "button", function () {
      var data = table.row($(this).parents("tr")).data();
      if ($(this).attr("id") == "del") {
        document.getElementById("deletebtn").click();
        proxy.editid = data[0];
      }

      //console.log(data[0] + "'s salary is: " + data[2]);
    });
  },
  methods: {
    onPositiveClick() {
      //window.$message.success("submit");
      //console.log(proxy.editid);
      const formData = new FormData();
      formData.append("deleteid", this.editid);
      axios
        .post("http://localhost/api/delproduct", formData, {})
        .then((res) => {
          if (res.data.Status == "Success") {
            window.$message.success(res.data.Message);
            $("#example").DataTable().ajax.reload();
            this.showDeleteModalRef = false;
          }
        });
    },
    onNegativeClick() {
      this.showDeleteModalRef = false;
    },

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

      formData.append("product_count", this.product_count);
      formData.append("product_name", this.product_name);
      formData.append("product_describe", this.product_describe);
      formData.append("product_price", this.product_price);

      console.log(formData);
      axios
        .post("http://localhost/api/newproduct", formData, {})
        .then((res) => {
          if (res.data.Status == "Success") {
            this.showModal = false;
            this.image_list = [];
            this.preview_list = [];
            this.product_count = 0;
            this.product_name = "";
            this.product_describe = "";
            this.product_price = window.$message.success(res.data.Message);
            $("#example").DataTable().ajax.reload();
          }
        });
    },
  },
});
</script>