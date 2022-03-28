<template>
  <div class="container">
    購物車商品
    <div class="row">
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
            <n-button type="primary" v-on:click="del(props.row.id)">
              刪除
            </n-button>
          </span>
          <span v-if="props.column.field == 'count'">
            <n-input-number
              min="1"
              max="50"
              v-model:max="props.row.maxcount"
              v-model:value="props.row.count"
              @update:value="counthandleChange(props.row.id, props.row.count)"
              
            />
          </span>
          <span v-else>
            {{ props.formattedRow[props.column.field] }}
          </span>
        </template>
      </vue-good-table>
    </div>

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
            <n-form-item label="姓名" path="inputValue">
              <n-input placeholder="請輸入姓名" v-model:value="name" />
            </n-form-item>
            <n-form-item label="電話" path="inputValue">
              <n-input placeholder="請輸入電話號碼" v-model:value="phone" />
            </n-form-item>
          </n-form>
        </n-card>
      </div>

      <div class="col-12 col-xl-6" style="margin-top: 20px">
        <n-card title="送貨資料">
          <n-select
            v-bind:disabled="amount == 0"
            v-model:value="selectcvst"
            :options="options"
          /><br />

          <div v-if="selectcvst == 1">
            <n-button type="primary" v-on:click="selectcvs">
              選擇門市
            </n-button>
            <div id="CVSStoreName">取貨門市：請選擇</div>
            <div id="CVSAddress">取貨地址：請選擇</div>
          </div>

          <div v-if="selectcvst == 2">
            <n-button type="primary" v-on:click="selectcvs">
              選擇門市
            </n-button>
            <div id="CVSStoreName">取貨門市：請選擇</div>
            <div id="CVSAddress">取貨地址：請選擇</div>
          </div>

          <div v-if="selectcvst == 3">
            <n-button type="primary" v-on:click="selectcvs">
              選擇門市
            </n-button>
            <div id="CVSStoreName">取貨門市：請選擇</div>
            <div id="CVSAddress">取貨地址：請選擇</div>
          </div>
          <div v-if="selectcvst == 4">
            <div class="row">
              <div class="col-6">
                <n-select
                  v-model:value="selectcounties"
                  @update:value="test"
                  :options="counties"
                />
              </div>
              <div class="col-6">
                <n-select
                  v-model:value="selectdistricts"
                  :options="districts"
                />
              </div>
            </div>

            <n-input
              style="margin-top: 10px"
              v-model:value="selectaddress"
              type="text"
              placeholder="請輸入完整地址"
            />
          </div>

          <br />
        </n-card>
      </div>
      <div class="col-12" style="margin-top: 10px">
        <n-card title="訂單備註">
          <n-input
            v-model:value="ordermark"
            placeholder=""
            type="textarea"
            :autosize="{
              minRows: 3,
              maxRows: 5,
            }"
          />
        </n-card>
      </div>
      <div class="col-12" style="margin-top: 10px">
        訂單總金額：{{ amount }}
      </div>

      <n-button
        style="margin-top: 20px"
        type="primary"
        v-bind:disabled="amount == 0"
        v-on:click="checkout"
      >
        前往結賬
      </n-button>
    </div>
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
  ></n-button>
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
import $ from "jquery";

import { ref } from "vue";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import "jquery/dist/jquery.min.js";

