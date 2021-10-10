<template>
  <div class="bg-gray-50 px-6 mt-10 rounded-xl overflow-hidden">
    <!-- First Name -->
    <div class="flex px-4 pt-4">

      <div class="flex flex-col items-center mx-2 justify-center">
        <div class="opacity-60">Rank</div>
        <div> 1 </div>
      </div>
      <div class="flex flex-col items-center mx-2">
        <img :src="users[0]?.picture || $store.state.alternativeImg" alt="Winner" class="w-14 rounded-full" />
        <router-link :to="{ name: 'Profile', params: { 'user_id': (users[0]?.universityId || 0) } }" class="flex">
          <div class="font-semibold text-xl mt-2"> {{ users[0]?.name }} </div>
        </router-link>

      </div>
      <div class="flex flex-col items-center justify-center mx-2">
        <div class="opacity-60">Points</div>
        <div>{{ users[0]?.points }}</div>
      </div>
    </div>

    <!-- Rest of names -->
    <div>
      <div v-for="(user, index) in users" :key="index">
        <div class="flex my-4" v-if="index > 0 && index < 5">
          <div class="mx-4 text-lg"> {{ index + 1 }} </div>
          <div class="mr-4">
            <img :src="user.picture || $store.state.alternativeImg" :alt="`${user.name}`" class="w-6 rounded-full" />
          </div>
          <router-link :to="{ name: 'Profile', params: { 'user_id': (user?.universityId || 0) } }" class="flex">
            <div> {{ user.name }} </div>
          </router-link>
          <div class="ml-2"> ({{ user.points }}) </div>
        </div>
        <hr />
      </div>
    </div>
  </div>
</template>

<script>
// import getFromIdMixin from '@/mixins/getFromIdMixin';
import currentuserDataMixin from '@/mixins/currentuserDataMixin';

export default {
  mixins: [currentuserDataMixin],
  data() {
    return {
      users : {},
    };
  },
  mounted(){
    this.initializeValues();

  },
  methods: {
    async initializeValues(){
        this.users = (await this.getLeaderboard()).users;
    },
  }
};
</script>
