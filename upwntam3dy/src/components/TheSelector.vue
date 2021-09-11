<template>
  <div class="my-6 flex flex-col">
    <label :for="label" class="mb-2 font-bold">{{ label }}</label>
    <select
      v-model="defaultVal"
      :name="label"
      :id="label"
      class="cursor-pointer w-60 rounded-lg p-2 outline-none bg-gray-200"
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
      required: true,
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
      defaultVal: this.defaultChoice,
    };
  },
};
</script>
