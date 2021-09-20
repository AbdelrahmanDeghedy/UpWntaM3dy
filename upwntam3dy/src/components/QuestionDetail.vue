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
          <div class="text-2xl font-semibold cursor-pointer">
            {{ text }}
          </div>
          <div class="flex ml-2 my-2">
            <div class="text-blue-800 font-bold">
              {{ owner }}
            </div>
            <div class="opacity-80 ml-2">{{ time }}2 days ago</div>
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
          <answer-card />
          <hr class="mx-2" />

          <answer-card />
          <hr class="mx-2" />

          <answer-card />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AnswerCard from "@/components/AnswerCard";
import TheButton from "@/components/TheButton";

export default {
  components: {
    AnswerCard,
    TheButton,
  },
  data() {
    return {
      likes : this.findQuestionById(this.$route.params.qId).likes,
      answersNumber : this.getAnswersOfQuestion(this.$route.params.qId).length,
      text : this.findQuestionById(this.$route.params.qId).title,
      owner : this.getUsernameFromId(this.findQuestionById(this.$route.params.qId).ownerId),
      fullQuestionText : this.findQuestionById(this.$route.params.qId).fullQuestionText,
    };
  },
  mounted(){
    console.log("testt>", this.$route.params.qId);
    console.log("testt>", this.getUsernameFromId(18010918));
    
    
  },
  computed : {
//
  },
  methods :{
    getUsernameFromId(uid){
      return this.$store.state.users.filter(user => {
        return user.universityId === uid
      })[0].name;
    },
    getAnswersOfQuestion(qId) {
      let answers = [];
      this.$store.state.answers.forEach((answer) => {
        console.log("testtt", qId);
        if (answer.questionOfAnswerId === +qId) {
          answers.push(answer);
        }
      });
      return answers;
    },
    findQuestionById (qId) {
      return this.$store.state.questions.filter((question) => {
        if (+question.id === +qId) {
          return question;
        }
      })[0]
    }
  }
};
</script>
