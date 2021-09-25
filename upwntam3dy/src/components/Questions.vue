<template>
  <div class="flex flex-col">
    <!-- Filter By Date Buttons -->
    <div class="flex justify-end">
      <the-button
        @click="handleActiveBtns(0)"
        :disabled="btnStates[0]"
        class="mr-4"
        content="Month"
        :key="change"
        type="ternary"
        size="small"
      />
      <the-button
        @click="handleActiveBtns(1)"
        :disabled="btnStates[1]"
        class="mr-4"
        :key="change"
        content="Week"
        type="ternary"
        size="small"
      />
      <the-button
        @click="handleActiveBtns(2)"
        class="mr-4"
        :disabled="btnStates[2]"
        :key="change"
        content="Day"
        type="ternary"
        size="small"
      />
    </div>
    <!-- Question cards -->
    <div class="flex flex-col mt-4">
      <question-card
        v-for="question in this.$store.state.questions"
        :key="question"
        :question="question"
      />
    </div>

    <pagination-buttons 
      :maxRange="10"
    />

  </div>
</template>

<script>
import TheButton from "@/components/TheButton.vue";
import QuestionCard from "@/components/QuestionCard.vue";
import PaginationButtons from '@/components/PaginationButtons.vue';


export default {
  components: {
    TheButton,
    QuestionCard,
    PaginationButtons,
  },
  data() {
    return {
      activeBtn: "Day",
      btnStates: [true, true, false],
      change: 0
    };
  },
  mounted () {
    //
  },
  methods: {
    handleFilter(type) {
      this.activeBtn = type;
    },
    handleActiveBtns(val) {
      this.btnStates.forEach((btnState, index) => {
        this.btnStates[val] = false;
        index !== val && (this.btnStates[index] = true);
      })
      this.change = Math.random();
    },
  },
};
</script>

