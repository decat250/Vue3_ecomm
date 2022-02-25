<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <n-card title="管理者登入">
        <n-form :model="loginformValue" ref="loginformref" :rules="rules">
          <n-form-item path="account" label="帳號">
            <n-input
              v-model:value="loginformValue.account"
              placeholder="請輸入帳號"
              clearable
            />
          </n-form-item>

          <n-form-item path="password" label="密碼">
            <n-input
              v-model:value="loginformValue.password"
              placeholder="請輸入密碼"
              @keyup.enter="login"
              type="password"
              clearable
            />
          </n-form-item>
        </n-form>
        <n-button type="primary" block secondary strong v-on:click="login"
          >登入
        </n-button>
      </n-card>
    </div>
  </div>
</template>
<script>
import { defineComponent, ref } from "vue";
import { useMessage } from "naive-ui";

export default defineComponent({
  name: "header",
  components: {},
  data() {
    return {
      islogin: false,

      loginformValue: ref({
        account: "",
        password: "",
      }),

      rules: {
        account: [
          {
            required: true,
            message: "這是必填欄位",
            trigger: ["input", "blur"],
          },
        ],
        password: [
          {
            required: true,
            message: "這是必填欄位",
            trigger: ["input", "blur"],
          },
        ],
      },
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

    const loginformref = ref(null); //登入表單

    return {
      loginformref,
      showLoginModal: ref(false),
    };
  },
  methods: {
    logout() {
      localStorage.removeItem("account");
      this.islogin = false;
      window.$message.success("您已登出");
    },
    login() {
      this.loginformref.validate((valid) => {
        if (!valid) {
          fetch("http://127.0.0.1/api/signin", {
            method: "post",
            headers: {
              Accept: "application/json",
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              account: this.loginformValue.account,
              password: this.loginformValue.password,
            }),
          })
            .then((data) => {
              return data.json();
            })
            .then((ret) => {
              if (ret.Status == "Success") {
                console.log(ret)
                this.$router.push({ path: '/admindex'})
                this.showLoginModal = false;
                this.islogin = true;
                localStorage.setItem("account", ret.data[0]);
                
                window.$message.success(ret.Message);
                this.loginformValue.account = "";
                this.loginformValue.password = "";
              } else {
                window.$message.error(ret.Message);
              }
            });
        } else {
          return false;
        }
      });
    },
  },
});
</script>


<style scoped>
.vertical-center {
  min-height: 100%; /* Fallback for browsers do NOT support vh unit */
  min-height: 100vh; /* These two lines are counted as one :-)       */

  display: flex;
  align-items: center;
}
</style>