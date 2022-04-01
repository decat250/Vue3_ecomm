<template>
  <div class="row">
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
      <template #table-row="props">
        <span v-if="props.column.field == 'order_status'">
          <n-select
            v-model:value="props.row.status"
            :options="status_options"
            @update:value="order_status(props.row.order_id, props.row.status)"
          />
        </span>
        <span v-if="props.column.field == 'logistics'">
          <n-select
            v-model:value="props.row.logistics_state"
            :options="logistics_state_options"
            @update:value="
              logistics_state(props.row.order_id, props.row.logistics_state)
            "
          />
        </span>
        <span v-if="props.column.field == 'edit'">
          <n-button type="primary" @click="redirect(props.row.order_id)">
            訂單資訊
          </n-button>
        </span>

        <span v-else>
          {{ props.formattedRow[props.column.field] }}
        </span>
      </template>
    </vue-good-table>
  </div>
</template>

<script>
import axios from "axios";
import { useMessage } from "naive-ui";

import { defineComponent } from "vue";
import { VueGoodTable } from "vue-good-table-next";
import "vue-good-table-next/dist/vue-good-table-next.css";

export default defineComponent({
  components: { VueGoodTable },

  setup() {
    window.$message = useMessage();
    return {};
  },
  data() {
    return {
      columns: [
        {
          label: "訂單日期",
          field: "order_time",
          dateInputFormat: "yyyy-MM-dd'T'HH:mm:ss.SSSSSSXXX",
          dateOutputFormat: "yyyy",
          globalSearchDisabled: true,
        },
        {
          label: "訂購人姓名",
          field: "user_name",
          tdClass: "text-center",
          globalSearchDisabled: true,
        },
        {
          label: "總金額",
          field: "order_total",
          type: "number",
          tdClass: "text-center",
          globalSearchDisabled: true,
        },
        {
          label: "訂單狀態",
          field: "order_status",
          tdClass: "text-center",
          globalSearchDisabled: true,
        },
        {
          label: "出貨狀態",
          field: "logistics",
          tdClass: "text-center",
          globalSearchDisabled: true,
        },
        {
          label: "詳細資訊",
          field: "edit",
          tdClass: "text-center",
          globalSearchDisabled: true,
        },
      ],
      rows: [],
      status_options: [
        { value: "待付款", label: "待付款" },
        { value: "已付款", label: "已付款" },
      ],
      logistics_state_options: [
        { value: "待出貨", label: "待出貨" },
        { value: "已出貨", label: "已出貨" },
      ],
    };
  },
  mounted() {
    axios.get("http://localhost/api/getorderadm", {}).then((res) => {
      this.rows = res.data.data;
    });
  },
  methods: {
    order_status(id, status) {
      console.log(id);
      console.log(status);
      const formData = new FormData();
      formData.append("order_id", id);
      formData.append("status", status);

      axios
        .post("http://localhost/api/orderstatus_update", formData, {})
        .then((res) => {
          if (res.data.Status == "Success") {
            window.$message.success(res.data.Message);

            this.showDeleteModalRef = false;
          }
        });
    },
    logistics_state(id, status) {
      const formData = new FormData();
      formData.append("order_id", id);
      formData.append("status", status);

      axios
        .post("http://localhost/api/logistics_update", formData, {})
        .then((res) => {
          if (res.data.Status == "Success") {
            window.$message.success(res.data.Message);

            this.showDeleteModalRef = false;
          }
        });
    },
    redirect(id) {
      this.$router.push({ path: "/admindex/order_itemadm/" + id });
    },
  },
});
</script>