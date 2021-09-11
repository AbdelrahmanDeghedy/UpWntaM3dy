<template>
  <div class="shadow-md bg-white flex rounded-xl overflow-hidden m-2">
    <div class="py-6 w-1/6 flex flex-col justify-center items-center">
      <div>{{ answersNumber }}</div>
      <div class="opacity-60">Answers</div>
    </div>
    <div class="py-6 w-4/6">
      <div class="text-2xl font-semibold cursor-pointer">
        <!-- What's the square root of 9? -->
        {{ text }}
      </div>
      <div class="flex ml-2 my-2">
        <div class="text-blue-800 font-bold">{{ owner }}</div>
        <div class="opacity-80 ml-2">{{ dateToDays(time) }} days ago</div>
      </div>
      <div class="ml-4">
        <div class="flex">
          <div class="cursor-pointer">
            <font-awesome-icon icon="thumbs-up" :style="{ color: 'gray' }" />
          </div>
          <div class="ml-2">{{ likes }} Likes</div>
        </div>
      </div>
    </div>
    <div class="py-6 w-1/6 flex flex-col items-center">
      <the-button content="Answer" type="secondary" size="small" />
      <div
        class="mt-2 bg-gray-500 w-8 h-8 flex items-center justify-center rounded-full shadow-md cursor-pointer"
      >
        <font-awesome-icon icon="bookmark" :style="{ color: 'white' }" />
      </div>
    </div>
  </div>
</template>

<script>
import TheButton from "./TheButton.vue";
import { getDayDifference } from "@/_utils/helper";

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
      default: new Date(2021, 3, 5),
    },
    likes: {
      type: Number,
      required: true,
      default: 0,
    },
  },
  components: {
    TheButton,
  },
  methods: {
    dateToDays(date) {
      return getDayDifference(Date.now(), date);
    },
  },
  data() {
    return {
      //
    };
  },
};
</script>
