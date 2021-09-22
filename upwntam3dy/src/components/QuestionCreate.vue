<template>
  <div class="bg-white rounded-3xl p-6 flex flex-col shadow-md">
    <textarea
      v-model="text"
      @input="syncInput()"
      type="text"
      class="outline-none text-2xl question-text"
      placeholder="What's in Your Mind?"
      :dir="language === 'en' ? 'ltr' : 'rtl'"
    />
    <div class="flex justify-end">
      <the-button class="mt-4" :content="editMode ? 'Save' : 'Ask'" size="large" type="secondary" @click="editMode ? editQuestion() : createQuestion()" />
    </div>
    <div class="hidden" ref="markdown-content" :dir="language === 'en' ? 'ltr' : 'rtl'" v-html="markdown"></div>
  </div>
</template>

<script lang="ts">
import TheButton from "@/components/TheButton.vue";
import marked from "marked";
import { getDayDifference } from "@/_utils/helper";

import { randomIdGenerator } from '@/_utils/helper'
import { HTMLToText } from '@/_utils/helper'


// import { DateFormatter } from '@/_utils/dateFormatter';

export default {
  components: {
    TheButton,
  },
  props: {
    editMode : {
      type: Object,
      required: false,
      default : undefined
    },
    id: {
      type: String,
      required: false
    },
  },
  updated() {
    // console.log(this.markdown);
    console.log(this.markdown, HTMLToText(this.markdown).split("\n"));
  },
  mounted(){
    console.log(this.parseDate(new Date("2021-02-08"))); 
  },
  data() {
    return {
      markdown: "",
      text: this.editMode ? HTMLToText(this.editMode.editText) : "",
      language: "en", // or ar
    };
  },
  methods : {
    parseDate(date) {
      return getDayDifference(date);
    },
    syncInput(){
      this.markdown = marked(this.text);
    },
    editQuestion(){
      this.syncInput();
      this.$store.commit("editQuestionContent",{
        id : this.id,
        title : HTMLToText(this.markdown).split("\n")[0].replaceAll("&#39;", "'") + '..',
        fullQuestionText : this.markdown,
      })

      console.log(this.$store.state.questions);

      // Route to questions page
      this.$router.push({ name: "Questions" });
      this.$store.commit("setPageMode", "questions");
    },
    createQuestion(){
      this.$store.commit("createQuestion", {
        id: randomIdGenerator(),
        ownerId: 18010917,
        title: HTMLToText(this.markdown).split("\n")[0] + '..',
        fullQuestionText: this.markdown,
        time: this.parseDate(Date.now()),
        likes: 0,
        liked: false,
        answersIds: [],
      });

      // Clear the input field
      this.text = "";

      console.log(this.$store.state.questions);

      // Route to questions page
      this.$router.push({ name: "Questions" });
      this.$store.commit("setPageMode", "questions");

    },
  }
};
</script>

<style scoped>
.question-text {
}
</style>
