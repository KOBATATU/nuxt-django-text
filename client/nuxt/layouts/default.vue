<template>
  <div>
    <form @submit.prevent="SubmitText">
      <label for>テキスト入力</label>
      <v-text-field v-model="form.input_text" label="テキスト"></v-text-field>
      <button type="submit">登録</button>
    </form>
    {{text}}
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        input_text: ""
      },
      text: ""
    };
  },
  methods: {
    async SubmitText() {
      if (this.text == "") {
        return;
      }

      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      const formData = new FormData();
      for (const data in this.form) {
        formData.append(data, this.form[data]);
      }
      try {
        const response = await this.$axios.$post("/predict/", formData, config); // eslint-disable-line
        this.text = response;
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>



