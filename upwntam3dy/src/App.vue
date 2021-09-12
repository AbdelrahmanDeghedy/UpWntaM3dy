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
import QuestionCreate from "@/components/QuestionCreate.vue";

import { users, answers, questions, courseInfoPerTerm } from '@/_utils/data';

export default {
  components: {
    TheNavbar,
    QuestionLayout,
    QuestionDetail,
    Questions,
    QuestionCreate,
  },
  mounted () {
    this.loadData();
  },
  methods : {
    loadData () {
      this.$store.commit ("loadUsers", users);
      this.$store.commit ("loadAnswers", answers);
      this.$store.commit ("loadQuestions", questions);
      this.$store.commit ("loadCourseInfoPerTerm", courseInfoPerTerm);
    }
  },
  data() {
    return {};
  },
};
</script>

<style></style>
