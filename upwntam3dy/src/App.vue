<template>
  <div class="bg-yellow-100 min-h-screen">
    <the-navbar />
    <!-- Page Content -->
    <div class="flex mt-4">
      <div class="w-1/4 h-screen bg-white p-4 -mt-4 mr-6">
        <!-- Search Input -->
        <div class="flex justify-center mt-8">
          <input
            type="text"
            placeholder="Search For a Specific Question"
            class="h-8 rounded-md shadow-md outline-none p-4 py-6 text-l bg-gray-100"
          />
        </div>

        <div class="mt-14 ml-6">
          <!-- Selection Item -->
          <div class="my-6 flex flex-col">
            <label for="terms" class="mb-2 font-bold">Term</label>
            <select
              name="terms"
              id="terms"
              class="w-60 rounded-lg p-2 outline-none bg-gray-200"
            >
              <option value="1">1</option>
            </select>
          </div>

          <div class="my-6 flex flex-col">
            <label for="terms" class="mb-2 font-bold">Course</label>
            <select
              name="terms"
              id="terms"
              class="w-60 rounded-lg p-2 outline-none bg-gray-200"
            >
              <option value="1">1</option>
            </select>
          </div>

          <div class="my-6 flex flex-col">
            <label for="terms" class="mb-2 font-bold">Tag</label>
            <select
              name="terms"
              id="terms"
              class="w-60 rounded-lg p-2 outline-none bg-gray-200"
            >
              <option value="1">1</option>
            </select>
          </div>
        </div>
      </div>
      <!-- Filter By Date Buttons -->
      <div class="w-1/2">
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
          <!-- Question Card -->
          <question-card />
          <question-card />
          <question-card />
        </div>
      </div>
      <div class="w-1/4 flex flex-col items-center mt-4">
        <the-button content="Ask A Question" type="primary" size="large" />
        <!-- Leaderboard Card -->
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

export default {
  components: {
    TheNavbar,
    TheButton,
    QuestionCard,
    LeaderboardCard,
  },
  data() {
    return {};
  },
};
</script>

<style></style>
