<template>
  <div class="bg-yellow-100 min-h-screen">
    <the-navbar />
    <!-- Page Content -->
    <div class="flex mt-4">
      <div class="w-1/4 h-screen bg-gray-50">LEFT</div>
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
      <div class="w-1/4 bg-gray-200">RIGHT</div>
    </div>
  </div>
</template>

<script>
import "./index.css";
import TheNavbar from "./components/TheNavbar.vue";
import TheButton from "./components/TheButton.vue";
import QuestionCard from "./components/QuestionCard.vue";

export default {
  components: {
    TheNavbar,
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

<style></style>
