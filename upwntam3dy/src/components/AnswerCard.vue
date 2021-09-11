<template>
  <div class="bg-white flex rounded-xl overflow-hidden">
    <div class="py-6 w-4/6">
      <div class="flex ml-2 my-2">
        <div class="text-blue-800 font-bold">{{ owner }}</div>
        <div class="opacity-80 ml-2">{{ time }}ago</div>
      </div>
      <div class="ml-4">Answer TEXT</div>
    </div>
    <div class="py-6 flex items-center">
      <div class="flex">
        <div class="cursor-pointer">
          <font-awesome-icon icon="thumbs-up" :style="{ color: 'gray' }" />
        </div>
        <div class="flex items-center justify-center ml-2">
          {{ likes }} Likes
        </div>
      </div>
      <div
        class="ml-4 mt-2 bg-gray-500 w-8 h-8 flex  items-center justify-center rounded-full shadow-md cursor-pointer"
      >
        <font-awesome-icon icon="bookmark" :style="{ color: 'white' }" />
      </div>
    </div>
  </div>
</template>

<script>
// import TheButton from "./TheButton.vue";

export default {
  props: {
    answersNumber: {
      type: Number,
      required: true,
      default: 0,
    },
    text: {
      type: String,
      required: true,
      default: "NO QUESTION PROVIDED!!",
    },
    owner: {
      type: String,
      required: true,
      default: "NO OWNER PROVIDED!!",
    },
    time: {
      type: Date,
      required: true,
      default: Date.now(),
    },
    likes: {
      type: Number,
      required: true,
      default: 0,
    },
  },
  components: {
    // TheButton,
  },
  data() {
    return {
      //
    };
  },
};
</script>
