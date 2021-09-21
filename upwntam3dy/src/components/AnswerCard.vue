<template>
  <div class="bg-white flex rounded-xl overflow-hidden">
    <div class="py-6 w-4/6">
      <div class="flex ml-2 my-2">
        <div class="text-blue-800 font-bold">{{ getUsernameFromId(answer.ownerId) }}</div>
        <div class="opacity-80 ml-2">{{ answerTime }} days ago</div>
      </div>
      <div class="ml-4">{{answer.text}}</div>
    </div>
    <div class="py-6 flex items-center">
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
</template>

<script>
import getFromIdMixin from '@/mixins/getFromIdMixin';
import { getDayDifference } from '@/_utils/helper.ts'


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
      answerTime: getDayDifference(this.answer.time),
      currentLikeColor : "",
      answerLocal: this.answer,
    };
  },
  mounted(){
    this.initializeValues();
  },
  methods: {
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
