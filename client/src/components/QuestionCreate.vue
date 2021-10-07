<template>
  <!-- <div class="bg-white rounded-3xl p-6 flex flex-col shadow-md"> -->
  <form :class="answerMode ? answerConfig.containerClass: createConfig.containerClass">
    <textarea
      :class="answerMode ? answerConfig.textareaClass : createConfig.textareaClass"
      v-model="text"
      @input="syncInput()"
      @keyup="handleLanguage"
      type="text"
      :placeholder="answerMode ? answerConfig.textareaPlaceholder : createConfig.textareaPlaceholder"
      :dir="language === 'en' ? 'ltr' : 'rtl'"
      required
    />
    <input 
        v-if="!answerMode"
        class="border p-4 rounded-xl shadow outline-none mb-4"
        type="text"
        placeholder="Space Separated Tags"
        v-model="spaceSeparatedTags"
        @input="constructListedTags"
        required
    >
    <div v-if="!answerMode" class="ml-8">
      <span class="font-bold"> Tags: </span> {{ listedTags }}
    </div>
    <div class="flex justify-end">
      <the-button 
        class="mt-4"
        :size="answerMode ? answerConfig.buttonSize : createConfig.buttonSize"
        :content="answerMode ? answerConfig.buttonContent : createConfig.buttonContent"
        type="secondary"
        @click.prevent="handleClickingMode" 
      />
    </div>
    <div class="hidden" ref="markdown-content" :dir="language === 'en' ? 'ltr' : 'rtl'" v-html="markdown"></div>
  </form>
</template>



<script lang="ts">
import TheButton from "@/components/TheButton.vue";
import marked from "marked";
import { getDayDifference } from "@/_utils/helper";

import { randomIdGenerator } from '@/_utils/helper'
import { HTMLToText } from '@/_utils/helper'
import { isArabic } from '@/_utils/helper';

import currentuserDataMixin from '@/mixins/currentuserDataMixin';
import getFromIdMixin from '@/mixins/getFromIdMixin';
import authMixin from '@/mixins/authMixin';


// import { DateFormatter } from '@/_utils/dateFormatter';

export default {
  components: {
    TheButton,
  },
  mixins: [currentuserDataMixin, getFromIdMixin, authMixin],
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
    qid: {
      type: String,
      required: false
    },
  },

  data() {
    return {
      markdown: "",
      spaceSeparatedTags: this.editMode ? this.editMode.editTags : "",
      listedTags: "",
      text: this.editMode ? HTMLToText(this.editMode.editText) : "",
      language: "en",
      createConfig : {
        containerClass: "bg-white rounded-3xl p-6 flex flex-col shadow-md",
        textareaClass: "outline-none text-2xl question-text shadow border rounded-lg p-4 mb-4",
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
  async mounted(){
      // console.log("test", this.editMode)
      
  },
  methods : {
    constructListedTags(){
      const tags = this.spaceSeparatedTags.split(" ");
      this.listedTags = tags.join(",");
    },
    handleLanguage(){
      if (isArabic(this.text)) {
        this.language = "ar";
      } else {
        this.language = "en";
      }
    },
    handleClickingMode(){
      if (this.editMode) {
        this.editTheQuestion();
      } else if (this.answerMode) {
        this.answerQuestion();
      } else {
        this.createNewQuestion();
      }
    },
    parseDate(date) {
      return getDayDifference(date);
    },
    syncInput(){
      this.markdown = marked(this.text);
      console.log(this.markdown);
    },
    async answerQuestion(){
      const body = this.markdown;
      if (!this.text) return;
      
      await this.createQuestionAnswer(this.qid, { body })

      const answers = await this.getQuestionAnswers (this.qid);
      this.$store.commit("loadAnswers", answers.Answers);
      
      console.log("test", this.$store.state.answers);

      this.text = "";

    },
    async editTheQuestion(){
      this.syncInput();
      const title = HTMLToText(this.markdown).split("\n")[0].replaceAll("&#39;", "'") + '..';
      const body = this.markdown;
      
      await this.editQuestion (this.qid, { title, body, commaSeparatedTags: this.listedTags })

      this.questions =  await this.getAllQuestions();
      this.$store.commit("loadQuestions", this.questions.questions);

      const currentUserId = await this.getCurrentUser();
      console.log("sss", currentUserId);

      // Route to questions page
      this.$router.push({ name: "Questions", params: { 'user_id': currentUserId.currentUserId } });
      this.$store.commit("setPageMode", "questions");
    },
    async createNewQuestion(){
      if (!this.text || !this.spaceSeparatedTags) return;
      this.syncInput();
      
      const currentUser = await this.currentUser();
      console.log(currentUser);


      const title = HTMLToText(this.markdown).split("\n")[0] + '..';
      const body = this.markdown;
      const res = await this.createQuestion({ title, body, department: currentUser.department, commaSeparatedTags: this.listedTags  })
      console.log(res);
      
      this.questions =  await this.getAllQuestions();
      this.$store.commit("loadQuestions", this.questions.questions);

      // Clear the input field
      this.text = "";

      // // Route to questions page
      this.$router.push({ name: "Questions", params: { 'user_id': currentUser.universityId } });
      this.$store.commit("setPageMode", "questions");

    },
  }
};
</script>

<style scoped>
.question-text {
}
</style>
