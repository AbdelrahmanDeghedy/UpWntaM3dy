<template>
  <div class="shadow-md bg-white flex rounded-xl overflow-hidden m-2">
    <div class="py-6 w-1/6 flex flex-col justify-center items-center">
      <div>0</div>
      <div>Answers</div>
    </div>
    <div class="py-6 w-4/6">
      <div class="text-2xl font-semibold">
        What's the square root of 9?
      </div>
      <div class="flex ml-2 my-2">
        <div class="text-blue-800">Abdelrahman Deghedy</div>
        <div class="opacity-80 ml-2">1 Hour ago</div>
      </div>
      <div class="ml-4">2 Likes</div>
    </div>
    <div class="py-6 w-1/6">
      <the-button content="Answer" type="ternary" size="small" />
      <the-button class="mt-4" content="Bookmark" type="ternary" size="small" />
    </div>
  </div>
</template>

<script>
import TheButton from "./TheButton.vue";

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
