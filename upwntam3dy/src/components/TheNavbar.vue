<template>
  <div class="h-20 bg-gray-200 flex justify-around rounded-bl-lg rounded-br-lg">
    <router-link :to="{ name: 'Questions' }" class="flex">
      <div
        class="flex items-center cursor-pointer"
        @click="handlePageRouting()"
      >
        UpWntaM3dy
      </div>
    </router-link>
    <div class="flex items-center">&nbsp;</div>
    <div class="flex items-center">&nbsp;</div>
    <div class="flex items-center">&nbsp;</div>
    <div class="flex items-center">&nbsp;</div>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      //
    };
  },
  methods: {
    handlePageRouting() {
      this.$store.commit("setPageMode", "questions");
    },
  },
};
</script>
