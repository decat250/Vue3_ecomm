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
    訂單總金額：{{ amount }}
    <n-card title="">
      <n-select v-model:value="select" :options="options" />

      <div v-if="select == 1">
        <n-button type="primary" v-on:click="selectcvs"> 選擇門市 </n-button>
        <div id="CVSStoreName">取貨門市：請選擇</div>
        <div id="CVSAddress">取貨地址：請選擇</div>
      </div>

      <div v-if="select == 2">
        <n-button type="primary" v-on:click="selectcvs"> 選擇門市 </n-button>
        <div id="CVSStoreName">取貨門市：請選擇</div>
        <div id="CVSAddress">取貨地址：請選擇</div>
      </div>

      <div v-if="select == 3">
        <n-button type="primary" v-on:click="selectcvs"> 選擇門市 </n-button>
        <div id="CVSStoreName">取貨門市：請選擇</div>
        <div id="CVSAddress">取貨地址：請選擇</div>
      </div>
      <div v-if="select == 4">
        <n-select v-model:value="value" on-update:test :options="counties" />
        <n-select v-model:value="value" disabled :options="counties" />
      </div>
      <br />
    </n-card>
    <n-button
      type="primary"
      v-bind:disabled="amount == 0"
      v-on:click="checkout"
    >
      前往結賬
    </n-button>
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
import TwCitySelector from "tw-city-selector";
export default defineComponent({
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
      select: 0,
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
      distinctdata: [
        [
          {
            label: [
              "中正區",
              "大同區",
              "中山區",
              "松山區",
              "大安區",
              "萬華區",
              "信義區",
              "士林區",
              "北投區",
              "內湖區",
              "南港區",
              "文山區",
            ],
            value: [
              "中正區",
              "大同區",
              "中山區",
              "松山區",
              "大安區",
              "萬華區",
              "信義區",
              "士林區",
              "北投區",
              "內湖區",
              "南港區",
              "文山區",
            ],
          },
        ],
        [
          {
            label: [
              "仁愛區",
              "信義區",
              "中正區",
              "中山區",
              "安樂區",
              "暖暖區",
              "七堵區",
            ],
            value: [
              "仁愛區",
              "信義區",
              "中正區",
              "中山區",
              "安樂區",
              "暖暖區",
              "七堵區",
            ],
          },
        ],
        [
          {
            label: [
              "萬里區",
              "金山區",
              "板橋區",
              "汐止區",
              "深坑區",
              "石碇區",
              "瑞芳區",
              "平溪區",
              "雙溪區",
              "貢寮區",
              "新店區",
              "坪林區",
              "烏來區",
              "永和區",
              "中和區",
              "土城區",
              "三峽區",
              "樹林區",
              "鶯歌區",
              "三重區",
              "新莊區",
              "泰山區",
              "林口區",
              "蘆洲區",
              "五股區",
              "八里區",
              "淡水區",
              "三芝區",
              "石門區",
            ],
            value: [
              "萬里區",
              "金山區",
              "板橋區",
              "汐止區",
              "深坑區",
              "石碇區",
              "瑞芳區",
              "平溪區",
              "雙溪區",
              "貢寮區",
              "新店區",
              "坪林區",
              "烏來區",
              "永和區",
              "中和區",
              "土城區",
              "三峽區",
              "樹林區",
              "鶯歌區",
              "三重區",
              "新莊區",
              "泰山區",
              "林口區",
              "蘆洲區",
              "五股區",
              "八里區",
              "淡水區",
              "三芝區",
              "石門區",
            ],
          },
        ],
        [
          {
            label: [
              "宜蘭市",
              "頭城鎮",
              "礁溪鄉",
              "壯圍鄉",
              "員山鄉",
              "羅東鎮",
              "三星鄉",
              "大同鄉",
              "五結鄉",
              "冬山鄉",
              "蘇澳鎮",
              "南澳鄉",
              "釣魚台列嶼",
            ],
            value: [
              "宜蘭市",
              "頭城鎮",
              "礁溪鄉",
              "壯圍鄉",
              "員山鄉",
              "羅東鎮",
              "三星鄉",
              "大同鄉",
              "五結鄉",
              "冬山鄉",
              "蘇澳鎮",
              "南澳鄉",
              "釣魚台列嶼",
            ],
          },
        ],
        [
          {
            label: [
              "中壢區",
              "平鎮區",
              "龍潭區",
              "楊梅區",
              "新屋區",
              "觀音區",
              "桃園區",
              "龜山區",
              "八德區",
              "大溪區",
              "復興區",
              "大園區",
              "蘆竹區",
            ],
            value: [
              "中壢區",
              "平鎮區",
              "龍潭區",
              "楊梅區",
              "新屋區",
              "觀音區",
              "桃園區",
              "龜山區",
              "八德區",
              "大溪區",
              "復興區",
              "大園區",
              "蘆竹區",
            ],
          },
        ],
        [
          {
            label: ["東區", "北區", "香山區"],
            value: ["東區", "北區", "香山區"],
          },
        ],
        [
          {
            label: [
              "竹北市",
              "湖口鄉",
              "新豐鄉",
              "新埔鎮",
              "關西鎮",
              "芎林鄉",
              "寶山鄉",
              "竹東鎮",
              "五峰鄉",
              "橫山鄉",
              "尖石鄉",
              "北埔鄉",
              "峨眉鄉",
            ],
            value: [
              "竹北市",
              "湖口鄉",
              "新豐鄉",
              "新埔鎮",
              "關西鎮",
              "芎林鄉",
              "寶山鄉",
              "竹東鎮",
              "五峰鄉",
              "橫山鄉",
              "尖石鄉",
              "北埔鄉",
              "峨眉鄉",
            ],
          },
          {
            label: [
              "302",
              "303",
              "304",
              "305",
              "306",
              "307",
              "308",
              "310",
              "311",
              "312",
              "313",
              "314",
              "315",
            ],
            value: [
              "302",
              "303",
              "304",
              "305",
              "306",
              "307",
              "308",
              "310",
              "311",
              "312",
              "313",
              "314",
              "315",
            ],
          },
        ],
        [
          {
            label: [
              "竹南鎮",
              "頭份市",
              "三灣鄉",
              "南庄鄉",
              "獅潭鄉",
              "後龍鎮",
              "通霄鎮",
              "苑裡鎮",
              "苗栗市",
              "造橋鄉",
              "頭屋鄉",
              "公館鄉",
              "大湖鄉",
              "泰安鄉",
              "銅鑼鄉",
              "三義鄉",
              "西湖鄉",
              "卓蘭鎮",
            ],
            value: [
              "竹南鎮",
              "頭份市",
              "三灣鄉",
              "南庄鄉",
              "獅潭鄉",
              "後龍鎮",
              "通霄鎮",
              "苑裡鎮",
              "苗栗市",
              "造橋鄉",
              "頭屋鄉",
              "公館鄉",
              "大湖鄉",
              "泰安鄉",
              "銅鑼鄉",
              "三義鄉",
              "西湖鄉",
              "卓蘭鎮",
            ],
          },
          {
            label: [
              "350",
              "351",
              "352",
              "353",
              "354",
              "356",
              "357",
              "358",
              "360",
              "361",
              "362",
              "363",
              "364",
              "365",
              "366",
              "367",
              "368",
              "369",
            ],
            value: [
              "350",
              "351",
              "352",
              "353",
              "354",
              "356",
              "357",
              "358",
              "360",
              "361",
              "362",
              "363",
              "364",
              "365",
              "366",
              "367",
              "368",
              "369",
            ],
          },
        ],
        [
          {
            label: [
              "中區",
              "東區",
              "南區",
              "西區",
              "北區",
              "北屯區",
              "西屯區",
              "南屯區",
              "太平區",
              "大里區",
              "霧峰區",
              "烏日區",
              "豐原區",
              "后里區",
              "石岡區",
              "東勢區",
              "和平區",
              "新社區",
              "潭子區",
              "大雅區",
              "神岡區",
              "大肚區",
              "沙鹿區",
              "龍井區",
              "梧棲區",
              "清水區",
              "大甲區",
              "外埔區",
              "大安區",
            ],
            value: [
              "中區",
              "東區",
              "南區",
              "西區",
              "北區",
              "北屯區",
              "西屯區",
              "南屯區",
              "太平區",
              "大里區",
              "霧峰區",
              "烏日區",
              "豐原區",
              "后里區",
              "石岡區",
              "東勢區",
              "和平區",
              "新社區",
              "潭子區",
              "大雅區",
              "神岡區",
              "大肚區",
              "沙鹿區",
              "龍井區",
              "梧棲區",
              "清水區",
              "大甲區",
              "外埔區",
              "大安區",
            ],
          },
        ],
        [
          {
            label: [
              "彰化市",
              "芬園鄉",
              "花壇鄉",
              "秀水鄉",
              "鹿港鎮",
              "福興鄉",
              "線西鄉",
              "和美鎮",
              "伸港鄉",
              "員林市",
              "社頭鄉",
              "永靖鄉",
              "埔心鄉",
              "溪湖鎮",
              "大村鄉",
              "埔鹽鄉",
              "田中鎮",
              "北斗鎮",
              "田尾鄉",
              "埤頭鄉",
              "溪州鄉",
              "竹塘鄉",
              "二林鎮",
              "大城鄉",
              "芳苑鄉",
              "二水鄉",
            ],
            value: [
              "彰化市",
              "芬園鄉",
              "花壇鄉",
              "秀水鄉",
              "鹿港鎮",
              "福興鄉",
              "線西鄉",
              "和美鎮",
              "伸港鄉",
              "員林市",
              "社頭鄉",
              "永靖鄉",
              "埔心鄉",
              "溪湖鎮",
              "大村鄉",
              "埔鹽鄉",
              "田中鎮",
              "北斗鎮",
              "田尾鄉",
              "埤頭鄉",
              "溪州鄉",
              "竹塘鄉",
              "二林鎮",
              "大城鄉",
              "芳苑鄉",
              "二水鄉",
            ],
          },
        ],
        [
          {
            label: [
              "南投市",
              "中寮鄉",
              "草屯鎮",
              "國姓鄉",
              "埔里鎮",
              "仁愛鄉",
              "名間鄉",
              "集集鎮",
              "水里鄉",
              "魚池鄉",
              "信義鄉",
              "竹山鎮",
              "鹿谷鄉",
            ],
            value: [
              "南投市",
              "中寮鄉",
              "草屯鎮",
              "國姓鄉",
              "埔里鎮",
              "仁愛鄉",
              "名間鄉",
              "集集鎮",
              "水里鄉",
              "魚池鄉",
              "信義鄉",
              "竹山鎮",
              "鹿谷鄉",
            ],
          },
        ],
        [{ label: ["東區", "西區"], value: ["東區", "西區"] }],
        [
          {
            label: [
              "番路鄉",
              "梅山鄉",
              "竹崎鄉",
              "阿里山",
              "中埔鄉",
              "大埔鄉",
              "水上鄉",
              "鹿草鄉",
              "太保市",
              "朴子市",
              "東石鄉",
              "六腳鄉",
              "新港鄉",
              "民雄鄉",
              "大林鎮",
              "溪口鄉",
              "義竹鄉",
              "布袋鎮",
            ],
            value: [
              "番路鄉",
              "梅山鄉",
              "竹崎鄉",
              "阿里山",
              "中埔鄉",
              "大埔鄉",
              "水上鄉",
              "鹿草鄉",
              "太保市",
              "朴子市",
              "東石鄉",
              "六腳鄉",
              "新港鄉",
              "民雄鄉",
              "大林鎮",
              "溪口鄉",
              "義竹鄉",
              "布袋鎮",
            ],
          },
        ],
        [
          {
            label: [
              "斗南鎮",
              "大埤鄉",
              "虎尾鎮",
              "土庫鎮",
              "褒忠鄉",
              "東勢鄉",
              "台西鄉",
              "崙背鄉",
              "麥寮鄉",
              "斗六市",
              "林內鄉",
              "古坑鄉",
              "莿桐鄉",
              "西螺鎮",
              "二崙鄉",
              "北港鎮",
              "水林鄉",
              "口湖鄉",
              "四湖鄉",
              "元長鄉",
            ],
            value: [
              "斗南鎮",
              "大埤鄉",
              "虎尾鎮",
              "土庫鎮",
              "褒忠鄉",
              "東勢鄉",
              "台西鄉",
              "崙背鄉",
              "麥寮鄉",
              "斗六市",
              "林內鄉",
              "古坑鄉",
              "莿桐鄉",
              "西螺鎮",
              "二崙鄉",
              "北港鎮",
              "水林鄉",
              "口湖鄉",
              "四湖鄉",
              "元長鄉",
            ],
          },
        ],
        [
          {
            label: [
              "中西區",
              "東區",
              "南區",
              "北區",
              "安平區",
              "安南區",
              "永康區",
              "歸仁區",
              "新化區",
              "左鎮區",
              "玉井區",
              "楠西區",
              "南化區",
              "仁德區",
              "關廟區",
              "龍崎區",
              "官田區",
              "麻豆區",
              "佳里區",
              "西港區",
              "七股區",
              "將軍區",
              "學甲區",
              "北門區",
              "新營區",
              "後壁區",
              "白河區",
              "東山區",
              "六甲區",
              "下營區",
              "柳營區",
              "鹽水區",
              "善化區",
              "大內區",
              "山上區",
              "新市區",
              "安定區",
            ],
            value: [
              "中西區",
              "東區",
              "南區",
              "北區",
              "安平區",
              "安南區",
              "永康區",
              "歸仁區",
              "新化區",
              "左鎮區",
              "玉井區",
              "楠西區",
              "南化區",
              "仁德區",
              "關廟區",
              "龍崎區",
              "官田區",
              "麻豆區",
              "佳里區",
              "西港區",
              "七股區",
              "將軍區",
              "學甲區",
              "北門區",
              "新營區",
              "後壁區",
              "白河區",
              "東山區",
              "六甲區",
              "下營區",
              "柳營區",
              "鹽水區",
              "善化區",
              "大內區",
              "山上區",
              "新市區",
              "安定區",
            ],
          },
        ],
        [
          {
            label: [
              "新興區",
              "前金區",
              "苓雅區",
              "鹽埕區",
              "鼓山區",
              "旗津區",
              "前鎮區",
              "三民區",
              "楠梓區",
              "小港區",
              "左營區",
              "仁武區",
              "大社區",
              "東沙群島",
              "南沙群島",
              "岡山區",
              "路竹區",
              "阿蓮區",
              "田寮區",
              "燕巢區",
              "橋頭區",
              "梓官區",
              "彌陀區",
              "永安區",
              "湖內區",
              "鳳山區",
              "大寮區",
              "林園區",
              "鳥松區",
              "大樹區",
              "旗山區",
              "美濃區",
              "六龜區",
              "內門區",
              "杉林區",
              "甲仙區",
              "桃源區",
              "那瑪夏區",
              "茂林區",
              "茄萣區",
            ],
            value: [
              "新興區",
              "前金區",
              "苓雅區",
              "鹽埕區",
              "鼓山區",
              "旗津區",
              "前鎮區",
              "三民區",
              "楠梓區",
              "小港區",
              "左營區",
              "仁武區",
              "大社區",
              "東沙群島",
              "南沙群島",
              "岡山區",
              "路竹區",
              "阿蓮區",
              "田寮區",
              "燕巢區",
              "橋頭區",
              "梓官區",
              "彌陀區",
              "永安區",
              "湖內區",
              "鳳山區",
              "大寮區",
              "林園區",
              "鳥松區",
              "大樹區",
              "旗山區",
              "美濃區",
              "六龜區",
              "內門區",
              "杉林區",
              "甲仙區",
              "桃源區",
              "那瑪夏區",
              "茂林區",
              "茄萣區",
            ],
          },
        ],
        [
          {
            label: ["馬公市", "西嶼鄉", "望安鄉", "七美鄉", "白沙鄉", "湖西鄉"],
            value: ["馬公市", "西嶼鄉", "望安鄉", "七美鄉", "白沙鄉", "湖西鄉"],
          },
        ],
        [
          {
            label: ["金沙鎮", "金湖鎮", "金寧鄉", "金城鎮", "烈嶼鄉", "烏坵鄉"],
            value: ["金沙鎮", "金湖鎮", "金寧鄉", "金城鎮", "烈嶼鄉", "烏坵鄉"],
          },
        ],
        [
          {
            label: [
              "屏東市",
              "三地門鄉",
              "霧台鄉",
              "瑪家鄉",
              "九如鄉",
              "里港鄉",
              "高樹鄉",
              "鹽埔鄉",
              "長治鄉",
              "麟洛鄉",
              "竹田鄉",
              "內埔鄉",
              "萬丹鄉",
              "潮州鎮",
              "泰武鄉",
              "來義鄉",
              "萬巒鄉",
              "崁頂鄉",
              "新埤鄉",
              "南州鄉",
              "林邊鄉",
              "東港鎮",
              "琉球鄉",
              "佳冬鄉",
              "新園鄉",
              "枋寮鄉",
              "枋山鄉",
              "春日鄉",
              "獅子鄉",
              "車城鄉",
              "牡丹鄉",
              "恆春鎮",
              "滿州鄉",
            ],
            value: [
              "屏東市",
              "三地門鄉",
              "霧台鄉",
              "瑪家鄉",
              "九如鄉",
              "里港鄉",
              "高樹鄉",
              "鹽埔鄉",
              "長治鄉",
              "麟洛鄉",
              "竹田鄉",
              "內埔鄉",
              "萬丹鄉",
              "潮州鎮",
              "泰武鄉",
              "來義鄉",
              "萬巒鄉",
              "崁頂鄉",
              "新埤鄉",
              "南州鄉",
              "林邊鄉",
              "東港鎮",
              "琉球鄉",
              "佳冬鄉",
              "新園鄉",
              "枋寮鄉",
              "枋山鄉",
              "春日鄉",
              "獅子鄉",
              "車城鄉",
              "牡丹鄉",
              "恆春鎮",
              "滿州鄉",
            ],
          },
        ],
        [
          {
            label: [
              "台東市",
              "綠島鄉",
              "蘭嶼鄉",
              "延平鄉",
              "卑南鄉",
              "鹿野鄉",
              "關山鎮",
              "海端鄉",
              "池上鄉",
              "東河鄉",
              "成功鎮",
              "長濱鄉",
              "太麻里",
              "金峰鄉",
              "大武鄉",
              "達仁鄉",
            ],
            value: [
              "台東市",
              "綠島鄉",
              "蘭嶼鄉",
              "延平鄉",
              "卑南鄉",
              "鹿野鄉",
              "關山鎮",
              "海端鄉",
              "池上鄉",
              "東河鄉",
              "成功鎮",
              "長濱鄉",
              "太麻里",
              "金峰鄉",
              "大武鄉",
              "達仁鄉",
            ],
          },
        ],
        [
          {
            label: [
              "花蓮市",
              "新城鄉",
              "秀林鄉",
              "吉安鄉",
              "壽豐鄉",
              "鳳林鎮",
              "光復鄉",
              "豐濱鄉",
              "瑞穗鄉",
              "萬榮鄉",
              "玉里鎮",
              "卓溪鄉",
              "富里鄉",
            ],
            value: [
              "花蓮市",
              "新城鄉",
              "秀林鄉",
              "吉安鄉",
              "壽豐鄉",
              "鳳林鎮",
              "光復鄉",
              "豐濱鄉",
              "瑞穗鄉",
              "萬榮鄉",
              "玉里鎮",
              "卓溪鄉",
              "富里鄉",
            ],
          },
        ],
        [
          {
            label: ["南竿鄉", "北竿鄉", "莒光鄉", "東引鄉"],
            value: ["南竿鄉", "北竿鄉", "莒光鄉", "東引鄉"],
          },
        ],
      ],
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
    selectcvs() {
      console.log(this.select);
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
