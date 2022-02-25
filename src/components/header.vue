
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
          <li class="nav-item">
            <router-link class="nav-link" to="/Shopcart">購物車</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/test">test</router-link>
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

        <span class="navbar-text" v-if="!islogin" style="text-decoration: none">
          <a
            style="text-decoration: none"
            @click="showLoginModal = true"
            v-if="!islogin"
            >登入</a
          >
        </span>
      </div>
    </div>
  </nav>

  <n-modal v-model:show="showLoginModal" content="Are you sure?">
    <n-card
      style="width: 600px"
      title=""
      :bordered="false"
      size="huge"
      role="dialog"
      aria-modal="true"
    >
      <n-tabs default-value="signin" size="large">
        <n-tab-pane name="signin" tab="登入">
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
        </n-tab-pane>

        <n-tab-pane name="forgetpassword" tab="忘記密碼">
          <n-form
            :model="forgetformValuea"
            ref="forvaildformRef"
            :rules="rules"
          >
            <n-form-item path="account" label="帳號">
              <n-input
                v-model:value="forgetformValuea.account"
                placeholder="請輸入帳號"
              />
            </n-form-item>
            <n-form-item path="email" label="信箱">
              <n-input
                type="email"
                v-model:value="forgetformValuea.email"
                placeholder="請輸入信箱"
                @keyup.enter="sendvailed"
              />
            </n-form-item>

            <n-button
              type="primary"
              @click="sendvailed()"
              block
              secondary
              strong
              :disabled="resetvaildbutton"
              >送出驗證碼
            </n-button>
          </n-form>
          <n-form
            :model="forgetformValueb"
            ref="formresetpasswordRef"
            :rules="rules"
          >
            <n-form-item
              path="vaildcode"
              label="驗證碼"
              style="margin-top: 20px"
            >
              <n-input
                v-model:value="forgetformValueb.vaildcode"
                placeholder="請輸入驗證碼"
                :disabled="resetvaildform"
              />
            </n-form-item>

            <n-form-item path="password" label="密碼">
              <n-input
                type="password"
                v-model:value="forgetformValueb.password"
                placeholder="請輸入新密碼"
                :disabled="resetvaildform"
              />
            </n-form-item>

            <n-form-item path="forreenteredPassword" label="密碼確認">
              <n-input
                type="password"
                v-model:value="forgetformValueb.reenteredPassword"
                placeholder="請重新輸入新密碼"
                :disabled="resetvaildform"
              />
            </n-form-item>

            <n-button
              type="primary"
              @click="resetpassword()"
              block
              secondary
              strong
              :disabled="resetvaildform"
              >重設密碼
            </n-button>
          </n-form>
        </n-tab-pane>

        <n-tab-pane name="signup" tab="註冊帳號">
          <n-form :model="signupformValue" ref="signupformRef" :rules="rules">
            <n-form-item path="account" label="帳號">
              <n-input
                v-model:value="signupformValue.account"
                placeholder="請輸入帳號"
              />
            </n-form-item>

            <n-form-item path="name" label="姓名">
              <n-input
                v-model:value="signupformValue.name"
                placeholder="請輸入姓名"
              />
            </n-form-item>

            <n-form-item path="phone" label="電話">
              <n-input
                v-model:value="signupformValue.phone"
                placeholder="請輸入電話"
              />
            </n-form-item>

            <n-form-item path="email" label="信箱">
              <n-input
                v-model:value="signupformValue.email"
                placeholder="請輸入信箱"
              />
            </n-form-item>
            
            <n-form-item path="password" placeholder="請輸入密碼" label="密碼">
              <n-input
                v-model:value="signupformValue.password"
                type="password"
              />
            </n-form-item>

            <n-form-item
              path="signupreenteredPassword"
              placeholder="請重新輸入密碼"
              label="確認密碼"
            >
              <n-input
                type="password"
                v-model:value="signupformValue.signupreenteredPassword"
              />
            </n-form-item>
            
            <n-button type="primary" @click="signup()" block secondary strong
              >註冊
            </n-button>
          </n-form>
        </n-tab-pane>
      </n-tabs>
    </n-card>
  </n-modal>
</template>

<script>
import { defineComponent, ref } from "vue";
import { useMessage } from "naive-ui";

