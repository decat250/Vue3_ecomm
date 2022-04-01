<template>
  <div class="container">
    <h3>訂單總金額：${{ count }}</h3>
    <vue-good-table
      :columns="columns"
      :rows="rows"
      :paginate="true"
      :lineNumbers="true"
      :globalSearch="true"
    >
    </vue-good-table>
    <div class="row vertical-center">
      <div class="col-12 col-xl-6" style="margin-top: 20px">
        <n-card title="客戶資料">
          <n-form
            ref="formRef"
            :model="model"
            :rules="rules"
            label-placement="left"
            require-mark-placement="right-hanging"
            :size="size"
            label-width="auto"
          >
            訂單時間：{{ order_time }}
            <hr />
            姓名：{{ user_name }}
            <hr />
            電話：{{ user_phone }}
            <hr />
            備註：{{ order_mark }}
          </n-form>
        </n-card>
      </div>

      <div class="col-12 col-xl-6" style="margin-top: 20px">
        <n-card title="送貨資料">
          送貨方式：{{ order_LogisticsType }}
          <hr />
          地址：{{ order_address }}
        </n-card>
      </div>
      <div class="col-12" style="margin-top: 10px" v-if="paydiv">
        <n-card title="付款資料">
          付款方式：{{ PaymentType }}
          <hr />
          付款時間：{{ PaymentDate }}
        </n-card>
      </div>

      <n-button
        type="primary"
        v-on:click="redirect"
        style="margin-top: 20px; margin-buttom: 30px"
      >
        返回訂單
      </n-button>
    </div>
  </div>
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

.vertical-center {
  min-height: 100%; /* Fallback for browsers do NOT support vh unit */

  display: flex;
  align-items: center;
}
</style>
<script>
import { VueGoodTable } from "vue-good-table-next";
import "vue-good-table-next/dist/vue-good-table-next.css";
import axios from "axios";
import $ from "jquery";
import { defineComponent, ref } from "vue";

import "bootstrap/dist/css/bootstrap.min.css";
import "jquery/dist/jquery.min.js";
export default defineComponent({
  components: {
    VueGoodTable,
  },
  data() {
    return {
      showModal: ref(false),
      columns: [
        {
          label: "商品名稱",
          field: "product_name",
          globalSearchDisabled: true,
        },
        {
          label: "規格",
          field: "product_opt_item",
          tdClass: "text-center",
          globalSearchDisabled: true,
        },
        {
          label: "數量",
          field: "item_count",
          type: "number",
          tdClass: "text-center",
          globalSearchDisabled: true,
        },
        {
          label: "單價",
          field: "item_price",
          type: "number",
          tdClass: "text-center",
          globalSearchDisabled: true,
        },
        {
          label: "小記",
          field: "item_total",
          tdClass: "text-center",
          globalSearchDisabled: true,
        },
        {
          label: "出貨狀態",
          field: "logistics_state",
          tdClass: "text-center",
          globalSearchDisabled: true,
        },
      ],
      rows: [],
      count: 0,
      user_name: "",
      user_phone: "",
      order_mark: "",
      order_time: "",
      order_LogisticsType: "",
      order_address: "",
      PaymentDate: "",
      PaymentType: "",
      paydiv: true,
    };
  },
  setup() {},
  mounted() {
    //this.$route.params.id,
    const formData = new FormData();
    formData.append("order_id", this.$route.params.id);
    axios
      .post("http://localhost/api/getorder_item", formData, {})
      .then((res) => {
        if (res.data.custom.order_status != "已付款") {
          this.paydiv = false;
        }
        console.log(res.data.custom.order_status);
        this.user_name = res.data.custom.user_name;
        this.user_phone = res.data.custom.user_phone;
        this.order_address = res.data.custom.order_address;
        this.order_LogisticsType = res.data.custom.order_LogisticsType;

        this.order_mark = res.data.custom.order_mark;
        this.order_time = res.data.custom.order_time;
        this.PaymentDate = res.data.custom.PaymentDate;
        this.PaymentType = res.data.custom.PaymentType;

        this.rows = res.data.data;
        this.count = res.data.count + "元";
      });
  },
  methods: {
    pay() {
      var id = this.$route.params.id;
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
    redirect() {
      this.$router.push({ path: "/admindex/orderadm" });
    },
  },
});
</script>