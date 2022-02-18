<template>
  商品管理
  <n-button type="primary" @click="showModal = true"> 新增商品 </n-button>
    <vue-editor v-model="content" />

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
      <template #header-extra> Oops! </template>
      Content
      <template #footer> Footer </template>
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
    return {
      showModal: ref(false),
      columns: createColumns({
        play(row) {
          message.info(`Play ${row.product_id}`);
        },
      }),
      pagination: { pageSize: 10 },
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
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    })
      .then((data) => {
        return data.json();
      })
      .then((ret) => {
        this.productlist = ret.productlist;
        console.log(ret.productlist);
      });
  },
});
</script>