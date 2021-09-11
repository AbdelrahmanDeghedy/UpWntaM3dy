<template>
  <div :class="(mode === 'questionDetails' || 'questionCreate') && 'px-20'">
    <div class="flex justify-around">
      <filter-nav-bar v-if="mode === 'questions'" class="w-1/5" />
      <div :class="mode === 'questionDetails' ? 'w-4/5' : 'w-3/5'">
        <slot v-if="mode === 'questions'" name="questions"></slot>
        <slot v-if="mode === 'questionDetails'" name="questionDetail"></slot>
        <slot v-if="mode === 'questionCreate'" name="questionCreate"></slot>
      </div>

      <div class="w-1/5 ml-6 flex flex-col items-center mt-4">
        <the-button
          v-if="mode !== 'questionCreate'"
          content="Ask A Question"
          type="primary"
          size="large"
        />
        <leaderboard-card />
      </div>
    </div>
  </div>
</template>

<script>
import TheButton from "@/components/TheButton.vue";

import LeaderboardCard from "@/components/LeaderboardCard.vue";
import FilterNavBar from "@/components/FilterNavBar.vue";

export default {
  components: {
    TheButton,
    LeaderboardCard,
    FilterNavBar,
  },
  data() {
    return {
      mode: "questionCreate", // questions, questionDetails, or questionCreate
    };
  },
};
</script>

<style></style>
