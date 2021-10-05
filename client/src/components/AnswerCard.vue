<template>
  <div class="bg-white rounded-xl overflow-hidden">
    <div class="w-4/6">
      <div class="flex ml-2 my-2">
        <div class="text-blue-800 font-bold">{{ getUsernameFromId(answer.owner_id) }} </div>
        <div class="opacity-80 ml-2">{{ answerTime }} </div>
      </div>
    </div>


    <div class="my-6 flex justify-between items-center px-4">

      <div 
          class="flex items-center ml-4 mr-4 w-9/12 flex-wrap"
          :class="{ 'order-last' : language === 'en' ? false : true }" 
          v-html="answer.body"
          :dir="language === 'en' ? 'ltr' : 'rtl'"
      >
      </div>
      
      <div class="flex flex-col  mr-16">
        <div class="flex">
          <div class="cursor-pointer" @click="toggleLike">
            <font-awesome-icon icon="thumbs-up" :style="{ color: currentLikeColor }" />
          </div>

          <div class="ml-2">
            {{ answer.likes }} Likes
          </div>
        </div>

          <div
            class="ml-4 mt-2 bg-gray-500 w-8 h-8 flex  items-center justify-center rounded-full shadow-md cursor-pointer"
            @click="toggleBookmark"
          >
            <font-awesome-icon icon="bookmark" :style="{ color: currentBookmarkColor }" />
        </div>

      </div>
    </div>
   
  </div>
</template>

<script>
import getFromIdMixin from '@/mixins/getFromIdMixin';
import currentuserDataMixin from '@/mixins/currentuserDataMixin';
import authMixin from '@/mixins/authMixin';

import { getDayDifference } from '@/_utils/helper.ts'

import { isArabic } from '@/_utils/helper';


export default {
  props: {
    answer : {
      type : Object,
      required: true
    }
  },
  mixins: [ getFromIdMixin, currentuserDataMixin, authMixin ],
  components: {
    // TheButton,
  },
  data() {
    return {
      language: "en",
      answerTime: this.answer.pub_date,
      currentLikeColor : "",
      currentBookmarkColor: "",
      answerLocal: this.answer,
    };
  },
  async mounted(){
    await this.initializeValues();
    this.handleLanguage();
  },
  methods: {
    handleLanguage(){
      if (isArabic(this.answerLocal.body)) {
        this.language = "ar";
      } else {
        this.language = "en";
      }
    },
    async initializeValues(){
      // this.currentLikeColor = this.answer.liked ? this.$store.state.likePrimaryColor : this.$store.state.likeSecondaryColor;
      const users =  await this.getLeaderboard();
      this.$store.commit("loadUsers", users.users);
      
      const currentUser = await this.currentUser();
      // console.log(this.answer.id);
      console.log(currentUser, currentUser.likedAnswerIds, this.id);
      if (currentUser.likedAnswerIds.includes (this.answer.id)) {
        this.currentLikeColor = this.$store.state.likePrimaryColor;
      } else {
        this.currentLikeColor = this.$store.state.likeSecondaryColor;
      }
      
      if (currentUser.bookmarkedAnswerIds.includes (this.answer.id)) {
        this.currentBookmarkColor = this.$store.state.bookmarkPrimaryColor;
      } else {
        this.currentBookmarkColor = this.$store.state.bookmarkSecondaryColor;
      }
    },
    async toggleBookmark(){
          if (this.currentBookmarkColor !== this.$store.state.bookmarkPrimaryColor) {
            await this.bookmarkAnswer(this.answer.id);
        } else {
          await this.removeBookmarkAnswer(this.answer.id);
        }
    },
    async toggleLike(){
      if (this.currentLikeColor !== this.$store.state.likePrimaryColor) {
        await this.likeAnswer(this.answer.id);
        } else {
          await this.dislikeAnswer(this.answer.id);
        }
          // this.$emit("syncAnswersLikeState", this.answerLocal);
    },
  }
};
</script>
