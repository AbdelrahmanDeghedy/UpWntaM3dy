<template>
  <!-- <div class="bg-white rounded-3xl p-6 flex flex-col shadow-md"> -->
  <div :class="answerMode ? answerConfig.containerClass: createConfig.containerClass">
    <textarea
      :class="answerMode ? answerConfig.textareaClass : createConfig.textareaClass"
      v-model="text"
      @input="syncInput()"
      @keyup="handleLanguage"
      type="text"
      :placeholder="answerMode ? answerConfig.textareaPlaceholder : createConfig.textareaPlaceholder"
      :dir="language === 'en' ? 'ltr' : 'rtl'"
    />
    <div class="flex justify-end">
      <the-button 
        class="mt-4"
        :size="answerMode ? answerConfig.buttonSize : createConfig.buttonSize"
        :content="answerMode ? answerConfig.buttonContent : createConfig.buttonContent"
        type="secondary"
        @click="handleClickingMode" 
      />
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
import { isArabic } from '@/_utils/helper';

// import { DateFormatter } from '@/_utils/dateFormatter';

export default {
  components: {
    TheButton,
  },
  props: {
    answerMode :{
      type: Boolean,
      required: false,
      default: false,
    },
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
  data() {
    return {
      markdown: "",
      text: this.editMode ? HTMLToText(this.editMode.editText) : "",
      language: "en",
      createConfig : {
        containerClass: "bg-white rounded-3xl p-6 flex flex-col shadow-md",
        textareaClass: "outline-none text-2xl question-text",
        textareaPlaceholder : "What's in Your Mind?",
        buttonSize: "large",
        buttonContent: this.editMode ? 'Save' : 'Ask'
      },
      answerConfig :{
        containerClass: "bg-gray-100 rounded-3xl p-6 flex justify-between shadow-md w-11/12 mx-auto",
        textareaPlaceholder : "Do you have an answer?",
        textareaClass: "bg-gray-100 w-10/12 outline-none",
        buttonSize: "small",
        buttonContent: "Answer",
      }
    };
  },
  updated() {
    // console.log(this.markdown);
    // console.log(this.markdown, HTMLToText(this.markdown).split("\n"));
  },
  mounted(){
    //
  },
  methods : {
    handleLanguage(){
      if (isArabic(this.text)) {
        this.language = "ar";
      } else {
        this.language = "en";
      }
    },
    handleClickingMode(){
      if (this.editMode) {
        this.editQuestion();
      } else if (this.answerMode) {
        this.answerQuestion();
      } else {
        this.createQuestion();
      }
    },
    parseDate(date) {
      return getDayDifference(date);
    },
    syncInput(){
      this.markdown = marked(this.text);
    },
    answerQuestion(){
      this.$store.commit("createAnswer", {
        id: randomIdGenerator(),
        ownerId: 18010917,  // current user id
        questionOfAnswerId: this.id,
        text: this.markdown,
        time: this.parseDate(Date.now()),
        likes: 0,
        liked: false,
      });
      this.text = "";

    },
    editQuestion(){
      this.syncInput();
      this.$store.commit("editQuestionContent",{
        id : this.id,
        title : HTMLToText(this.markdown).split("\n")[0].replaceAll("&#39;", "'") + '..',
        fullQuestionText : this.markdown,
      })


      // Route to questions page
      this.$router.push({ name: "Questions", params: { 'user_id': 18010917 } });
      this.$store.commit("setPageMode", "questions");
    },
    createQuestion(){
      this.$store.commit("createQuestion", {
        id: randomIdGenerator(),
        ownerId: 18010917,  // current user id
        title: HTMLToText(this.markdown).split("\n")[0] + '..',
        fullQuestionText: this.markdown,
        time: this.parseDate(Date.now()),
        likes: 0,
        liked: false,
        answersIds: [],
      });

      // Clear the input field
      this.text = "";

      // console.log(this.$store.state.questions);

      // Route to questions page
      this.$router.push({ name: "Questions", params: { 'user_id': 18010917 } });
      this.$store.commit("setPageMode", "questions");

    },
  }
};
</script>

<style scoped>
.question-text {
}
</style>
