<template>
  <div class="container">
    <div class="row">
      <n-input-group>
        <n-input
          v-model:value="RouteID"
          v-on:keyup.enter="subtotal"
          clearable
        />
        <n-button type="primary" ghost v-on:click="subtotal"> 搜尋 </n-button>
      </n-input-group>
    </div>

    <n-tabs type="segment" style="margin-top: 10px">
      <n-tab-pane name="chap1" v-bind:tab="DepartureStopNameZh">
        <n-space
          v-for="project in DepartureStoplist"
          v-bind:key="project.name"
          vertical
          :size="10"
          style="margin-top: 10px"
        >
          <n-alert v-bind:title="project.name" type="default"> </n-alert>
        </n-space>
      </n-tab-pane>

      <n-tab-pane name="chap2" v-bind:tab="DestinationStopNameZh">
        <n-space
          v-for="project in DestinationStoplist"
          v-bind:key="project.name"
          vertical
          :size="10"
          style="margin-top: 10px"
        >
          <n-alert v-bind:title="project.name" type="default"> </n-alert>
        </n-space>
      </n-tab-pane>
    </n-tabs>
    <div class="google-map" id="map"></div>
  </div>
</template>
  
  

<script>
import "axios";
import jsSHA from "jssha";

export default {
  name: "About",
  components: {},
  mounted() {
    let recaptchaScript = document.createElement("script");
    recaptchaScript.setAttribute(
      "src",
      "https://www.google.com/recaptcha/api.js"
    );
    document.head.appendChild(recaptchaScript);
  },
  data() {
    return {
      RouteID: "9009", //路線代碼
      DepartureStopNameZh: "", //起點
      DestinationStopNameZh: "", //終點
      DepartureStoplist: [], //去程站牌
      DestinationStoplist: [], //反程站牌
    };
  },
  methods: {
    subtotal: function () {
      this.DepartureStopNameZh = "";
      this.DestinationStopNameZh = "";
      this.DepartureStoplist = [];
      this.DestinationStoplist = [];
      //列出所有站牌
      fetch(
        "https://ptx.transportdata.tw/MOTC/v2/Bus/StopOfRoute/InterCity/" +
          this.RouteID +
          "?%24format=JSON"
      )
        .then((data) => {
          return data.json();
        })
        .then((ret) => {
          if (ret.length === 0) return;

          for (var i = 0; i < ret[0].Stops.length; i++) {
            this.DepartureStoplist.push({
              name: ret[0].Stops[i].StopName.Zh_tw,
            });

            this.DestinationStoplist.push({
              name: ret[ret.length - 1].Stops[i].StopName.Zh_tw,
            });
          }
        });
      //起迄點
      fetch(
        "https://ptx.transportdata.tw/MOTC/v2/Bus/Route/InterCity/" +
          this.RouteID +
          "?%24format=JSON"
      )
        .then((data) => {
          return data.json();
        })
        .then((ret) => {
          if (ret.length === 0) return;
          this.DepartureStopNameZh = ret[0].DepartureStopNameZh;
          this.DestinationStopNameZh = ret[0].DestinationStopNameZh;
        });

      //起迄點
      fetch(
        "https://ptx.transportdata.tw/MOTC/v2/Bus/EstimatedTimeOfArrival/Streaming/InterCity/9009?%24filter=Direction%20eq%20'1'&%24top=30&%24format=JSON",
        { headers: this.getAuthorizationHeader() }
      )
        .then((data) => {
          return data.json();
        })
        .then((ret) => {
          if (ret.length === 0) return;
          console.log("123");
        });
    },
    getAuthorizationHeader: function () {
      var AppID = "9e44be4efea845fcac241258a5fd94ae";
      var AppKey = "-avNhKkekGQITmfTEMF5yiTNeNQ";

      var GMTString = new Date().toGMTString();
      var ShaObj = new jsSHA("SHA-1", "TEXT");
      ShaObj.setHMACKey(AppKey, "TEXT");
      ShaObj.update("x-date: " + GMTString);
      var HMAC = ShaObj.getHMAC("B64");
      // eslint-disable-next-line
      var Authorization =
        'hmac username="' +
        AppID +
        '", algorithm="hmac-sha1", headers="x-date", signature="' +
        HMAC +
        '"';

      return { Authorization: Authorization, "X-Date": GMTString };
    },
  },
};
</script>