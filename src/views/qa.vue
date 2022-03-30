<template>
  <n-form ref="formRef" :model="model" :rules="rules">
    <n-form-item path="age" label="Age">
      <n-input v-model:value="model.age" @keydown.enter.prevent />
    </n-form-item>
    
    <n-button round type="primary" @click="handleValidateButtonClick">
      Validate
    </n-button>
  </n-form>

  <pre
    >{{ JSON.stringify(model, null, 2) }}
</pre
  >
</template>

<script>
import { defineComponent, ref } from "vue";
import { useMessage } from "naive-ui";

export default defineComponent({
  setup() {
    const formRef = ref(null);
    const message = useMessage();
    const modelRef = ref({
      age: null,
    });
    const rules = {
      age: [
        {
          required: true,
          trigger: ["input", "blur"],
        },
      ],
    };
    return {
      formRef,
      model: modelRef,
      rules,
      handleValidateButtonClick(e) {
        e.preventDefault();
        formRef.value?.validate((errors) => {
          if (!errors) {
            message.success("Valid");
          } else {
            console.log(errors);
            message.error("Invalid");
          }
        });
      },
    };
  },
});
</script>