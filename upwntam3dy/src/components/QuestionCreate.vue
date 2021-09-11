<template>
  <div class="bg-white rounded-3xl p-6 flex flex-col shadow-md">
    <textarea
      type="text"
      class="outline-none text-2xl"
      placeholder="What's in Your Mind?"
    />
    <div class="flex justify-end">
      <the-button class="mt-4" content="Ask" size="large" type="secondary" />
    </div>
  </div>
</template>

<script>
import TheButton from "@/components/TheButton.vue";

export default {
  components: {
    TheButton,
  },
  data() {
    return {
      //
    };
  },
};
</script>
