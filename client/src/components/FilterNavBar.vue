<template>
  <div :class="$store.state.mobileResponsive === true ? mobileClasses.container : laptopClasses.container">
    <div class="flex justify-center w-full" :class="$store.state.mobileResponsive === true ? '' : 'mt-8'">
      <input
        :class="$store.state.mobileResponsive === true ? mobileClasses.input : laptopClasses.input"
        class="h-8 rounded-md shadow-md outline-none mt-2 p-4 py-6 bg-gray-100 text-sm"
        @input="filterQuestions"
        type="text"
        v-model="searchText"
        placeholder="Search For a Specific Question"
      />
    </div>

    <!-- Selection Items -->
    <div class="flex flex-col items-center" :class="$store.state.mobileResponsive === true ? '' : 'mt-20'">
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
      value: "",
      mobileClasses : {
        input : "h-8 rounded-md shadow-md outline-none p-4 py-6 bg-gray-100 w-full text-sm",
        container: "h-auto rounded-xl mb-4 flex flex-col items-center bg-white p-4  w-1/2 mx-auto",
      },
      laptopClasses : {
        input : "h-8 rounded-md shadow-md outline-none p-4 py-6 bg-gray-100 w-full text-sm",
        container : "h-auto bg-white p-4 -mt-4 mr-6",
      }
    };
  },
  updated() {
    // console.log(this.$store.state.courseInfoPerTerm);
  },
  mounted() {
    this.loadTags();
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
