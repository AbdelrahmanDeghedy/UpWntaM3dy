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
    <leaderboard-card 
      class="flex flex-col justify-center items-center w-auto mx-auto"
      v-else-if="$store.state.pageMode ==='leaderboard'"
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

<script>
import "./index.css";
import TheNavbar from "@/components/TheNavbar.vue";

import QuestionLayout from "@/layouts/QuestionLayout.vue";
import QuestionDetail from "@/components/QuestionDetail.vue";
import Questions from "@/components/Questions.vue";
import QuestionCreate from "@/components/QuestionCreate.vue";
import UserProfile from '@/components/UserProfile.vue';

import Auth from './components/Auth.vue';
import NotFound from './components/NotFound.vue';

import authMixin from '@/mixins/authMixin';
import currentuserDataMixin from '@/mixins/currentuserDataMixin';
import LeaderboardCard from '@/components/LeaderboardCard.vue';

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
    LeaderboardCard,
  },
  data() {
    return {
      // mode: "questions", // questions, questionDetails, or questionCreate
      questions : {},
      users: {},
      windowWidth : 0,
    };
  },
  watch: {
    $route() {
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
      } else if (this.$route.name === "Leaderboard") {
        this.$store.commit("setPageMode", "leaderboard");
      } else if (this.$route.name === "NotFound") {
        this.$store.commit("setPageMode", "notfound");
      }
      
    },
    windowWidth : {
      // immediate: true,
      handler(){
        console.log(this.windowWidth);
        if (this.windowWidth < 900) {
          this.$store.state.mobileResponsive = true;
        } else {
          this.$store.state.mobileResponsive = false;
        }
      }
    }
  },
  async mounted() {
    this.$nextTick(() => {
        window.addEventListener('resize', this.onResize);
    })


    this.questions =  await this.getAllQuestions();
    this.users =  await this.getLeaderboard();   
    this.loadData();
  },
  updated(){
    // console.log(this.windowWidth);

  },

  methods: {
    onResize() {
        this.windowWidth = window.innerWidth;
    },
    loadData() {
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
