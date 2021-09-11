<template>
  <div class="bg-white rounded-3xl p-6 flex flex-col shadow-md">
    <textarea
      v-model="text"
      type="text"
      class="outline-none text-2xl question-text"
      placeholder="What's in Your Mind?"
      :dir="language === 'en' ? 'ltr' : 'rtl'"
    />
    <div class="flex justify-end">
      <the-button class="mt-4" content="Ask" size="large" type="secondary" />
    </div>
    <div :dir="language === 'en' ? 'ltr' : 'rtl'" v-html="markdown"></div>
  </div>
</template>

<script>
import TheButton from "@/components/TheButton.vue";
import marked from "marked";

export default {
  components: {
    TheButton,
  },
  updated() {
    this.markdown = marked(this.text);
  },
  data() {
    return {
      markdown: "",
      text: "",
      language: "en", // or ar
    };
  },
};
</script>

<style scoped>
.question-text {
}
</style>
