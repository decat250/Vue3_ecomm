<template>
  <n-button
    :disabled="!fileListLength"
    @click="handleClick"
    style="margin-bottom: 12px"
  >
    Upload File
  </n-button>
  <n-upload
    @change="handleChange"
    action="https://www.mocky.io/v2/5e4bafc63100007100d8b70f"
    :default-upload="false"
    multiple
    ref="upload"
  >
    <n-button>Select File</n-button>
  </n-upload>
</template>

<script>
import { defineComponent, ref } from "vue";
import axios from 'axios'

export default defineComponent({
  setup() {
    const fileListLengthRef = ref(0);
    const uploadRef = ref(null);

    return {
      upload: uploadRef,
      fileListLength: fileListLengthRef,
      handleChange({ fileList }) {
        fileListLengthRef.value = fileList.length;
      },
      handleClick(param) {
        let fileObj = param.file;
        let form = new FormData();
        form.append("fileToUpload", fileObj);
        console.log(form); // output is: FormData {}; 需要使用 .get() 来读取
        console.log(form.get("fileToUpload")); // output is exactly the fileObj

        axios.post("http://127.0.0.1/api/uploadFile", form, {
          headers: { "content-type": "multipart/form-data" },
        });
      },
    };
  },
});
</script>