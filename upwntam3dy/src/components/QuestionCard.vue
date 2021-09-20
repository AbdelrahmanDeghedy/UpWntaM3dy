<template>
  <div class="shadow-md bg-white flex rounded-xl overflow-hidden m-2">
    <div class="py-6 w-1/6 flex flex-col justify-center items-center">
      <div>{{ answersNumber }}</div>
      <div class="opacity-60">Answers</div>
    </div>
    <div class="py-6 w-4/6">
      <router-link :to="{ name: 'Question', params: { qId: id } }">
        <div
          class="text-2xl font-semibold cursor-pointer"
          @click="handlePageRouting()"
        >
          <!-- What's the square root of 9? -->
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
            <font-awesome-icon icon="thumbs-up" :style="{ color: likeColor }" />
          </div>
          <div class="ml-2">{{ likes }} Likes</div>
        </div>
      </div>
    </div>
    <div class="py-6 w-1/6 flex flex-col items-center">
      <the-button content="Answer" type="secondary" size="small" />
      <div
        class="mt-2 bg-gray-100 w-8 h-8 flex items-center justify-center rounded-full shadow-md cursor-pointer"
        @click="toggleBookmark"
      >
        <font-awesome-icon icon="bookmark" :style="{ color: bookmarkColor }" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import TheButton from "./TheButton.vue";

import getFromIdMixin from '@/mixins/getFromIdMixin';

export default {
  mixins: [getFromIdMixin],
  props: {
    answersNumber: {
      type: Number,
      required: true,
      default: 0,
    },
    id: {
      type: Number,
      required: true,
      default: 0,
    },
    text: {
      type: String,
      required: true,
      default: "NO QUESTION PROVIDED!!",
    },
    owner: {
      type: String,
      required: true,
      default: "NO OWNER PROVIDED!!",
    },
    time: {
      type: Number,
      required: true,
      default: 100,
    },
    likes: {
      type: Number,
      required: true,
      default: 0,
    },
  },
  components: {
    TheButton,
  },
  mounted(){
    console.log(this.findQuestionById(this.id));
    console.log(this.$store.state.questions);
  },
  methods: {
    toggleBookmark(){
      this.bookmarkColor = this.$store.state.bookmarkSecondaryColor;
      this.bookmarkColor = this.findQuestionById(this.id).bookmarked ? this.$store.state.bookmarkSecondaryColor : this.$store.state.bookmarkPrimaryColor,
      
      this.findQuestionById(this.id).bookmarked = !this.findQuestionById(this.id).bookmarked;
    },
    toggleLike(){
      // optimistic updates
      this.likeColor = this.findQuestionById(this.id).liked ? this.$store.state.likeSecondaryColor : this.$store.state.likePrimaryColor,
      
      this.findQuestionById(this.id).liked = !this.findQuestionById(this.id).liked;
      
    },
    handlePageRouting(): void {
      this.$store.commit("setPageMode", "questionDetails");
    },
  },
  data(): any {
    return {
      likeColor: this.findQuestionById(this.id).liked ? this.$store.state.likePrimaryColor : this.$store.state.likeSecondaryColor,
      bookmarkColor: this.findQuestionById(this.id).bookmarked ? this.$store.state.bookmarkPrimaryColor : this.$store.state.bookmarkSecondaryColor,
    };
  },
};
</script>
