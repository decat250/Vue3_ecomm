<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <n-card title="個人資料" style="margin-bottom: 16px">
          <n-tabs
            default-value="oasis"
            justify-content="space-evenly"
            type="line"
          >
            <n-tab-pane name="oasis" tab="個人資料">
              <n-form :model="model" ref="formRef" :rules="rules">
                <n-form-item path="age" label="帳號" >
                  <n-input  @keydown.enter.prevent disabled />
                </n-form-item>
                 <n-form-item path="name" label="姓名">
                  <n-input
                    type=""
                    @keydown.enter.prevent disabled
                  />
                </n-form-item>
                <n-form-item path="email" label="信箱">
                  <n-input
                    type=""
                    @keydown.enter.prevent
                  />
                </n-form-item>
                <n-form-item path="phone" label="電話號碼">
                  <n-input
                    type=""
                    @keydown.enter.prevent
                  />
                </n-form-item>
                
                <n-row :gutter="[0, 24]">
                  <n-col :span="24">
                    <div style="display: flex; justify-content: flex-end">
                      <n-button
                        round
                        type="primary"
                      >
                        Validate
                      </n-button>
                    </div>
                  </n-col>
                </n-row>
              </n-form>
            </n-tab-pane>
            <n-tab-pane name="the beatles" tab="購買記錄">
              Hey Jude
            </n-tab-pane>
            <n-tab-pane name="jay chou" tab="Jay Chou"> Qilixiang </n-tab-pane>
          </n-tabs>
        </n-card>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  mounted() {
    const isLogin = localStorage.getItem("account");
    this.userName = isLogin;
  },
  data() {
    return {
      userName: "Steven Chou",
      userId: 9527,
    };
  },
};
</script>
