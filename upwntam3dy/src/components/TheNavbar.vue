<template>
  <div class="h-20 bg-gray-200 flex justify-around rounded-bl-lg rounded-br-lg">
    <router-link :to="{ name: 'Questions' }" class="flex">
      <div
        class="flex items-center cursor-pointer"
        @click="handlePageRouting('questions')"
      >
        UpWntaM3dy
      </div>
    </router-link>
    <router-link :to="{ name: 'Profile' }" class="flex">
      <div
        class="flex items-center cursor-pointer"
        @click="handlePageRouting('profile')"
      >
        Profile
      </div>
    </router-link>
    <router-link :to="{ name: 'Signin' }" class="flex">
      <div
        class="flex items-center cursor-pointer"
        @click="handlePageRouting('auth')"
      >
        Sign in
      </div>
    </router-link>
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
    handlePageRouting(mode) {
      this.$store.commit("setPageMode", mode);
    },
  },
};
</script>
