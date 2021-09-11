<template>
  <div class="shadow-md bg-white flex rounded-xl overflow-hidden m-2">
    <div class="py-6 w-1/6 flex flex-col">
      <div class="flex flex-col items-center my-2">
        <div>{{ answersNumber }} 10</div>
        <div class="opacity-60">Answers</div>
      </div>

      <!-- Likes -->
      <div class="flex flex-col items-center my-2">
        <div class="cursor-pointer">
          <font-awesome-icon icon="thumbs-up" :style="{ color: 'gray' }" />
        </div>
        <div>{{ likes }}0 Likes</div>
      </div>

      <!-- Bookmark -->
      <div class="flex flex-col items-center my-2">
        <div
          class="mt-2 bg-gray-500 w-8 h-8 flex items-center justify-center rounded-full shadow-md cursor-pointer"
        >
          <font-awesome-icon icon="bookmark" :style="{ color: 'white' }" />
        </div>
      </div>
    </div>

    <div class="flex flex-col w-5/6">
      <div class="flex justify-between">
        <div class="py-6 w-4/6 ml-4">
          <div class="text-2xl font-semibold cursor-pointer">
            What's the square root of 9?
            {{ text }}
          </div>
          <div class="flex ml-2 my-2">
            <div class="text-blue-800 font-bold">
              {{ owner }}Abdelrahman Deghedy
            </div>
            <div class="opacity-80 ml-2">{{ time }}2 days ago</div>
          </div>
        </div>

        <div class="flex items-center mr-8">
          <the-button content="Edit" type="secondary" size="small" />
        </div>
      </div>

      <hr class="mx-4 -mt-4" />
      <div class="mt-4">
        <div class="ml-4 mb-4">
          Full Question CONTENT
        </div>

        <div class="font-bold text-xl mb-2 ml-4">
          2 Answers
        </div>

        <hr class="mx-2" />

        <!-- Answers -->
        <div class="ml-4">
          <answer-card />
          <hr class="mx-2" />

          <answer-card />
          <hr class="mx-2" />

          <answer-card />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AnswerCard from "@/components/AnswerCard";
import TheButton from "@/components/TheButton";

export default {
  components: {
    AnswerCard,
    TheButton,
  },
  data() {
    return {
      //
    };
  },
};
</script>
