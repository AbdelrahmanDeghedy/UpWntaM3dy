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
      <the-selector defaultChoice="1" label="Term" :values="['1', '2']" />
      <the-selector defaultChoice="1" label="Course" :values="['1', '2']" />
      <the-selector defaultChoice="1" label="Tag" :values="['1', '2']" />
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
      //
    };
  },
};
</script>
