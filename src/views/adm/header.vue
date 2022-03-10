
<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/">Easy Shop</router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" to="/">首頁</router-link>
          </li>
        </ul>

        <span
          v-if="islogin"
          class="navbar-text"
          style="text-decoration: none; margin-right: 10px"
        >
          <router-link
            v-if="islogin"
            to="/Userinfo"
            style="text-decoration: none"
            >{{ account }}test</router-link
          >
        </span>

        <span class="navbar-text" style="text-decoration: none">
          <a
            v-if="islogin"
            to=""
            style="text-decoration: none"
            v-on:click="logout"
            >登出</a
          >
        </span>
      </div>
    </div>
  </nav>
</template>

<script>
import { defineComponent } from "vue";
import { useMessage } from "naive-ui";

export default defineComponent({
  name: "header",
  components: {},
  data() {
    return {
      islogin: false,
    };
  },
  mounted() {
    const isLogin = localStorage.getItem("account");

    if (isLogin != null) {
      this.islogin = true;
      this.account = localStorage.getItem("account");
    } else {
      this.islogin = false;
    }
  },
  setup() {
    window.$message = useMessage();
    return {};
  },
  methods: {
    logout() {
      this.$router.push({ path: '/adm'});
      localStorage.removeItem("account");
      this.islogin = false;
      window.$message.success("您已登出");
      
    },
  },
});
</script>
