<template>
  <n-space vertical>
    <n-layout has-sider>
      <n-layout-sider
        bordered
        collapse-mode="width"
        :collapsed-width="64"
        :width="240"
        :collapsed="collapsed"
        show-trigger
        @collapse="collapsed = true"
        @expand="collapsed = false"
      >
        <n-menu
          @update:value="handleUpdateValue"
          :collapsed="collapsed"
          :collapsed-width="64"
          :collapsed-icon-size="22"
          :options="menuOptions"
          :render-label="renderMenuLabel"
          :render-icon="renderMenuIcon"
          :expand-icon="expandIcon"
        />
      </n-layout-sider>
      <n-layout>
        <span><router-view></router-view></span>
      </n-layout>
    </n-layout>
  </n-space>
</template>

<script>
import { h, defineComponent } from "vue";
import { useMessage } from "naive-ui";

const menuOptions = [
  {
    label: "商品管理",
    key: "product",
  },{
    label: "使用者管理",
    key: "User",
  },
  {
    label: "商品頁banner管理",
    key: "banner",
  },
];

export default defineComponent({
  setup() {
    window.$message = useMessage();
    return {
      menuOptions,
      renderMenuLabel(option) {
        if ("href" in option) {
          return h("a", { href: option.href, target: "_blank" }, option.label);
        }
        return option.label;
      },
    };
  },
  mounted() {
    const isLogin = localStorage.getItem("account");
    if (isLogin != null) {
      this.islogin = true;
      this.account = localStorage.getItem("account");
    } else {
      
      this.$router.push({ path: "/adm" });
      window.$message.error("您尚未登入");
      this.islogin = false;
    }
  },
  methods: {
    handleUpdateValue(value) {
      this.$router.push({ path: "/admindex/" + value, params: { userId: 1 } });
    },
  },
});
</script>