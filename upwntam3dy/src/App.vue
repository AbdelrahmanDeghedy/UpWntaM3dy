<template>
  <div class="bg-yellow-100 min-h-screen">
    <the-navbar />
    <!-- Page Content -->
    <div class="flex mt-4">
      <div class="w-1/5 h-screen bg-white p-4 -mt-4 mr-6">
        <!-- Search Input -->
        <div class="flex justify-center mt-8">
          <input
            type="text"
            placeholder="Search For a Specific Question"
            class="h-8 rounded-md shadow-md outline-none p-4 py-6 text-l bg-gray-100"
          />
        </div>

        <!-- Selection Items -->
        <div class="mt-14 flex flex-col items-center">
          <the-selector defaultChoice="1" label="Term" :values="['1', '2']" />
          <the-selector defaultChoice="1" label="Course" :values="['1', '2']" />
          <the-selector defaultChoice="1" label="Tag" :values="['1', '2']" />
        </div>
      </div>
      <div class="w-3/5">
        <!-- Filter By Date Buttons -->
        <div class="flex justify-end">
          <the-button
            class="mr-4"
            content="Month"
            type="ternary"
            size="small"
          />
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
      <div class="w-1/5 flex flex-col items-center mt-4">
        <the-button content="Ask A Question" type="primary" size="large" />
        <leaderboard-card />
      </div>
    </div>
  </div>
</template>

<script>
import "./index.css";
import TheNavbar from "./components/TheNavbar.vue";
import TheButton from "./components/TheButton.vue";
import QuestionCard from "./components/QuestionCard.vue";

import LeaderboardCard from "./components/LeaderboardCard.vue";
import TheSelector from "./components/TheSelector.vue";

export default {
  components: {
    TheNavbar,
    TheButton,
    QuestionCard,
    LeaderboardCard,
    TheSelector,
  },
  data() {
    return {};
  },
};
</script>

<style></style>
