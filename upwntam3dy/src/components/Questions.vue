<template>
  <div>
    <!-- Filter By Date Buttons -->
    <div class="flex justify-end">
      <the-button class="mr-4" content="Month" type="ternary" size="small" />
      <the-button class="mr-4" content="Week" type="ternary" size="small" />
      <the-button class="mr-4" content="Day" type="ternary" size="small" />
    </div>
    <!-- Question cards -->
    <div class="flex flex-col mt-4 h-screen">
      <question-card
        v-for="question in this.$store.state.questions"
        :key="question"
        :id="question.id"
        :likes="question.likes"
        :owner="getUsernameFromUserId(question.ownerId)"
        :text="question.text"
        :answersNumber="question.answersIds.length"
        :time="parseDate(question.time)"
      />
    </div>
  </div>
</template>

<script>
import TheButton from "@/components/TheButton.vue";
import QuestionCard from "@/components/QuestionCard.vue";
import { getDayDifference } from "@/_utils/helper";

export default {
  components: {
    TheButton,
    QuestionCard,
  },
  methods: {
    getUsernameFromUserId(userId) {
      return this.$store.state.users.filter(
        (user) => user.UnniversityId === userId
      )[0].name;
    },
    parseDate(date) {
      return getDayDifference(date);
    },
  },
  data() {
    return {
      //
    };
  },
};
</script>
