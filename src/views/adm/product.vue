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
        {{fileList}}
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
        <n-upload
         @finish="handleFinish"
          action="http://localhost/api/upload_file"
          :default-file-list="fileList"
          list-type="image-card"
        >
          Click to Upload
        </n-upload>

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

<script>
import { h, defineComponent, ref } from "vue";
import { NButton, useMessage } from "naive-ui";
import { VueEditor } from "vue3-editor";
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
    const handleFinish = ({  event }) => {
      console.log("123")
      console.log(event.target.response)
      this.fileList=[]
    }
    return {
      showModal: ref(false),
      columns: createColumns({
        play(row) {
          this.showModal = true;
          message.info(`Play ${row.product_id}`);
        },
      }),
      handleFinish,
      pagination: { pageSize: 10 },
      formRef,
      rPasswordFormItemRef,
      model: modelRef,
      rules: {},
      fileList: [    
        {
          id: "c",
          name: "我是自带url的图片.png",
          status: "finished",
          url: "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg",
        },
      ],
    };
  },
  data() {
    return {
      content: "<h1>Some initial content</h1>",
      productlist: [],
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
});
</script>