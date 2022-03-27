<template>
  商品管理
  <n-button
    type="primary"
    @click="
      showModal = true;
      mod: 0;
    "
  >
    新增商品
  </n-button>
  <vue-good-table
    ref="my-table"
    :search-options="{ enabled: true }"
    :columns="columns"
    :rows="rows"
    :paginate="true"
    :lineNumbers="true"
    :globalSearch="true"
    :pagination-options="{
      enabled: true,
      mode: 'records',
      perPage: 20,
      position: 'top',
      perPageDropdown: [5, 10, 20],
      dropdownAllowAll: false,
      setCurrentPage: 2,
      jumpFirstOrLast: true,
      firstLabel: '第一頁',
      lastLabel: '最後一頁',
      nextLabel: '下一頁',
      prevLabel: '上一頁',
      rowsPerPageLabel: '每頁顯示項目',
      ofLabel: 'of',
      pageLabel: 'page',
      allLabel: 'All',
      infoFn: (params) => `目前頁數 ${params.firstRecordOnPage}`,
    }"
    @on-selected-rows-change="selectionChanged"
    :select-options="{
      enabled: true,
    }"
  >
    >
    <template #selected-row-actions>
      <n-button type="primary" style="margin-right: 10px" v-on:click="test">
        刪除所選商品
      </n-button>
    </template>

    <template #table-row="props">
      <span v-if="props.column.field == 'edit'">
        <n-button
          type="primary"
          style="margin-right: 10px"
          v-on:click="edit(props.row.id)"
        >
          編輯商品
        </n-button>
        <n-button type="primary" v-on:click="del(props.row.id)">
          刪除
        </n-button>
      </span>
      <span v-else>
        {{ props.formattedRow[props.column.field] }}
      </span>
    </template>
  </vue-good-table>
  <n-button
    id="deletebtn"
    style="display: None"
    @click="showDeleteModalRef = true"
  ></n-button>
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

        <n-dynamic-input
          v-model:value="opt"
          :on-create="onCreate"
          style="margin-top: 20px"
        >
          <template #create-button-default> Add whatever you want </template>
          <template #default="{ value }">
            <div style="display: flex; align-items: center; width: 100%">
              
              <n-input-number
                placeholder="輸入價格"
                v-model:value="value.price"
                style="margin-right: 12px; width: 180px"
                min=1
              >
                <template #prefix> $ </template>
              </n-input-number>
        
              <n-input
                placeholder="輸入規格"
                v-model:value="value.string"
                type="text"
                style="margin-right: 12px; width: 180px"
                
              />
            </div>
          </template>
        </n-dynamic-input>
        <hr />
        照片上傳<br />
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
              <br />
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
//import $ from "jquery";
import { VueGoodTable } from "vue-good-table-next";
import "vue-good-table-next/dist/vue-good-table-next.css";

export default defineComponent({
  components: { VueEditor, VueGoodTable },

  setup() {
    const formRef = ref(null);
    const rPasswordFormItemRef = ref(null);
    const modelRef = ref({});

    return {
      opt: ref([
        {
          price: "",
          string: "",
        },
      ]),
      onCreate() {
        return {
          price: "",
          string: "",
        };
      },
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
      preview: "",
      image_list: [],
      preview_list: [],
      product_name: "1",
      product_describe: "",
      editid: 0,
      mod: 0, //0 新增 1 修改
      columns: [
        {
          label: "名稱",
          field: "name",
        },
        {
          label: "價格",
          field: "price",
          type: "number",
        },
        {
          label: "編輯商品",
          field: "edit",
        },
      ],
      rows: [],
    };
  },
  mounted() {
    this.load();
  },
  methods: {
    test() {
      console.log(this.$refs["my-table"].selectedRows);
    },
    load() {
      axios.get("http://localhost/api/productadmgetlist", {}).then((res) => {
        this.rows = res.data.data;
      });
    },
    del(id) {
      document.getElementById("deletebtn").click();
      this.editid = id;
    },
    edit(id) {
      this.image_list = [];
      this.preview_list = [];
      this.product_name = "";
      this.product_describe = "";
      this.product_price = 0;
      this.showModal = true;
      this.mod = 1;
      axios.get("http://127.0.0.1/api/getproductinfo/" + id, {}).then((res) => {
        console.log(res.data.productdata.opt)
        this.product_name = res.data.productdata.product_name;
        this.product_describe = res.data.productdata.product_describe;
        this.opt = res.data.productdata.optad;
        this.editid = id;
        for (var i = 0; i < res.data.productdata.product_img.length; i++) {
          this.getfileimg(res.data.productdata.product_img[i].src);
        }
      });
    },

    onPositiveClick() {
      const formData = new FormData();
      formData.append("deleteid", this.editid);
      axios
        .post("http://localhost/api/delproduct", formData, {})
        .then((res) => {
          if (res.data.Status == "Success") {
            window.$message.success(res.data.Message);

            this.showDeleteModalRef = false;
          }
        });
      this.load();
      axios.get("http://localhost/api/productadmgetlist", {}).then((res) => {
        this.rows = res.data.data;
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
    getfileimg(url) {
      //編輯商品仔入相片
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
    newproduct() {
      const formData = new FormData();

      for (var i = 0; i < this.image_list.length; i++) {
        console.log(this.image_list[i]);
        formData.append("file[]", this.image_list[i]);
      }
    
      formData.append("id", this.editid);
      formData.append("opt", JSON.stringify(this.opt));
      formData.append("product_name", this.product_name);
      formData.append("product_describe", this.product_describe);
      if (this.mod == 0) {
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
              this.product_img = [];
              window.$message.success(res.data.Message);
              axios
                .get("http://localhost/api/productadmgetlist", {})
                .then((res) => {
                  this.rows = res.data.data;
                });
            }
          });
      } else {
        axios
          .post("http://localhost/api/editproduct", formData, {})
          .then((res) => {
            if (res.data.Status == "Success") {
              this.showModal = false;
              window.$message.success(res.data.Message);
              axios
                .get("http://localhost/api/productadmgetlist", {})
                .then((res) => {
                  this.rows = res.data.data;
                });
            }
          });
      }
    },
  },
});
</script>