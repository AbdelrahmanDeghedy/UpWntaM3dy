<template>
  <div class="h-screen bg-white p-4 -mt-4 mr-6">
    <!-- Search Input -->
    <div class="flex justify-center mt-8">
      <input
        type="text"
        placeholder="Search For a Specific Question"
        class="h-8 rounded-md shadow-md outline-none p-4 py-6 text-l bg-gray-100"
      />
    </div>

    <!-- Selection Items -->
    <div class="mt-14 flex flex-col items-center">
      <the-selector defaultChoice="1" label="Term" :values="terms" />
      <the-selector label="Course" :values="courses" />
      <the-selector label="Tag" :values="['1', '2']" />
    </div>
  </div>
</template>

<script>
import TheSelector from "@/components/TheSelector.vue";

export default {
  components: {
    TheSelector,
  },
  data() {
    return {
      terms : [],
      courses : []
    };
  },
  updated(){
    console.log(this.$store.state.courseInfoPerTerm);

  },
  mounted(){
    this.loadTerms();
    this.loadCourses();
    // This component is rendered before app, so load the data (after 0!) to 
    // make the data be loaded (a hack!)
    // setTimeout(() => {console.log(this.$store.state.courseInfoPerTerm)}, 0);

  },
  methods : {
    loadTerms (){     
      setTimeout(() => {this.$store.state.courseInfoPerTerm.forEach(element => {
        this.terms.push (element.term);
      });}, 0);
    },
    loadCourses (){
      setTimeout(() => {this.$store.state.courseInfoPerTerm.forEach(element => {
        console.log(element.courses);
        this.courses.push (element.courses.name);
      });}, 0);
    },
  },
};
</script>
