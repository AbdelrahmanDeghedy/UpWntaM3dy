<template>
  <div v-if="questionMode === 'details'" class="shadow-md bg-white flex rounded-xl overflow-hidden m-2">
    <div class="py-6 w-1/6 flex flex-col">
      <div class="flex flex-col items-center my-2">
        <div>{{ answersNumber }} </div>
        <div class="opacity-60">Answers</div>
      </div>

      <!-- Likes -->
      <div class="flex flex-col items-center my-2">
        <div class="cursor-pointer" @click="toggleLike">
          <font-awesome-icon icon="thumbs-up" :style="{ color: currentLikeColor }" />
        </div>
        <div>{{ likes }} Likes</div>
      </div>

      <!-- Bookmark -->
      <div class="flex flex-col items-center my-2">
        <div
          class="mt-2 bg-gray-100 w-8 h-8 flex items-center justify-center rounded-full shadow-md cursor-pointer"
          @click="toggleBookmark"
        >
          <font-awesome-icon icon="bookmark" :style="{ color: currentBookmarkColor }" />
        </div>
      </div>
    </div>

    <div class="flex flex-col w-5/6">
      <div class="flex justify-between">
        <div class="py-6 w-4/6 ml-4">
          <div 
            class="text-2xl font-semibold"
            :dir="language === 'en' ? 'ltr' : 'rtl'"
          >
            {{ text }}
          </div>
          <div class="flex ml-2 my-2">
            <div class="text-blue-800 font-bold">
              {{ owner }}
            </div>
            <div class="opacity-80 ml-2">{{ time }} days ago</div>
          </div>
        </div>

        <div class="flex items-center mr-8">
          <the-button content="Edit" type="secondary" size="small" @click="handleEdit" />
        </div>
      </div>

      <hr class="mx-4 -mt-4" />
      <div class="mt-4">
        <div 
          class="ml-4 mb-4 px-8"
          v-html="fullQuestionText" 
          :dir="language === 'en' ? 'ltr' : 'rtl'"
        >
        </div>

        <div class="font-bold text-xl mb-2 ml-4">
          {{ answersNumber }} Answers
        </div>

        <hr class="mx-2" />

        <!-- Answers -->
        <div class="ml-4" :key="$store.state.answers.length">
          <div v-for="answer in answers" :key='answer'>
            <answer-card :answer="answer" @syncAnswersLikeState="syncAnswersLikeState" />
            <hr class="mx-2" />
          </div>
        </div>

        <div class="mt-4 mx-auto mb-4" ref="answerComment">
            <question-create 
              :answerMode="true"
              :qid="$route.params.qId"
            />
        </div>


      </div>
    </div>
  </div>
  <div v-else-if="questionMode === 'edit'">
    <question-create 
      :editMode = "{ editText : fullQuestionText }"
      :qid="$route.params.qId"
    />
  </div>
</template>

<script>
import AnswerCard from "@/components/AnswerCard";
import TheButton from "@/components/TheButton";
import QuestionCreate from '@/components/QuestionCreate.vue'

import currentuserDataMixin from '@/mixins/currentuserDataMixin';

import getFromIdMixin from '@/mixins/getFromIdMixin';
// import { getDayDifference } from '@/_utils/helper.ts'
import { isArabic } from '@/_utils/helper';



export default {
  components: {
    AnswerCard,
    TheButton,
    QuestionCreate,
  },
  mixins: [ getFromIdMixin, currentuserDataMixin ],
  data() {
    return {
      language: "en",
      likes : 0,
      answersNumber : 0,
      text : "",
      owner : "",
      fullQuestionText : "",
      time: 0,
      currentLikeColor : "",
      currentBookmarkColor: "",
      questionMode: "details",  // "details" or "edit"
      answers : [],
    };
  },
  updated(){
    this.scrollToAnswer();
  },
  async mounted(){
    await setTimeout(() => {
      this.initializeValues();
      this.scrollToAnswer();
      this.handleLanguage();
    }, 0)
    

    
  },
  computed : {
    //
  },
  methods :{
    async getAnswersOfQuestion(){
      const answers = await this.getQuestionAnswers(this.$route.params.qId);
      this.answers = answers.Answers;
    },
    handleLanguage(){
      if (isArabic(this.text)) {
        this.language = "ar";
      } else {
        this.language = "en";
      }
    },
    async scrollToAnswer(){
      if (!this.$store.state.scrollToAnswer) return;
      
      this.$refs.answerComment.scrollIntoView({behavior: 'smooth'});
      await setTimeout(() => {
        this.$store.commit("toggleScrollToAnswer");
      }, 0); 
    },
    handleEdit(){
     this.questionMode = "edit";
    },
   initializeValues(){
    //  console.log("??", this.findQuestionById(this.$route.params.qId)?.title);

      this.likes = this.findQuestionById(this.$route.params.qId)?.likes;
      this.answersNumber = this.getAnswersOfQuestion(this.$route.params.qId)?.length;
      this.text = this.findQuestionById(this.$route.params.qId)?.title;
      this.owner = this.getUsernameFromId(this.findQuestionById(this.$route.params.qId)?.ownerId);
      this.fullQuestionText = this.findQuestionById(this.$route.params.qId)?.body;
      this.time = this.findQuestionById(this.$route.params.qId)?.pub_date;

      this.currentLikeColor = this.findQuestionById(this.$route.params.qId)?.liked ? this.$store.state?.likePrimaryColor : this.$store.state?.likeSecondaryColor;
      this.currentBookmarkColor = this.findQuestionById(this.$route.params.qId)?.bookmarked ? this.$store.state?.bookmarkPrimaryColor : this.$store.state?.bookmarkSecondaryColor;
   },

    toggleBookmark(){
      this.currentBookmarkColor = this.$store.state.bookmarkSecondaryColor;
      this.currentBookmarkColor = this.findQuestionById(this.$route.params.qId).bookmarked ? this.$store.state.bookmarkSecondaryColor : this.$store.state.bookmarkPrimaryColor,
      
      this.findQuestionById(this.$route.params.qId).bookmarked = !this.findQuestionById(this.$route.params.qId)?.bookmarked;
    },
    toggleLike(){
      // optimistic updates
      this.currentLikeColor = this.findQuestionById(this.$route.params.qId).liked ? this.$store.state.likeSecondaryColor : this.$store.state.likePrimaryColor,
      
      this.findQuestionById(this.$route.params.qId).liked = !this.findQuestionById(this.$route.params.qId)?.liked;
      this.findQuestionById(this.$route.params.qId).likes = this.findQuestionById(this.$route.params.qId)?.liked ? this.findQuestionById(this.$route.params.qId).likes + 1 : this.findQuestionById(this.$route.params.qId).likes - 1; 
      
      this.initializeValues();
    },
    syncAnswersLikeState(answer){
      this.$store.state.answers.filter(ans => {
        return ans.id === answer.id;
      })[0].liked = answer.liked;

      this.$store.state.answers.filter(ans => {
        return ans.id === answer.id;
      })[0].likes = answer.likes;
    },
  }
};
</script>
