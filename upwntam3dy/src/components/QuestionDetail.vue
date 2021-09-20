<template>
  <div class="shadow-md bg-white flex rounded-xl overflow-hidden m-2">
    <div class="py-6 w-1/6 flex flex-col">
      <div class="flex flex-col items-center my-2">
        <div>{{ answersNumber }} </div>
        <div class="opacity-60">Answers</div>
      </div>

      <!-- Likes -->
      <div class="flex flex-col items-center my-2">
        <div class="cursor-pointer">
          <font-awesome-icon icon="thumbs-up" :style="{ color: 'gray' }" />
        </div>
        <div>{{ likes }} Likes</div>
      </div>

      <!-- Bookmark -->
      <div class="flex flex-col items-center my-2">
        <div
          class="mt-2 bg-gray-500 w-8 h-8 flex items-center justify-center rounded-full shadow-md cursor-pointer"
        >
          <font-awesome-icon icon="bookmark" :style="{ color: 'white' }" />
        </div>
      </div>
    </div>

    <div class="flex flex-col w-5/6">
      <div class="flex justify-between">
        <div class="py-6 w-4/6 ml-4">
          <div class="text-2xl font-semibold">
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
          <the-button content="Edit" type="secondary" size="small" />
        </div>
      </div>

      <hr class="mx-4 -mt-4" />
      <div class="mt-4">
        <div class="ml-4 mb-4">
          {{ fullQuestionText }}
        </div>

        <div class="font-bold text-xl mb-2 ml-4">
          {{ answersNumber }} Answers
        </div>

        <hr class="mx-2" />

        <!-- Answers -->
        <div class="ml-4">
          <div v-for="answer in getAnswersOfQuestion($route.params.qId)" :key='answer'>
            <answer-card :answer="answer" />
            <hr class="mx-2" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AnswerCard from "@/components/AnswerCard";
import TheButton from "@/components/TheButton";

import getFromIdMixin from '@/mixins/getFromIdMixin';
import { getDayDifference } from '@/_utils/helper.ts'

export default {
  components: {
    AnswerCard,
    TheButton,
  },
  mixins: [ getFromIdMixin ],
  data() {
    return {
      likes : 0,
      answersNumber : 0,
      text : "",
      owner : "",
      fullQuestionText : "",
      time: 0,
    };
  },
  async mounted(){
    await setTimeout(() => {
      this.initializeValues();
    }, 0)
    
    // console.log("testt>", this.$route);
  },
  computed : {
//
  },
  methods :{
   initializeValues(){
      this.likes = this.findQuestionById(this.$route.params.qId)?.likes;
      this.answersNumber = this.getAnswersOfQuestion(this.$route.params.qId)?.length;
      this.text = this.findQuestionById(this.$route.params.qId)?.title;
      this.owner = this.getUsernameFromId(this.findQuestionById(this.$route.params.qId)?.ownerId);
      this.fullQuestionText = this.findQuestionById(this.$route.params.qId)?.fullQuestionText;
      this.time = getDayDifference (this.findQuestionById(this.$route.params.qId)?.time);
   }
  }
};
</script>
