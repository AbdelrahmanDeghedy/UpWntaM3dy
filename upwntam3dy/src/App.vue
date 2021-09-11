<template>
  <div class="bg-yellow-100 min-h-screen">
    <the-navbar />
    <question-layout class="mt-4">
      <template #questionDetail>
        <question-detail />
      </template>
      <template #questions>
        <questions />
      </template>
      <template #questionCreate>
        <question-create />
      </template>
    </question-layout>
  </div>
</template>

<script>
import "./index.css";
import TheNavbar from "@/components/TheNavbar.vue";

import QuestionLayout from "@/layouts/QuestionLayout.vue";
import QuestionDetail from "@/components/QuestionDetail.vue";
import Questions from "@/components/Questions.vue";
// import TheButton from "@/components/TheButton.vue";
import QuestionCreate from "@/components/QuestionCreate.vue";

export default {
  components: {
    TheNavbar,
    QuestionLayout,
    QuestionDetail,
    Questions,
    // TheButton,
    QuestionCreate,
  },
  data() {
    return {
      //
    };
  },
};
</script>

<style></style>
