<template>
  <div class="flex flex-col">
    <!-- Filter By Date Buttons -->
    <div class="flex justify-end">
      <the-button
        @click="handleActiveBtns(0)"
        :disabled="btnStates[0]"
        class="mr-4"
        content="Answers"
        :key="change"
        type="ternary"
        size="small"
      />
      <the-button
        @click="handleActiveBtns(1)"
        :disabled="btnStates[1]"
        class="mr-4"
        :key="change"
        content="Likes"
        type="ternary"
        size="small"
      />
      <the-button
        @click="handleActiveBtns(2)"
        class="mr-4"
        :disabled="btnStates[2]"
        :key="change"
        content="Date"
        type="ternary"
        size="small"
      />
    </div>
    <!-- Question cards -->
    <div class="flex flex-col mt-4" :key="change">
      <question-card
        v-for="(question, index) in renderedQuestions"
        :key="index"
        :question="question"
      />
    </div>

  <!-- <div :key="change"> -->
      <pagination-buttons 
        class="mb-10"
        :list="$store.state.questions"
        @paginatedList="syncCurrentList"
      />
  <!-- </div> -->

  </div>
</template>

<script>
import TheButton from "@/components/TheButton.vue";
import QuestionCard from "@/components/QuestionCard.vue";
import PaginationButtons from '@/components/PaginationButtons.vue';


export default {
  components: {
    TheButton,
    QuestionCard,
    PaginationButtons,
  },
  updated(){
    // console.log(this.$store.state.questions);
    // console.log("backup", this.$store.state.backupQuestions);
  },
  data() {
    return {
      activeBtn: "Day",
      btnStates: [true, true, false],
      change: 0,
      renderedQuestions: [],
    };
  },
  mounted () {
    //
  },
  methods: {
    syncCurrentList(questions){
      this.renderedQuestions = questions;
    },
    handleFilter(type) {
      this.activeBtn = type;
    },
    handleActiveBtns(val) {
      this.btnStates.forEach((btnState, index) => {
        this.btnStates[val] = false;
        index !== val && (this.btnStates[index] = true);
      })

      if (val === 0) {
        this.$store.commit ("sortQuestions", "answerIds");
        // this.syncCurrentList(this.$store.state.questions)
      } else if (val === 1) {
        this.$store.commit ("sortQuestions", "likes");
        // this.syncCurrentList(this.$store.state.questions)
      } else if (val === 2) {
        this.$store.commit ("sortQuestions", "pub_date");
        // this.syncCurrentList(this.$store.state.questions)
      }
        this.change = Math.random();
    },
  },
};
</script>

