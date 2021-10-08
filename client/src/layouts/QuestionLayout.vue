<template>
  <div :class="['questionDetails', 'questionCreate'].includes(mode) && $store.state.mobileResponsive !== true ? 'px-20' : 'px-0'">
    <div class="flex justify-around">
      <filter-nav-bar v-if="mode === 'questions' && $store.state.mobileResponsive === false" class="w-1/5" />
      <div :class="questionCardWidth">
        <slot v-if="mode === 'questions'" name="questions"></slot>
        <slot v-if="mode === 'questionDetails'" name="questionDetail"></slot>
        <slot v-if="mode === 'questionCreate'" name="questionCreate"></slot>
      </div>

      <div v-if="$store.state.mobileResponsive !== true" class="w-1/5 ml-6 flex flex-col items-center mt-4">
        <router-link :to="{ name: 'Ask', params: { 'user_id': currentUserId } }">
          <the-button
            @click="handlePageRouting()"
            v-if="mode !== 'questionCreate'"
            content="Ask A Question"
            type="primary"
            size="large"
          />
        </router-link>
        <leaderboard-card />
      </div>
    </div>
  </div>
</template>

<script>
import TheButton from "@/components/TheButton.vue";

import LeaderboardCard from "@/components/LeaderboardCard.vue";
import FilterNavBar from "@/components/FilterNavBar.vue";
import authMixin from '@/mixins/authMixin';

export default {
  mixins: [authMixin],
  components: {
    TheButton,
    LeaderboardCard,
    FilterNavBar,
  },
  updated() {
    //
  },
  data() {
    return {
      mode: this.$store.state.pageMode,
      currentUserId: 0,
    };
  },
  computed: {
    questionCardWidth(){
      if (this.$store.state.mobileResponsive === true) {
        return 'w-full';
      }
      else if (this.mode === 'questionDetails') {
        return 'w-4/5';
      } else {
        return 'w-3/5'
      }
    }
  },
  mounted() {
    this.setCurrentUser();
    
  },
  methods: {
    async setCurrentUser(){
      this.currentUserId = (await this.getCurrentUser()).currentUserId;
    },
    handlePageRouting() {
      this.$store.commit("setPageMode", "questionCreate");
    },
  },
};
</script>

<style></style>