export default defineComponent({
  name: "header",
  components: {},
  data() {
    const vailedemail = (rules, value) => {
      //eslint-disable-next-line
      if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(value)) {
        return true
      } else {
        return false
      }
    };
    const forformsamepassword = (rules, value) => {
      if (this.signupformValue.password === value) {
        return true;
      } else {
        return false;
      }
    };
    //註冊畫面密碼驗證
    const signupformsamepassword = (rules, value) => {
      if (this.signupformValue.password === value) {
        return true;
      } else {
        return false;
      }
    };
    return {
      islogin: false,
      resetvaildbutton: false, //重設密碼按鈕是否可案
      resetvaildform: true, //重設密碼欄位是否不可填寫
      resetaccount: "0",
      loginformValue: ref({
        account: "",
        password: "",
      }),
      signupformValue: ref({
        account: "",
        password: "",
        signupreenteredPassword: "",
        code:"",
        email: "",
        phone: "",
        age: "",
      }),
      forgetformValuea: ref({
        account: "",
        email: "",
      }),
      forgetformValueb: ref({
        vaildcode: "",
        password: "",
        reenteredPassword: "",
      }),
      rules: {
        email: [
          {
            required: true,
            message: "這是必填欄位",
            trigger: ["input", "blur"],
          },
          {
            validator: vailedemail,
            message: "信箱格式不正確",
            trigger: ["blur", "password-input"],
          },
        ],
        account: [
          {
            required: true,
            message: "這是必填欄位",
            trigger: ["input", "blur"],
          },
        ],
        name: [
          {
            required: true,
            message: "這是必填欄位",
            trigger: ["input", "blur"],
          },
        ],
        phone: [
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
        forreenteredPassword: [
          {
            required: true,
            message: "這是必填欄位",
            trigger: ["input", "blur"],
          },
          {
            validator: forformsamepassword,
            message: "Password is not same as re-entered password!",
            trigger: ["blur", "password-input"],
          },
        ],
        signupreenteredPassword: [
          {
            required: true,
            message: "這是必填欄位",
            trigger: ["input", "blur"],
          },
          {
            validator: signupformsamepassword,
            message: "Password is not same as re-entered password!",
            trigger: ["blur", "password-input"],
          },
        ],
        vaildcode: [
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
    const signupformRef = ref(null); //註冊帳號
    const forvaildformRef = ref(null); //忘記密碼驗證碼表單
    const formresetpasswordRef = ref(null); //重設密碼
    const loginformref = ref(null); //登入表單

    return {
      loginformref,
      signupformRef,
      forvaildformRef,
      formresetpasswordRef,
      showLoginModal: ref(false),
    };
  },
  methods: {
    resetpassword() {
      this.formresetpasswordRef.validate((valid) => {
        if (!valid) {
          fetch("http://localhost/api/resetpwd", {
            method: "post",
            headers: {
              Accept: "application/json",
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              id: this.resetaccount,
              code: this.forgetformValueb.vaildcode,
              password: this.forgetformValueb.password,
            }),
          })
            .then((data) => {
              return data.json();
            })
            .then((ret) => {
              if (ret.Status == "Failed") {
                window.$message.error(ret.Message);
              } else {
                this.forgetformValuea.email = "";
                this.forgetformValuea.account = "";
                this.forgetformValueb.vaildcode = "";
                this.forgetformValueb.password = "";
                this.forgetformValueb.reenteredPassword = "";
                this.resetvaildbutton = false; //重設密碼按鈕是否可案
                this.resetvaildform = true; //重設密碼欄位是否不可填寫
                window.$message.success(ret.Message);
              }
            });
        } else {
          return false;
        }
      });
    },
    sendvailed() {
      this.forvaildformRef.validate((valid) => {
        if (!valid) {
          this.resetvaildbutton = true;
          fetch("http://localhost/api/resetpwdsendvaild", {
            method: "post",
            headers: {
              Accept: "application/json",
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              account: this.forgetformValuea.account,
              email: this.forgetformValuea.email,
            }),
          })
            .then((data) => {
              return data.json();
            })
            .then((ret) => {
              if (ret.Status == "Failed") {
                this.resetvaildbutton = false;
                window.$message.error(ret.Message);
              } else {
                this.resetvaildform = false;
                this.resetaccount = ret.id;
                window.$message.success(ret.Message);
              }
            });
        } else {
          return false;
        }
      });
    },
    signup() {
      //註冊帳號
      this.signupformRef.validate((valid) => {
        if (!valid) {
          fetch("http://localhost/api/signup", {
            method: "post",
            headers: {
              Accept: "application/json",
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              account: this.signupformValue.account,
              password: this.signupformValue.password,
              name: this.signupformValue.name,
              phone: this.signupformValue.phone,
              email: this.signupformValue.email,
            }),
          })
            .then((data) => {
              return data.json();
            })
            .then((ret) => {
              if (ret.Status == "Success") {
                this.signupformValue.account=""
                this.signupformValue.password=""
                this.signupformValue.name=""
                this.signupformValue.phone=""
                this.signupformValue.email=""

                window.$message.success(ret.Message);
              } else {
                window.$message.error(ret.Message);
              }
            });
        } else {
          return false;
        }
      });
    },
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
                this.showLoginModal = false;
                this.islogin = true;
                localStorage.setItem("account", ret.data[0]);
                localStorage.setItem("id", ret.data[5]);
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
