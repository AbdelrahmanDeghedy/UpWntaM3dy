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
          class="flex items-center ml-4 mr-4 w-10/12 flex-wrap"
          :class="{ 'order-last' : language === 'en' ? false : true }" 
          v-html="answer.body"
          :dir="language === 'en' ? 'ltr' : 'rtl'"
      >
      </div>
      
      <div class="flex items-center mr-16">
        <div class="flex">
          <div class="cursor-pointer" @click="toggleLike">
            <font-awesome-icon icon="thumbs-up" :style="{ color: currentLikeColor }" />
          </div>
          <div class="flex items-center justify-center ml-2">
            {{ answer.likes }} Likes
          </div>
        </div>
        <!-- <div
          class="ml-4 mt-2 bg-gray-500 w-8 h-8 flex  items-center justify-center rounded-full shadow-md cursor-pointer"
        >
          <font-awesome-icon icon="bookmark" :style="{ color: 'white' }" />
        </div> -->
      </div>
    </div>
   
  </div>
</template>

<script>
import getFromIdMixin from '@/mixins/getFromIdMixin';
import { getDayDifference } from '@/_utils/helper.ts'

import { isArabic } from '@/_utils/helper';


export default {
  props: {
    answer : {
      type : Object,
      required: true
    }
  },
  mixins: [ getFromIdMixin ],
  components: {
    // TheButton,
  },
  data() {
    return {
      language: "en",
      answerTime: this.answer.pub_date,
      currentLikeColor : "",
      answerLocal: this.answer,
    };
  },
  mounted(){
    this.initializeValues();
    this.handleLanguage();
  },
  methods: {
    handleLanguage(){
      if (isArabic(this.answerLocal.text)) {
        this.language = "ar";
      } else {
        this.language = "en";
      }
    },
    initializeValues(){
      this.currentLikeColor = this.answer.liked ? this.$store.state.likePrimaryColor : this.$store.state.likeSecondaryColor;
    },
    toggleLike(){
      // optimistic updates
      this.currentLikeColor = this.answer.liked ? this.$store.state.likeSecondaryColor : this.$store.state.likePrimaryColor,
      
      this.answerLocal.liked = !this.answerLocal.liked;
      this.answerLocal.likes = this.answerLocal.liked ? this.answerLocal.likes + 1 : this.answerLocal.likes - 1; 
      
      this.$emit("syncAnswersLikeState", this.answerLocal);
    },
  }
};
</script>
