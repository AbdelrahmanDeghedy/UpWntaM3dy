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
        <div class="flex">
            <div class="w-6 h-6 mr-2 rounded-full overflow-hidden shadow-lg flex justify-center items-center">
                <img 
                    class="w-6 h-6"
                    :src="userImg || $store.state?.alternativeImg"
                    alt="profile pic"
                >
            </div>

            <div class="text-blue-800 font-bold">{{ owner }}</div>
        </div>
        <div class="opacity-80 ml-2">{{ time }} </div>
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
import authMixin from '@/mixins/authMixin';
import currentuserDataMixin from '@/mixins/currentuserDataMixin';
// import { questions } from '@/_utils/data';
import { getDayDifference } from "@/_utils/helper";
import { isArabic } from '@/_utils/helper';

export default {
  mixins: [ getFromIdMixin, authMixin, currentuserDataMixin ],
  props: {
    question: {
      type: Object,
      required: true,
    },
  },
  components: {
    TheButton,
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
      userImg: "",

      currentLikeColor: this.findQuestionById(this.id).liked ? this.$store.state.likePrimaryColor : this.$store.state.likeSecondaryColor,
      currentBookmarkColor: this.findQuestionById(this.id).bookmarked ? this.$store.state.bookmarkPrimaryColor : this.$store.state.bookmarkSecondaryColor,
    };
  },
      async mounted(){
        await this.initializeValues();
        this.handleLanguage();
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
    async initializeValues(){
      this.answersNumber = this.question.answerIds.length;
      this.text = this.question.title;
      this.owner =  this.getUsernameFromUniversityId(this.question.owner);
      this.time = this.question.pub_date;
      this.likes = this.question.likes;
      this.id = this.question.id;
      

      const currentUser = await this.currentUser();
      this.userImg = currentUser.picture;
      
      if (currentUser.likedQuestionIds.includes (this.id)) {
        this.currentLikeColor = this.$store.state.likePrimaryColor;
      } else {
        this.currentLikeColor = this.$store.state.likeSecondaryColor;
      }

      
      if (currentUser.bookmarkedQuestionIds.includes (this.id)) {
        this.currentBookmarkColor = this.$store.state.bookmarkPrimaryColor;
      } else {
        this.currentBookmarkColor = this.$store.state.bookmarkSecondaryColor;
      }

    },
    async toggleBookmark(){
        if (this.currentBookmarkColor !== this.$store.state.bookmarkPrimaryColor) {
          await this.bookmarkQuestion(this.id);
          // optimistic updates
          this.currentBookmarkColor = this.$store.state.bookmarkPrimaryColor;
        } else {
          await this.removeBookmarkQuestion(this.id);
          // optimistic updates
          this.currentBookmarkColor = this.$store.state.bookmarkSecondaryColor;
        }
    },
    async toggleLike(){
        if (this.currentLikeColor !== this.$store.state.likePrimaryColor) {
          await this.likeQuestion(this.id);
          // optimistic updates
          this.currentLikeColor = this.$store.state.likePrimaryColor;
          this.likes += 1;
        } else {
          await this.dislikeQuestion(this.id);
          // optimistic updates
          this.currentLikeColor = this.$store.state.likeSecondaryColor;
          this.likes -= 1;
        }
    },
    handlePageRouting(): void {
      this.$store.commit("setPageMode", "questionDetails");
    },
  },
};
</script>
