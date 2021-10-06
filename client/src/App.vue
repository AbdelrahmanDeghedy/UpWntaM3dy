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

// import { users, answers, questions, courseInfoPerTerm } from "@/_utils/data";
import Auth from './components/Auth.vue';
import NotFound from './components/NotFound.vue';

import authMixin from '@/mixins/authMixin';
import currentuserDataMixin from '@/mixins/currentuserDataMixin';

export default {
  name: "App",
  mixins: [authMixin, currentuserDataMixin],
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
      questions : {},
      users: {},
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
  async mounted() {
    console.log("router mode", this.$store.state.pageMode);

    await this.login({ email : "test@test.com", password : "password" });
    // await this.createQuestion({ title: "test question", body: "from client", department: "comm", commaSeparatedTags: "" })
    // console.log(await this.getAllQuestions());
    
    this.questions =  await this.getAllQuestions();
    this.users =  await this.getLeaderboard();
    console.log(this.users.users);
    // const user = await this.getCurrentUser()
    // console.log(user);

    console.log(this.questions.questions);
    // this.logout();
    
    this.loadData();
  },

  methods: {
    loadData(): void {
      this.$store.commit("loadUsers", this.users.users);
      // this.$store.commit("loadAnswers", answers);
      this.$store.commit("loadQuestions", this.questions.questions);
      this.$store.commit("loadBackupQuestions", this.questions.questions);
      // this.$store.commit("loadCourseInfoPerTerm", courseInfoPerTerm);
      // console.log("done", this.$store.state.courseInfoPerTerm);
    },
  },
};
</script>

<style></style>
