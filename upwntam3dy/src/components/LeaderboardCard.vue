<template>
  <div class="bg-gray-50 mt-10 rounded-xl overflow-hidden">
    <!-- First Name -->
    <div class="flex px-4 pt-4">
      <div class="flex flex-col items-center justify-center mx-2">
        <div class="opacity-60">Points</div>
        <div>523</div>
      </div>
      <div class="flex flex-col items-center mx-2">
        <img :src="smallVersion" alt="Winner" class="w-14 rounded-full" />
        <div class="font-semibold text-xl mt-2">Abdelrahman</div>
      </div>
      <div class="flex flex-col items-center mx-2 justify-center">
        <div class="opacity-60">Rank</div>
        <div>1</div>
      </div>
    </div>

    <!-- Rest of names -->
    <div>
      <div class="flex my-4">
        <div class="mx-4 text-lg">2</div>
        <div class="mr-4">
          <img :src="smallVersion" alt="Winner" class="w-6 rounded-full" />
        </div>
        <div>Habiba</div>
      </div>

      <hr />
      <div class="flex my-4">
        <div class="mx-4 text-lg">2</div>
        <div class="mr-4">
          <img :src="smallVersion" alt="Winner" class="w-6 rounded-full" />
        </div>
        <div>Habiba</div>
      </div>
    </div>
  </div>
</template>

<script>
import smallVersion from "../_utils/images/small-version.jpg";

export default {
  data() {
    return {
      smallVersion,
    };
  },
};
</script>
