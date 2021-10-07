<template>
  <div class="my-6 flex flex-col w-full">
    <label :for="label" class="mb-2 font-bold">{{ label }}</label>
    <select
      @change="currentValueChange()"
      v-model="currentValue"
      :name="label"
      :id="label"
      class="shadow cursor-pointer rounded-lg p-2 outline-none bg-gray-200"
    >
      <option :key="value" v-for="value in values" :value="value">{{
        value
      }}</option>
    </select>
  </div>
</template>

<script>
export default {
  props: {
    values: {
      type: Array[String],
      required: true,
      default: ["NO VALUES"],
    },
    defaultChoice: {
      type: String,
      required: false,
      default: "NO VALUES",
    },
    label: {
      type: String,
      required: true,
      default: "NO LABEL",
    },
  },
  data() {
    return {
      currentValue: this.defaultChoice,
    };
  },
  methods: {
    currentValueChange() {
      this.$emit("currentValueChange", this.currentValue);
    },
  },
};
</script>
