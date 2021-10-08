<template>
  <div class="navbar shadow h-20 flex items-center justify-around rounded-bl-lg rounded-br-lg">
    <router-link active-class="selected" :to="{ name: 'Questions', params: { 'user_id': currentUserId } }" class="flex">
      <div
        class="flex items-center cursor-pointer"
        @click="handlePageRouting('questions')"
      >
        <span class="upColor"> UP </span> <span class="wntaColor"> Wnta </span> <span class="m3dyColor"> M3dy </span>
      </div>
    </router-link>
    <router-link active-class="selected" :to="{ name: 'Profile', params: { 'user_id': currentUserId } }" class="flex">
      <div
        class="flex items-center cursor-pointer"
        @click="handlePageRouting('profile')"
      >
        Profile
      </div>
    </router-link>
    <router-link active-class="selected" v-if="!isLoggedIn()" :to="{ name: 'Signin' }" class="flex">
      <div
        class="flex items-center cursor-pointer"
        @click="handlePageRouting('auth')"
      >
        Sign in
      </div>
    </router-link>
    <router-link active-class="selected" v-if="isLoggedIn()" :to="{ name: 'Signin' }" class="flex">
      <div
        class="flex items-center cursor-pointer"
        @click="signOut"
      >
        Sign out
      </div>
    </router-link>
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
    },
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

<style scoped>

.navbar {
background-color: #fff293;
background-image: linear-gradient(315deg, #fff293 0%, #ffe884 74%);

}

.selected {
  background-color: #fff;
  border-radius: 100rem;
  padding: .5rem 1rem;
  
}

.m3dyColor, .wntaColor, .upColor {
  /* font-size: 1.5rem; */
  font-weight: 700;
  
}
 
.m3dyColor {
  color: #FF06D7;
  

}
.wntaColor {
  color: #FF5106;
}

.upColor {
  color: #F7AF43;
} 

</style>