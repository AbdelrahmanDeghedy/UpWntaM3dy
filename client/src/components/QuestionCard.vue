<template>
  <div class="shadow-md bg-white flex rounded-xl overflow-hidden m-2">
    <div class="py-6 w-1/6 flex flex-col justify-center items-center">
      <div>{{ answersNumber }}</div>
      <div class="opacity-60">Answers</div>
    </div>
    <div class="py-6 w-4/6">
      <router-link :to="{ name: 'Question', params: { qId: id, 'user_id': 18010917 } }">
        <div
          class="text-2xl font-semibold cursor-pointer"
          :dir="language === 'en' ? 'ltr' : 'rtl'"
          @click="handlePageRouting()"
        >
          {{ text }}
        </div>
      </router-link>
      <div class="flex ml-2 my-2">
        <div class="text-blue-800 font-bold">{{ owner }}</div>
        <div class="opacity-80 ml-2">{{ time }} days ago</div>
      </div>
      <div class="ml-4">
        <div class="flex">
          <div class="cursor-pointer" @click="toggleLike">
            <font-awesome-icon icon="thumbs-up" :style="{ color: currentLikeColor }" />
          </div>
          <div class="ml-2">{{ likes }} Likes</div>
        </div>
      </div>
    </div>
    <div class="py-6 w-1/6 flex flex-col items-center">
      <router-link :to="{ name: 'Question', params: { qId: id, 'user_id': 18010917 } }">
        <the-button content="Answer" type="secondary" size="small" @click="handleAnswerClick"/>
      </router-link>
      <div
        class="mt-2 bg-gray-100 w-8 h-8 flex items-center justify-center rounded-full shadow-md cursor-pointer"
        @click="toggleBookmark"
      >
        <font-awesome-icon icon="bookmark" :style="{ color: currentBookmarkColor }" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import TheButton from "./TheButton.vue";

import getFromIdMixin from '@/mixins/getFromIdMixin';
// import { questions } from '@/_utils/data';
import { getDayDifference } from "@/_utils/helper";
import { isArabic } from '@/_utils/helper';

export default {
  mixins: [ getFromIdMixin ],
  props: {
    question: {
      type: Object,
      required: true,
    },
  },
  components: {
    TheButton,
  },
  async mounted(){
    await this.initializeValues();
    this.handleLanguage();
    // console.log(this.findQuestionById(this.id));
    // console.log(this.$store.state.questions);
  },
  data(): any {
    return {
      language: "en",
      answersNumber: 0,
      text: "",
      owner: "",
      time: 0,
      likes: 0,
      id: 0,

      currentLikeColor: this.findQuestionById(this.id).liked ? this.$store.state.likePrimaryColor : this.$store.state.likeSecondaryColor,
      currentBookmarkColor: this.findQuestionById(this.id).bookmarked ? this.$store.state.bookmarkPrimaryColor : this.$store.state.bookmarkSecondaryColor,
    };
  },
  methods: {
    handleLanguage(){
      if (isArabic(this.text)) {
        this.language = "ar";
      } else {
        this.language = "en";
      }
    },
    handleAnswerClick(){
      this.handlePageRouting();
      this.$store.commit("toggleScrollToAnswer");
      // console.log(this.$store.state.scrollToAnswer);
    },
    initializeValues(){
      this.answersNumber = this.question.answersIds.length;
      this.text = this.question.title;
      this.owner =  this.getUsernameFromId(this.question.ownerId);
      this.time = this.question.time;
      this.likes = this.question.likes;
      this.id = this.question.id;
      this.currentLikeColor = this.findQuestionById(this.id).liked ? this.$store.state.likePrimaryColor : this.$store.state.likeSecondaryColor;
      this.currentBookmarkColor = this.findQuestionById(this.id).bookmarked ? this.$store.state.bookmarkPrimaryColor : this.$store.state.bookmarkSecondaryColor;

    },
    parseDate(date) {
      return getDayDifference(date);
    },
    toggleBookmark(){      
      this.findQuestionById(this.id).bookmarked = !this.findQuestionById(this.id).bookmarked;
      this.initializeValues();
    },
    toggleLike(){
      // optimistic updates
      
      this.findQuestionById(this.id).liked = !this.findQuestionById(this.id).liked;
      this.findQuestionById(this.id).likes = this.findQuestionById(this.id).liked ? this.findQuestionById(this.id).likes + 1 : this.findQuestionById(this.id).likes - 1; 
      
      this.initializeValues();
    },
    handlePageRouting(): void {
      this.$store.commit("setPageMode", "questionDetails");
    },
  },
};
</script>
