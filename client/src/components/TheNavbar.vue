<template>
  <div class="h-20 bg-gray-200 flex justify-around rounded-bl-lg rounded-br-lg">
    <router-link :to="{ name: 'Questions', params: { 'user_id': currentUserId } }" class="flex">
      <div
        class="flex items-center cursor-pointer"
        @click="handlePageRouting('questions')"
      >
        UpWntaM3dy
      </div>
    </router-link>
    <router-link :to="{ name: 'Profile', params: { 'user_id': currentUserId } }" class="flex">
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
    <router-link :to="{ name: 'Signin' }" class="flex">
      <div
        class="flex items-center cursor-pointer"
        @click="signOut"
      >
        Sign out
      </div>
    </router-link>
    <div class="flex items-center">&nbsp;</div>
  </div>
</template>

<script>
import authMixin from '@/mixins/authMixin';

export default {
  mixins: [authMixin],
  data() {
    return {
      currentUserId: 0,
    };
  },
  computed :{
    watchToken(){
      return this.$store.state.token;
    }
  },
  watch :{
    watchToken(){
      this.setCurrentUser()
    }
  },
  mounted(){
    this.setCurrentUser();
  },
  methods: {
    async setCurrentUser(){
      this.currentUserId = (await this.getCurrentUser()).currentUserId || 0;
      // console.log("this.currentUserId", this.currentUserId);
    },
    signOut(){
        this.logout();
        this.$store.commit("setPageMode", "auth");
    },
    handlePageRouting(mode) {
      if (!this.isLoggedIn()) return;
      this.$store.commit("setPageMode", mode);
    },
  },
};
</script>
