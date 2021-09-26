<template>
  <div class="bg-yellow-100 min-h-screen">
    <the-navbar v-if="$store.state.pageMode !== 'notfound'" />
    <not-found v-if="$store.state.pageMode ==='notfound'"/>
    <auth 
      v-else-if="$store.state.pageMode ==='auth'"
      class="pt-10"
    />
    <user-profile 
      v-else-if="$store.state.pageMode ==='profile'"
      class="pt-10"
    />
    <question-layout v-else class="mt-4" :key="$store.state.pageMode">
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

<script lang="ts">
import "./index.css";
import TheNavbar from "@/components/TheNavbar.vue";

import QuestionLayout from "@/layouts/QuestionLayout.vue";
import QuestionDetail from "@/components/QuestionDetail.vue";
import Questions from "@/components/Questions.vue";
import QuestionCreate from "@/components/QuestionCreate.vue";
import UserProfile from '@/components/UserProfile.vue';

import { users, answers, questions, courseInfoPerTerm } from "@/_utils/data";
import Auth from './components/Auth.vue';
import NotFound from './components/NotFound.vue';

export default {
  name: "App",
  components: {
    TheNavbar,
    QuestionLayout,
    QuestionDetail,
    Questions,
    QuestionCreate,
    UserProfile,
    Auth,
    NotFound,
  },
  data() {
    return {
      // mode: "questions", // questions, questionDetails, or questionCreate
    };
  },
  watch: {
    $route(): void {
      if (this.$route.name === "Ask") {
        this.$store.commit("setPageMode", "questionCreate");
      } else if (this.$route.name === "Questions") {
        this.$store.commit("setPageMode", "questions");
      } else if (this.$route.name === "Question") {
        this.$store.commit("setPageMode", "questionDetails");
      } else if (this.$route.name === "Profile") {
        this.$store.commit("setPageMode", "profile");
      } else if (this.$route.name === "Signin" || this.$route.name === "Signup" ) {
        this.$store.commit("setPageMode", "auth");
      } else if (this.$route.name === "NotFound") {
        this.$store.commit("setPageMode", "notfound");
      }
      
    },
  },
  mounted(): void {
    this.loadData();
    console.log("router mode", this.$store.state.pageMode);
  },

  methods: {
    loadData(): void {
      this.$store.commit("loadUsers", users);
      this.$store.commit("loadAnswers", answers);
      this.$store.commit("loadQuestions", questions);
      this.$store.commit("loadBackupQuestions", questions);
      this.$store.commit("loadCourseInfoPerTerm", courseInfoPerTerm);
      console.log("done", this.$store.state.courseInfoPerTerm);
    },
  },
};
</script>

<style></style>
