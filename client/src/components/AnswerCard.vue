<template>
  <div class="bg-white rounded-xl overflow-hidden">
    <div class="w-4/6">
      <div class="flex ml-2 my-2">
        <div class="w-6 h-6 mr-2 rounded-full overflow-hidden shadow-lg flex justify-center items-center">
            <img 
                class="w-6 h-6"
                :src="owner.picture || $store.state?.alternativeImg"
                alt="profile pic"
            />
        </div>
        <div class="text-blue-800 font-bold">{{ owner.name }} </div>
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
            {{ localAnswerLikes }} Likes
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
      userImg: "",
      localAnswerLikes: 0,
      owner: ""
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
      const currentUser = await this.currentUser();
      this.userImg = currentUser.picture;
      this.owner =  await this.getUserFromId(this.answer.owner_id);
      
      this.localAnswerLikes = this.answer.likes;
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
            this.currentBookmarkColor = this.$store.state.bookmarkPrimaryColor;
        } else {
          await this.removeBookmarkAnswer(this.answer.id);
          this.currentBookmarkColor = this.$store.state.bookmarkSecondaryColor;
        }
    },
    async toggleLike(){
      if (this.currentLikeColor !== this.$store.state.likePrimaryColor) {
          await this.likeAnswer(this.answer.id);
          this.currentLikeColor = this.$store.state.likePrimaryColor;
          this.localAnswerLikes += 1;
        } else {
          await this.dislikeAnswer(this.answer.id);
          this.currentLikeColor = this.$store.state.likeSecondaryColor;
          this.localAnswerLikes -= 1;
        }
    },
  }
};
</script>
