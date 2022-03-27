<template>
  <vue-good-table
    :search-options="{ enabled: true }"
    :columns="columns"
    :rows="rows"
    :paginate="true"
    :lineNumbers="true"
    :globalSearch="true"
  >
    <template #table-row="props">
      <span v-if="props.column.field == 'edit'">
        <n-button type="primary" style="margin-right:10px"  v-on:click="getTotals(props.row.id)"> 搜尋 </n-button>
        <n-button type="primary" v-on:click="del(props.row.id)"> 刪除 </n-button>
      </span>
      <span v-else>
        {{ props.formattedRow[props.column.field] }}
      </span>
    </template>
  </vue-good-table>
</template>

<script>
import { VueGoodTable } from "vue-good-table-next";
import "vue-good-table-next/dist/vue-good-table-next.css";

export default {
  name: "HelloWorld",

  components: {
    VueGoodTable,
  },
  data() {
    return {
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
          label: "數量",
          field: "count",
          type: "number",

        },
         {
          label: "編輯商品",
          field: "edit",
        },
      
      ],
      rows: [
      ],
    };
  },

  methods: {
    getTotals(id) {
      console.log(id)
    },
  },
  setup() {},
};
</script>

<style>
button {
  display: inline-block;
  line-height: 1;
  white-space: nowrap;
  cursor: pointer;
  background: #fff;
  border: 1px solid #dcdfe6;
  color: #606266;
  -webkit-appearance: none;
  text-align: center;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  outline: 0;
  margin: 0;
  -webkit-transition: 0.1s;
  transition: 0.1s;
  font-weight: 500;
  padding: 12px 20px;
  font-size: 14px;
  border-radius: 4px;
  margin-right: 1em;
}

button:disabled {
  background: #fff;
  color: #ddd;
  cursor: not-allowed;
}
</style>