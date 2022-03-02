<template>
  <div class="container">
    購物車商品
    <div class="row">
      <table class="table table-hover table-bordered" id="example">
        <thead>
          <tr>
            <th>ID</th>
            <th>名稱</th>
            <th>規格</th>
            <th>單價</th>
            <th>數量</th>

            <th>操作</th>
          </tr>
        </thead>
        <tbody></tbody>
      </table>
    </div>
    訂單總金額：{{ amount
    }}<n-card title="">
        <div role="tw-city-selector" data-bootstrap-style></div>

      <n-button type="primary" v-on:click="checkout"> 前往結賬 </n-button>
    </n-card>
  </div>
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
  <n-button
    id="deletebtn"
    style="display: None"
    @click="showDeleteModalRef = true"
    >123</n-button
  >
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
import { defineComponent, ref } from "vue";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import "jquery/dist/jquery.min.js";
import "datatables.net-dt/js/dataTables.dataTables";
import "datatables.net-dt/css/jquery.dataTables.min.css";
import $ from "jquery";
import TwCitySelector from "tw-city-selector"
export default defineComponent({
  setup() {
    return {
      showDeleteModalRef: ref(false),
    };
  },
  data() {
    return {
      amount: 0,
      item: "",
    };
  },
  mounted() {
    new TwCitySelector();

    let proxy = this;
    this.refreshmount();
    var table = $("#example").DataTable({
      ajax: "http://localhost/api/getshopcart/" + localStorage.getItem("id"),
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
          targets: [5],
          defaultContent: "<button id='del'>刪除</button>",
        },
      ],
    });
    $("#example tbody").on("click", "button", function () {
      var data = table.row($(this).parents("tr")).data();
      document.getElementById("deletebtn").click();
      proxy.editid = data[0];
    });
  },
  methods: {
    onPositiveClick() {
      const formData = new FormData();
      formData.append("deleteid", this.editid);
      axios.post("http://localhost/api/delcart", formData, {}).then((res) => {
        if (res.data.Status == "Success") {
          window.$message.success(res.data.Message);
          $("#example").DataTable().ajax.reload();
          this.refreshmount();
          this.showDeleteModalRef = false;
        }
      });
    },
    onNegativeClick() {
      console.log(this.amount);

      this.showDeleteModalRef = false;
    },
    refreshmount() {
      this.amount = 0;
      axios
        .get(
          "http://localhost/api/getshopcart/" + localStorage.getItem("id"),
          {}
        )
        .then((res) => {
          for (var i = 0; i < res.data.data.length; i++) {
            this.amount += res.data.data[i][3] * res.data.data[i][4];
            this.item += res.data.data[i][1] + "x" + res.data.data[i][4] + "#";
          }
        });
    },
    checkout() {
      var url = "http://localhost/api/pay";
      var form = $(
        '<form style="display:none" action="' +
          url +
          '" method="post">' +
          '<input type="text" name="TotalAmount" value="' +
          this.amount +
          '" />' +
          '<input type="text" name="ItemName" value="' +
          this.item +
          '" />' +
          "</form>"
      );

      $("body").append(form);
      form.submit();
    },
  },
});
</script>
