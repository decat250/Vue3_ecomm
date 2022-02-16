<template>

  <div class="container">
      購物記錄  
    <n-data-table
      :columns="columns"
      :data="data"
      :pagination="pagination"
      :bordered="false"
    />
  </div>
</template>

<script>
import { h, defineComponent } from "vue";
import { NButton, useMessage } from "naive-ui";

const createColumns = ({ play }) => {
  return [
    {
      title: "編號",
      key: "no",
    },
    {
      title: "商品名稱",
      key: "title",
    },
    {
      title: "狀態",
      key: "length",
    },
    {
      title: "操作",
      key: "actions",
      render(row) {
        return h(
          NButton,
          {
            strong: true,
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

const data = [
  { no: 3, title: "預購】口袋相簿三代Piconizer3 128G 玫瑰金 ★送保護套＆轉接頭", length: "待出貨" },
  { no: 4, title: "Don't Look Back in Anger", length: "待出貨" },
  { no: 12, title: "Champagne Supernova", length: "待出貨" },
];

export default defineComponent({
  setup() {
    const message = useMessage();
    return {
      data,
      columns: createColumns({
        play(row) {
          message.info(`Play ${row.title}`);
        },
      }),
      pagination: false,
    };
  },
});
</script>