//import $ from "jquery";
import TwCitySelector from "tw-city-selector";
export default {
  name: "Table",
  components: {
    VueGoodTable,
  },
  setup() {
    return {
      showDeleteModalRef: ref(false),
    };
  },
  data() {
    return {
      islogin: 0,
      amount: 0,
      item: "",
      selectcvst: 0,
      selectcounties: -1,
      selectdistricts: "選擇縣市",
      selectaddress: "",
      name: "",
      phone: "",
      ordermark: "",
      options: [
        {
          label: "請選擇取貨方式",
          value: 0,
        },
        {
          label: "7-11超商取貨",
          value: 1,
        },
        {
          label: "全家超商取貨",
          value: 2,
        },
        {
          label: "萊爾富取貨",
          value: 3,
        },
        {
          label: "宅配",
          value: 4,
        },
      ],
      counties: [
        { label: "選擇縣市", value: -1, disabled: true },
        { label: "台北市", value: 0 },
        { label: "基隆市", value: 1 },
        { label: "新北市", value: 2 },
        { label: "宜蘭縣", value: 3 },
        { label: "桃園市", value: 4 },
        { label: "新竹市", value: 5 },
        { label: "新竹縣", value: 6 },
        { label: "苗栗縣", value: 7 },
        { label: "台中市", value: 8 },
        { label: "彰化縣", value: 9 },
        { label: "南投縣", value: 10 },
        { label: "嘉義市", value: 11 },
        { label: "嘉義縣", value: 12 },
        { label: "雲林縣", value: 13 },
        { label: "台南市", value: 14 },
        { label: "高雄市", value: 15 },
        { label: "澎湖縣", value: 16 },
        { label: "金門縣", value: 17 },
        { label: "屏東縣", value: 18 },
        { label: "台東縣", value: 19 },
        { label: "花蓮縣", value: 20 },
        { label: "連江縣", value: 21 },
      ],
      districts: [],
      columns: [
        {
          label: "商品名稱",
          field: "name",
          tdClass: "text-center",
        },
        {
          label: "價格",
          field: "price",
          type: "number",
          tdClass: "text-center",
          globalSearchDisabled: true,
        },
        {
          label: "規格",
          field: "option",
          tdClass: "text-center",
          globalSearchDisabled: true,
        },
        {
          label: "購買數量",
          field: "count",
          type: "number",
          tdClass: "text-center",
          globalSearchDisabled: true,
        },
        {
          label: "小計",
          field: "tot",
          type: "number",
          tdClass: "text-center",
          globalSearchDisabled: true,
        },

        {
          label: "移除商品",
          field: "edit",
          tdClass: "text-center",
          globalSearchDisabled: true,
        },
      ],
      rows: [],
    };
  },
  mounted() {
    const isLogin = localStorage.getItem("account");

    if (isLogin != null) {
      this.islogin = true;
    } else {
      this.islogin = false;
      window.$message.success("您尚未登入");
      this.$router.push({ path: "/" });
    }

    new TwCitySelector();

    //let proxy = this;
    this.load();
  },
  methods: {
    counthandleChange(id, count) {
      const formData = new FormData();
      formData.append("id", id);
      formData.append("count", count);
      axios
        .post("http://localhost/api/changeshopcartcount", formData, {})
        .then((res) => {
          console.log(res)
          if (res.data.Status=="Success")
          {
            this.load()
          }
        });
    },
    load() {
      axios
        .get(
          "http://localhost/api/getshopcart/" + localStorage.getItem("id"),
          {}
        )
        .then((res) => {
          this.rows = res.data.data;
          this.amount = res.data.total
          console.log(res.data.data)
          for (var j=0;j<res.data.data.length;j++)
          {
            console.log(res.data.data[j].name)
            this.item+=res.data.data[j].name+"\n"
          }
          console.log(this.item)
        });
    },
    del(id) {
      document.getElementById("deletebtn").click();
      this.editid = id;
    },
    test() {
      var data = [
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "中正區", value: "中正區" },
          { label: "大同區", value: "大同區" },
          { label: "中山區", value: "中山區" },
          { label: "松山區", value: "松山區" },
          { label: "大安區", value: "大安區" },
          { label: "萬華區", value: "萬華區" },
          { label: "信義區", value: "信義區" },
          { label: "士林區", value: "士林區" },
          { label: "北投區", value: "北投區" },
          { label: "內湖區", value: "內湖區" },
          { label: "南港區", value: "南港區" },
          { label: "文山區", value: "文山區" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "仁愛區", value: "仁愛區" },
          { label: "信義區", value: "信義區" },
          { label: "中正區", value: "中正區" },
          { label: "中山區", value: "中山區" },
          { label: "安樂區", value: "安樂區" },
          { label: "暖暖區", value: "暖暖區" },
          { label: "七堵區", value: "七堵區" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "萬里區", value: "萬里區" },
          { label: "金山區", value: "金山區" },
          { label: "板橋區", value: "板橋區" },
          { label: "汐止區", value: "汐止區" },
          { label: "深坑區", value: "深坑區" },
          { label: "石碇區", value: "石碇區" },
          { label: "瑞芳區", value: "瑞芳區" },
          { label: "平溪區", value: "平溪區" },
          { label: "雙溪區", value: "雙溪區" },
          { label: "貢寮區", value: "貢寮區" },
          { label: "新店區", value: "新店區" },
          { label: "坪林區", value: "坪林區" },
          { label: "烏來區", value: "烏來區" },
          { label: "永和區", value: "永和區" },
          { label: "中和區", value: "中和區" },
          { label: "土城區", value: "土城區" },
          { label: "三峽區", value: "三峽區" },
          { label: "樹林區", value: "樹林區" },
          { label: "鶯歌區", value: "鶯歌區" },
          { label: "三重區", value: "三重區" },
          { label: "新莊區", value: "新莊區" },
          { label: "泰山區", value: "泰山區" },
          { label: "林口區", value: "林口區" },
          { label: "蘆洲區", value: "蘆洲區" },
          { label: "五股區", value: "五股區" },
          { label: "八里區", value: "八里區" },
          { label: "淡水區", value: "淡水區" },
          { label: "三芝區", value: "三芝區" },
          { label: "石門區", value: "石門區" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "宜蘭市", value: "宜蘭市" },
          { label: "頭城鎮", value: "頭城鎮" },
          { label: "礁溪鄉", value: "礁溪鄉" },
          { label: "壯圍鄉", value: "壯圍鄉" },
          { label: "員山鄉", value: "員山鄉" },
          { label: "羅東鎮", value: "羅東鎮" },
          { label: "三星鄉", value: "三星鄉" },
          { label: "大同鄉", value: "大同鄉" },
          { label: "五結鄉", value: "五結鄉" },
          { label: "冬山鄉", value: "冬山鄉" },
          { label: "蘇澳鎮", value: "蘇澳鎮" },
          { label: "南澳鄉", value: "南澳鄉" },
          { label: "釣魚台列嶼", value: "釣魚台列嶼" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "中壢區", value: "中壢區" },
          { label: "平鎮區", value: "平鎮區" },
          { label: "龍潭區", value: "龍潭區" },
          { label: "楊梅區", value: "楊梅區" },
          { label: "新屋區", value: "新屋區" },
          { label: "觀音區", value: "觀音區" },
          { label: "桃園區", value: "桃園區" },
          { label: "龜山區", value: "龜山區" },
          { label: "八德區", value: "八德區" },
          { label: "大溪區", value: "大溪區" },
          { label: "復興區", value: "復興區" },
          { label: "大園區", value: "大園區" },
          { label: "蘆竹區", value: "蘆竹區" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "東區", value: "東區" },
          { label: "北區", value: "北區" },
          { label: "香山區", value: "香山區" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "竹北市", value: "竹北市" },
          { label: "湖口鄉", value: "湖口鄉" },
          { label: "新豐鄉", value: "新豐鄉" },
          { label: "新埔鎮", value: "新埔鎮" },
          { label: "關西鎮", value: "關西鎮" },
          { label: "芎林鄉", value: "芎林鄉" },
          { label: "寶山鄉", value: "寶山鄉" },
          { label: "竹東鎮", value: "竹東鎮" },
          { label: "五峰鄉", value: "五峰鄉" },
          { label: "橫山鄉", value: "橫山鄉" },
          { label: "尖石鄉", value: "尖石鄉" },
          { label: "北埔鄉", value: "北埔鄉" },
          { label: "峨眉鄉", value: "峨眉鄉" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "竹南鎮", value: "竹南鎮" },
          { label: "頭份市", value: "頭份市" },
          { label: "三灣鄉", value: "三灣鄉" },
          { label: "南庄鄉", value: "南庄鄉" },
          { label: "獅潭鄉", value: "獅潭鄉" },
          { label: "後龍鎮", value: "後龍鎮" },
          { label: "通霄鎮", value: "通霄鎮" },
          { label: "苑裡鎮", value: "苑裡鎮" },
          { label: "苗栗市", value: "苗栗市" },
          { label: "造橋鄉", value: "造橋鄉" },
          { label: "頭屋鄉", value: "頭屋鄉" },
          { label: "公館鄉", value: "公館鄉" },
          { label: "大湖鄉", value: "大湖鄉" },
          { label: "泰安鄉", value: "泰安鄉" },
          { label: "銅鑼鄉", value: "銅鑼鄉" },
          { label: "三義鄉", value: "三義鄉" },
          { label: "西湖鄉", value: "西湖鄉" },
          { label: "卓蘭鎮", value: "卓蘭鎮" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "中區", value: "中區" },
          { label: "東區", value: "東區" },
          { label: "南區", value: "南區" },
          { label: "西區", value: "西區" },
          { label: "北區", value: "北區" },
          { label: "北屯區", value: "北屯區" },
          { label: "西屯區", value: "西屯區" },
          { label: "南屯區", value: "南屯區" },
          { label: "太平區", value: "太平區" },
          { label: "大里區", value: "大里區" },
          { label: "霧峰區", value: "霧峰區" },
          { label: "烏日區", value: "烏日區" },
          { label: "豐原區", value: "豐原區" },
          { label: "后里區", value: "后里區" },
          { label: "石岡區", value: "石岡區" },
          { label: "東勢區", value: "東勢區" },
          { label: "和平區", value: "和平區" },
          { label: "新社區", value: "新社區" },
          { label: "潭子區", value: "潭子區" },
          { label: "大雅區", value: "大雅區" },
          { label: "神岡區", value: "神岡區" },
          { label: "大肚區", value: "大肚區" },
          { label: "沙鹿區", value: "沙鹿區" },
          { label: "龍井區", value: "龍井區" },
          { label: "梧棲區", value: "梧棲區" },
          { label: "清水區", value: "清水區" },
          { label: "大甲區", value: "大甲區" },
          { label: "外埔區", value: "外埔區" },
          { label: "大安區", value: "大安區" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "彰化市", value: "彰化市" },
          { label: "芬園鄉", value: "芬園鄉" },
          { label: "花壇鄉", value: "花壇鄉" },
          { label: "秀水鄉", value: "秀水鄉" },
          { label: "鹿港鎮", value: "鹿港鎮" },
          { label: "福興鄉", value: "福興鄉" },
          { label: "線西鄉", value: "線西鄉" },
          { label: "和美鎮", value: "和美鎮" },
          { label: "伸港鄉", value: "伸港鄉" },
          { label: "員林市", value: "員林市" },
          { label: "社頭鄉", value: "社頭鄉" },
          { label: "永靖鄉", value: "永靖鄉" },
          { label: "埔心鄉", value: "埔心鄉" },
          { label: "溪湖鎮", value: "溪湖鎮" },
          { label: "大村鄉", value: "大村鄉" },
          { label: "埔鹽鄉", value: "埔鹽鄉" },
          { label: "田中鎮", value: "田中鎮" },
          { label: "北斗鎮", value: "北斗鎮" },
          { label: "田尾鄉", value: "田尾鄉" },
          { label: "埤頭鄉", value: "埤頭鄉" },
          { label: "溪州鄉", value: "溪州鄉" },
          { label: "竹塘鄉", value: "竹塘鄉" },
          { label: "二林鎮", value: "二林鎮" },
          { label: "大城鄉", value: "大城鄉" },
          { label: "芳苑鄉", value: "芳苑鄉" },
          { label: "二水鄉", value: "二水鄉" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "南投市", value: "南投市" },
          { label: "中寮鄉", value: "中寮鄉" },
          { label: "草屯鎮", value: "草屯鎮" },
          { label: "國姓鄉", value: "國姓鄉" },
          { label: "埔里鎮", value: "埔里鎮" },
          { label: "仁愛鄉", value: "仁愛鄉" },
          { label: "名間鄉", value: "名間鄉" },
          { label: "集集鎮", value: "集集鎮" },
          { label: "水里鄉", value: "水里鄉" },
          { label: "魚池鄉", value: "魚池鄉" },
          { label: "信義鄉", value: "信義鄉" },
          { label: "竹山鎮", value: "竹山鎮" },
          { label: "鹿谷鄉", value: "鹿谷鄉" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "東區", value: "東區" },
          { label: "西區", value: "西區" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "番路鄉", value: "番路鄉" },
          { label: "梅山鄉", value: "梅山鄉" },
          { label: "竹崎鄉", value: "竹崎鄉" },
          { label: "阿里山", value: "阿里山" },
          { label: "中埔鄉", value: "中埔鄉" },
          { label: "大埔鄉", value: "大埔鄉" },
          { label: "水上鄉", value: "水上鄉" },
          { label: "鹿草鄉", value: "鹿草鄉" },
          { label: "太保市", value: "太保市" },
          { label: "朴子市", value: "朴子市" },
          { label: "東石鄉", value: "東石鄉" },
          { label: "六腳鄉", value: "六腳鄉" },
          { label: "新港鄉", value: "新港鄉" },
          { label: "民雄鄉", value: "民雄鄉" },
          { label: "大林鎮", value: "大林鎮" },
          { label: "溪口鄉", value: "溪口鄉" },
          { label: "義竹鄉", value: "義竹鄉" },
          { label: "布袋鎮", value: "布袋鎮" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "斗南鎮", value: "斗南鎮" },
          { label: "大埤鄉", value: "大埤鄉" },
          { label: "虎尾鎮", value: "虎尾鎮" },
          { label: "土庫鎮", value: "土庫鎮" },
          { label: "褒忠鄉", value: "褒忠鄉" },
          { label: "東勢鄉", value: "東勢鄉" },
          { label: "台西鄉", value: "台西鄉" },
          { label: "崙背鄉", value: "崙背鄉" },
          { label: "麥寮鄉", value: "麥寮鄉" },
          { label: "斗六市", value: "斗六市" },
          { label: "林內鄉", value: "林內鄉" },
          { label: "古坑鄉", value: "古坑鄉" },
          { label: "莿桐鄉", value: "莿桐鄉" },
          { label: "西螺鎮", value: "西螺鎮" },
          { label: "二崙鄉", value: "二崙鄉" },
          { label: "北港鎮", value: "北港鎮" },
          { label: "水林鄉", value: "水林鄉" },
          { label: "口湖鄉", value: "口湖鄉" },
          { label: "四湖鄉", value: "四湖鄉" },
          { label: "元長鄉", value: "元長鄉" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "中西區", value: "中西區" },
          { label: "東區", value: "東區" },
          { label: "南區", value: "南區" },
          { label: "北區", value: "北區" },
          { label: "安平區", value: "安平區" },
          { label: "安南區", value: "安南區" },
          { label: "永康區", value: "永康區" },
          { label: "歸仁區", value: "歸仁區" },
          { label: "新化區", value: "新化區" },
          { label: "左鎮區", value: "左鎮區" },
          { label: "玉井區", value: "玉井區" },
          { label: "楠西區", value: "楠西區" },
          { label: "南化區", value: "南化區" },
          { label: "仁德區", value: "仁德區" },
          { label: "關廟區", value: "關廟區" },
          { label: "龍崎區", value: "龍崎區" },
          { label: "官田區", value: "官田區" },
          { label: "麻豆區", value: "麻豆區" },
          { label: "佳里區", value: "佳里區" },
          { label: "西港區", value: "西港區" },
          { label: "七股區", value: "七股區" },
          { label: "將軍區", value: "將軍區" },
          { label: "學甲區", value: "學甲區" },
          { label: "北門區", value: "北門區" },
          { label: "新營區", value: "新營區" },
          { label: "後壁區", value: "後壁區" },
          { label: "白河區", value: "白河區" },
          { label: "東山區", value: "東山區" },
          { label: "六甲區", value: "六甲區" },
          { label: "下營區", value: "下營區" },
          { label: "柳營區", value: "柳營區" },
          { label: "鹽水區", value: "鹽水區" },
          { label: "善化區", value: "善化區" },
          { label: "大內區", value: "大內區" },
          { label: "山上區", value: "山上區" },
          { label: "新市區", value: "新市區" },
          { label: "安定區", value: "安定區" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "新興區", value: "新興區" },
          { label: "前金區", value: "前金區" },
          { label: "苓雅區", value: "苓雅區" },
          { label: "鹽埕區", value: "鹽埕區" },
          { label: "鼓山區", value: "鼓山區" },
          { label: "旗津區", value: "旗津區" },
          { label: "前鎮區", value: "前鎮區" },
          { label: "三民區", value: "三民區" },
          { label: "楠梓區", value: "楠梓區" },
          { label: "小港區", value: "小港區" },
          { label: "左營區", value: "左營區" },
          { label: "仁武區", value: "仁武區" },
          { label: "大社區", value: "大社區" },
          { label: "東沙群島", value: "東沙群島" },
          { label: "南沙群島", value: "南沙群島" },
          { label: "岡山區", value: "岡山區" },
          { label: "路竹區", value: "路竹區" },
          { label: "阿蓮區", value: "阿蓮區" },
          { label: "田寮區", value: "田寮區" },
          { label: "燕巢區", value: "燕巢區" },
          { label: "橋頭區", value: "橋頭區" },
          { label: "梓官區", value: "梓官區" },
          { label: "彌陀區", value: "彌陀區" },
          { label: "永安區", value: "永安區" },
          { label: "湖內區", value: "湖內區" },
          { label: "鳳山區", value: "鳳山區" },
          { label: "大寮區", value: "大寮區" },
          { label: "林園區", value: "林園區" },
          { label: "鳥松區", value: "鳥松區" },
          { label: "大樹區", value: "大樹區" },
          { label: "旗山區", value: "旗山區" },
          { label: "美濃區", value: "美濃區" },
          { label: "六龜區", value: "六龜區" },
          { label: "內門區", value: "內門區" },
          { label: "杉林區", value: "杉林區" },
          { label: "甲仙區", value: "甲仙區" },
          { label: "桃源區", value: "桃源區" },
          { label: "那瑪夏區", value: "那瑪夏區" },
          { label: "茂林區", value: "茂林區" },
          { label: "茄萣區", value: "茄萣區" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "馬公市", value: "馬公市" },
          { label: "西嶼鄉", value: "西嶼鄉" },
          { label: "望安鄉", value: "望安鄉" },
          { label: "七美鄉", value: "七美鄉" },
          { label: "白沙鄉", value: "白沙鄉" },
          { label: "湖西鄉", value: "湖西鄉" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "金沙鎮", value: "金沙鎮" },
          { label: "金湖鎮", value: "金湖鎮" },
          { label: "金寧鄉", value: "金寧鄉" },
          { label: "金城鎮", value: "金城鎮" },
          { label: "烈嶼鄉", value: "烈嶼鄉" },
          { label: "烏坵鄉", value: "烏坵鄉" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "屏東市", value: "屏東市" },
          { label: "三地門鄉", value: "三地門鄉" },
          { label: "霧台鄉", value: "霧台鄉" },
          { label: "瑪家鄉", value: "瑪家鄉" },
          { label: "九如鄉", value: "九如鄉" },
          { label: "里港鄉", value: "里港鄉" },
          { label: "高樹鄉", value: "高樹鄉" },
          { label: "鹽埔鄉", value: "鹽埔鄉" },
          { label: "長治鄉", value: "長治鄉" },
          { label: "麟洛鄉", value: "麟洛鄉" },
          { label: "竹田鄉", value: "竹田鄉" },
          { label: "內埔鄉", value: "內埔鄉" },
          { label: "萬丹鄉", value: "萬丹鄉" },
          { label: "潮州鎮", value: "潮州鎮" },
          { label: "泰武鄉", value: "泰武鄉" },
          { label: "來義鄉", value: "來義鄉" },
          { label: "萬巒鄉", value: "萬巒鄉" },
          { label: "崁頂鄉", value: "崁頂鄉" },
          { label: "新埤鄉", value: "新埤鄉" },
          { label: "南州鄉", value: "南州鄉" },
          { label: "林邊鄉", value: "林邊鄉" },
          { label: "東港鎮", value: "東港鎮" },
          { label: "琉球鄉", value: "琉球鄉" },
          { label: "佳冬鄉", value: "佳冬鄉" },
          { label: "新園鄉", value: "新園鄉" },
          { label: "枋寮鄉", value: "枋寮鄉" },
          { label: "枋山鄉", value: "枋山鄉" },
          { label: "春日鄉", value: "春日鄉" },
          { label: "獅子鄉", value: "獅子鄉" },
          { label: "車城鄉", value: "車城鄉" },
          { label: "牡丹鄉", value: "牡丹鄉" },
          { label: "恆春鎮", value: "恆春鎮" },
          { label: "滿州鄉", value: "滿州鄉" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "台東市", value: "台東市" },
          { label: "綠島鄉", value: "綠島鄉" },
          { label: "蘭嶼鄉", value: "蘭嶼鄉" },
          { label: "延平鄉", value: "延平鄉" },
          { label: "卑南鄉", value: "卑南鄉" },
          { label: "鹿野鄉", value: "鹿野鄉" },
          { label: "關山鎮", value: "關山鎮" },
          { label: "海端鄉", value: "海端鄉" },
          { label: "池上鄉", value: "池上鄉" },
          { label: "東河鄉", value: "東河鄉" },
          { label: "成功鎮", value: "成功鎮" },
          { label: "長濱鄉", value: "長濱鄉" },
          { label: "太麻里", value: "太麻里" },
          { label: "金峰鄉", value: "金峰鄉" },
          { label: "大武鄉", value: "大武鄉" },
          { label: "達仁鄉", value: "達仁鄉" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "花蓮市", value: "花蓮市" },
          { label: "新城鄉", value: "新城鄉" },
          { label: "秀林鄉", value: "秀林鄉" },
          { label: "吉安鄉", value: "吉安鄉" },
          { label: "壽豐鄉", value: "壽豐鄉" },
          { label: "鳳林鎮", value: "鳳林鎮" },
          { label: "光復鄉", value: "光復鄉" },
          { label: "豐濱鄉", value: "豐濱鄉" },
          { label: "瑞穗鄉", value: "瑞穗鄉" },
          { label: "萬榮鄉", value: "萬榮鄉" },
          { label: "玉里鎮", value: "玉里鎮" },
          { label: "卓溪鄉", value: "卓溪鄉" },
          { label: "富里鄉", value: "富里鄉" },
        ],
        [
          { label: "請選擇", value: "請選擇", disabled: true },
          { label: "南竿鄉", value: "南竿鄉" },
          { label: "北竿鄉", value: "北竿鄉" },
          { label: "莒光鄉", value: "莒光鄉" },
          { label: "東引鄉", value: "東引鄉" },
        ],
      ];
      this.districts = data[this.selectcounties];
      this.selectdistricts = "請選擇";
    },
    selectcvs() {
      console.log(this);
      if (this.select == 1) {
        window.open(
          "http://localhost/api/cvs/UNIMARTC2C",
          "_blank",
          "width=500,height=500"
        );
      } else if (this.select == 2) {
        window.open(
          "http://localhost/api/cvs/FAMIC2C",
          "_blank",
          "width=500,height=500"
        );
      } else {
        window.open(
          "http://localhost/api/cvs/HILIFEC2C",
          "_blank",
          "width=500,height=500"
        );
      }
    },

    onPositiveClick() {
      const formData = new FormData();
      formData.append("deleteid", this.editid);
      axios.post("http://localhost/api/delcart", formData, {}).then((res) => {
        if (res.data.Status == "Success") {
          window.$message.success(res.data.Message);
          this.showDeleteModalRef = false;
          this.load();
        }
      });
    },
    onNegativeClick() {
      this.showDeleteModalRef = false;
    },
    
    checkout() {
     
      var data = [
        "台北市",
        "基隆市",
        "新北市",
        "宜蘭縣",
        "桃園市",
        "新竹市",
        "新竹縣",
        "苗栗縣",
        "台中市",
        "彰化縣",
        "南投縣",
        "嘉義市",
        "嘉義縣",
        "雲林縣",
        "台南市",
        "高雄市",
        "澎湖縣",
        "金門縣",
        "屏東縣",
        "台東縣",
        "花蓮縣",
        "連江縣",
      ];

      var address = "";
      if (this.selectcvst == 4) {
        address =
          data[this.selectcounties] + this.selectdistricts + this.selectaddress;
      } else {
        address = $($("#CVSAddress")[0]).html().split("：")[1];
      }
      var order_LogisticsType="32";
      if (this.select == 1)
      {
        order_LogisticsType = "7-11超商取貨"
      }
      else if (this.select == 2)
      {
        order_LogisticsType = "全家超商取貨"
      }else if (this.select == 3)
      {
        order_LogisticsType = "萊爾富超商取貨"
      }
      else
      {
        order_LogisticsType = "宅配"
      }
      this.item="test"
      console.log(order_LogisticsType)
      var url = "http://localhost/api/pay";
      var form = $(
        '<form style="display:none" action="' +
          url +
          '" method="post">' +
          '<input type="text" name="TotalAmount" value="' +
          this.amount +
          '" />' +
          '<input type="text" name="ItemName" value="' +
          "test" +
          '" />' +
          '<input type="text" name="userid" value="' +
          localStorage.getItem("id") +
          '" />' +
          '<input type="text" name="name" value="' +
          this.name +
          '" />' +
          '<input type="text" name="phone" value="' +
          this.phone +
          '" />' +
          '<input type="text" name="address" value="' +
          address +
          '" />' +
          '<input type="text" name="ordermark" value="' +
          this.ordermark +
          '" />' +
          '<input type="text" name="Logistics" value="' +
          order_LogisticsType +
          '" />' +
          "</form>"
      );
       
      $("body").append(form);
      form.submit();
    
    },
   
  },
};
</script>
