<template>
  <button
    ref="btn"
    :class="
      `flex outline-none items-center justify-center UpWntaM3dyButton__btn-${type} UpWntaM3dyButton__${size}-size opacity-80 hover:opacity-100 transition-all`
    "
  >
    {{ content }}
  </button>
</template>

<script lang="ts">
const buttonsTypes = ["primary", "secondary", "ternary"];
const buttonsSizes = ["large", "small"];

export default {
  props: {
    disabled : {
      type: Boolean,
      required: false,
      default : false
    },
    content: {
      type: String,
      required: true,
      default: "",
    },
    type: {
      type: String,
      required: true,
      default: "primary",
      validator: (value: string) => {
        return buttonsTypes.indexOf(value) !== -1;
      },
    },
    size: {
      type: String,
      required: true,
      default: "large",
      validator: (value: string) => {
        return buttonsSizes.indexOf(value) !== -1;
      },
    },
  },
  data() {
    return {
      //
    };
  },
  mounted(){
    this.disabled && (this.disabledEffect());
  },
  methods: {
    disabledEffect(){
      this.$refs.btn.classList.remove("opacity-80", "hover:opacity-100");
      this.$refs.btn.classList.add(`opacity-50`);
    },
  }
};
</script>

<style scoped>
.UpWntaM3dyButton__btn-primary {
  background: #ffffff;
  border: 3px solid #535353;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5rem;
  padding: 1rem;
}

.UpWntaM3dyButton__btn-secondary {
  background: #535353;
  border: 3px solid #ffffff;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5rem;
  padding: 1rem;
  color: #fff;
}

.UpWntaM3dyButton__btn-ternary {
  background: #797777;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 1rem;
  padding: 1rem;
  color: #fff;
}

.UpWntaM3dyButton__large-size {
  width: 10rem;
}

.UpWntaM3dyButton__small-size {
  width: 6rem;
  height: 3rem;
}
</style>
