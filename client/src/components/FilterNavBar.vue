<template>
  <div class="h-auto bg-white p-4 -mt-4 mr-6">
    <!-- Search Input -->
    <div class="flex justify-center mt-8 w-full">
      <input
        class="h-8 rounded-md shadow-md outline-none p-4 py-6 bg-gray-100 w-full text-sm"
        @input="filterQuestions"
        type="text"
        v-model="searchText"
        placeholder="Search For a Specific Question"
      />
    </div>

    <!-- Selection Items -->
    <div class="mt-20 flex flex-col items-center">
      <the-selector label="Tag" :values="tags" @currentValueChange="syncSelectedTag" />
      <div class="flex justify-center">
        <the-button 
          class="mr-2"
          @click="clearTags"
          content="Clear"
          type="primary"
          size="small"
        />
        <the-button 
          @click="filterByTag"
          content="Filter"
          type="secondary"
          size="small"
        />
      </div>
    </div>
  </div>
</template>

<script>
import TheSelector from "@/components/TheSelector.vue";
import TheButton from "@/components/TheButton.vue";
import currentuserDataMixin from '@/mixins/currentuserDataMixin';
  
export default {
  mixins: [currentuserDataMixin],
  components: {
    TheSelector,
    TheButton
  },
  data() {
    return {
      tags: [],
      selectedTag: "",
      searchText: "",
      value: ""
    };
  },
  updated() {
    // console.log(this.$store.state.courseInfoPerTerm);
  },
  mounted() {
    this.loadTags();
    
    console.log(this.$store.state.questions);
  },
  methods: {
    async loadTags(){
      this.tags = (await this.getTags())?.tags;
    },
    filterQuestions(){
      this.$store.commit("filterQuestions", this.searchText);
    },
    syncSelectedTag(tag){
      this.selectedTag = tag;
    },
    filterByTag(){
      this.$store.commit("filterQuestionsByTags", this.selectedTag);
    },
    clearTags(){
      this.$store.commit('clearFilterTags');
    },
  },
};
</script>
