<template>
    <div class="pagination-color-primary h-14 w-96 mx-auto shadow-lg rounded-md mt-2 flex items-center justify-around p-4 text-xl">
      <div class="font-bold cursor-pointer" @click="decrementActivePagBtns"> &#60; </div>
      <div class="flex items-center">
        <div
            class="px-6 cursor-pointer"
            ref="firstPagVal"
            @click="handleActiveBtns('firstPagVal')"
        > 
            {{ firstPagVal }}
        </div>
        <div 
            class="px-6 cursor-pointer"
            v-if="buttonsActiveRange.length > 1"
            ref="secondPagVal"
            @click="handleActiveBtns('secondPagVal')"
        > 
            {{ secondPagVal }} 
        </div>
        <div 
            class="px-6 cursor-pointer"
            v-if="buttonsActiveRange.length > 2" 
            ref="thirdPagVal"
            @click="handleActiveBtns('thirdPagVal')"
        > 
            {{ thirdPagVal }} 
        </div>
      </div>
      <div class="font-bold cursor-pointer" @click="incrementActivePagBtns"> &#62; </div>
    </div>
</template>

<script>

export default ({
    props :{
        maxRange : {
            type: Number,
            required: true,
            default: 1
        }
    },
    data() {
        return {
            selectedClass : ['pagination-color-secondary', 'h-16', 'shadow-lg', 'rounded-md', 'flex', 'items-center', 'transition', 'duration-300'],
            buttonValues : [],
            buttonsActiveRange: [],
            firstPagVal: 1,
            secondPagVal: 2,
            thirdPagVal: 3,
        }
    },
    mounted(){
        this.initializeButtonValues();
    },
    methods : {
        decrementActivePagBtns(){
            if (this.buttonValues.includes(this.buttonsActiveRange[0] - 1)) {
                this.buttonsActiveRange = this.buttonsActiveRange.map(el => el - 1);
                [this.firstPagVal, this.secondPagVal, this.thirdPagVal] = this.buttonsActiveRange;
            }            
        },
        incrementActivePagBtns(){
            if (this.buttonValues.includes(this.buttonsActiveRange[2] + 1)) {
                this.buttonsActiveRange = this.buttonsActiveRange.map(el => el + 1);
                [this.firstPagVal, this.secondPagVal, this.thirdPagVal] = this.buttonsActiveRange;
            }
        },
        handleActiveBtns(value){
            if (value.includes("first")) {
                this.$refs.firstPagVal.classList.add(...this.selectedClass);
                this.$refs.secondPagVal.classList.remove(...this.selectedClass);
                this.$refs.thirdPagVal.classList.remove(...this.selectedClass);
            }
            else if (value.includes("second")) {
                this.$refs.secondPagVal.classList.add(...this.selectedClass);
                this.$refs.firstPagVal.classList.remove(...this.selectedClass);
                this.$refs.thirdPagVal.classList.remove(...this.selectedClass);

            }
            else if (value.includes("third")) {
                this.$refs.thirdPagVal.classList.add(...this.selectedClass);
                this.$refs.firstPagVal.classList.remove(...this.selectedClass);
                this.$refs.secondPagVal.classList.remove(...this.selectedClass);

            }
        },
        initializeButtonValues () {
            for (let i = 1; i <= this.maxRange; i++) {
                this.buttonValues.push(i);
            }
            
            this.buttonsActiveRange = [];

            for (let i = 0; i < Math.min(3, this.buttonValues.length); i++) {
                this.buttonsActiveRange.push(this.buttonValues[i]);
            }
            
            [this.firstPagVal, this.secondPagVal, this.thirdPagVal] = this.buttonsActiveRange;
            this.$refs.firstPagVal.classList.add(...this.selectedClass);
            
            console.log(this.buttonValues);
            console.log(this.buttonsActiveRange);
        }
    }

})
</script>

<style scoped>
.pagination-color-primary {
  background-color: #C6BDB8;
}

.pagination-color-secondary {
  background-color: #A79D98;
}
</style>