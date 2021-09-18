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
      <the-selector
        defaultChoice="1"
        label="Term"
        :values="terms"
        @currentValueChange="getCurrentTerm"
      />
      <the-selector
        label="Course"
        :values="courses"
        @currentValueChange="getCurrentCourse"
      />
      <the-selector label="Tag" :values="tags" />
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
      terms: [],
      courses: [],
      tags: [],
      currentTerm: "1",
      currentCourse: "",
    };
  },
  updated() {
    console.log(this.$store.state.courseInfoPerTerm);
  },
  mounted() {
    this.loadTerms();
    this.loadCourses(this.currentTerm);
    // This component is rendered before app, so load the data (after 0!) to
    // make the data be loaded (a hack!)
    // setTimeout(() => {console.log(this.$store.state.courseInfoPerTerm)}, 0);
  },
  methods: {
    getCurrentCourse(currentCourse) {
      this.currentCourse = currentCourse;
      this.tags = [];
      this.loadTags(this.currentCourse);
    },
    getCurrentTerm(currentTerm) {
      this.currentTerm = currentTerm;
      this.courses = [];
      this.tags = [];
      this.loadCourses(this.currentTerm);
    },
    loadTerms() {
      setTimeout(() => {
        this.$store.state.courseInfoPerTerm.forEach((element) => {
          this.terms.push(element.term);
        });
      }, 0);
    },
    loadCourses(currentTerm) {
      setTimeout(() => {
        this.$store.state.courseInfoPerTerm.forEach((element) => {
          if (element.term === currentTerm) {
            element.courses.forEach((course) => {
              this.courses.push(course.name);
            });
          }
        });
      }, 0);
    },
    loadTags(currentCourse) {
      setTimeout(() => {
        this.$store.state.courseInfoPerTerm.forEach((courses) => {
          courses.courses.forEach((course) => {
            if (course.name === currentCourse) {
              course.tags.forEach((tag) => {
                this.tags.push(tag);
              });
            }
          });
        });
      }, 0);
    },
  },
};
</script>
