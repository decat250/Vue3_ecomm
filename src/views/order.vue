<template>
  <div class="container">
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
          <n-button
            type="primary"
            style="margin-right: 10px"
            v-if="props.row.status == '代付款'"
            v-on:click="pay(props.row.order_id)"
          >
            付款
          </n-button>
          <n-button type="primary" >
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
import { VueGoodTable } from "vue-good-table-next";
import "vue-good-table-next/dist/vue-good-table-next.css";
import axios from "axios";
import $ from "jquery";

import "bootstrap/dist/css/bootstrap.min.css";
import "jquery/dist/jquery.min.js";
export default {
  components: {
    VueGoodTable,
  },
  data() {
    return {
      columns: [
        {
          label: "訂單日期",
          field: "order_time",
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
          field: "status",
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
    };
  },
  setup() {},
  mounted() {
    axios
      .get("http://localhost/api/getorder/" + localStorage.getItem("id"), {})
      .then((res) => {
        this.rows = res.data.data;
      });
  },
  methods: {
    pay(id) {
      var url = "http://localhost/api/reorder";
      var form = $(
        '<form style="display:none" action="' +
          url +
          '" method="post">' +
          '<input type="text" name="order_id" value="' +
          id +
          '" />' +
          "</form>"
      );

      $("body").append(form);
      form.submit();
    },
  },
};
</script>