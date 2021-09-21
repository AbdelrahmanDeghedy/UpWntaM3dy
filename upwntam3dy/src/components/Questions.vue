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
        :question="question"
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
  methods: {
    //
  },
  data() {
    return {
      //
    };
  },
};
</script>
