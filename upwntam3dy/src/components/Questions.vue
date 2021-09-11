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
        :likes="10"
        owner="Abdelrahman Deghedy"
        text="What is the square root of 9?"
        :answersNumber="8"
        :time="Date.now()"
      />
    </div>
  </div>
</template>

<script>
import TheButton from "@/components/TheButton.vue";
import QuestionCard from "@/components/QuestionCard.vue";

export default {
  components: {
    TheButton,
    QuestionCard,
  },
  data() {
    return {
      //
    };
  },
};
</script>
