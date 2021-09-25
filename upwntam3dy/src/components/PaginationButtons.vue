<template>
    <div class="pagination-color-primary h-14 w-96 mx-auto shadow-lg rounded-md mt-2 flex items-center justify-around p-4 text-xl">
      <div class="font-bold cursor-pointer select-none" @click="decrementActivePagBtns"> &#60; </div>
      <div class="flex items-center">
        <div
            class="px-6 cursor-pointer select-none"
            ref="firstPagVal"
            @click="handleActiveBtns('firstPagVal', firstPagVal)"
        > 
            {{ firstPagVal }}
        </div>
        <div 
            class="px-6 cursor-pointer select-none"
            v-if="buttonsActiveRange.length > 1"
            ref="secondPagVal"
            @click="handleActiveBtns('secondPagVal', secondPagVal)"
        > 
            {{ secondPagVal }} 
        </div>
        <div 
            class="px-6 cursor-pointer select-none"
            v-if="buttonsActiveRange.length > 2" 
            ref="thirdPagVal"
            @click="handleActiveBtns('thirdPagVal', thirdPagVal)"
        > 
            {{ thirdPagVal }} 
        </div>
      </div>
      <div class="font-bold cursor-pointer select-none" @click="incrementActivePagBtns"> &#62; </div>
    </div>
</template>

<script>

export default ({
    props :{
        list : {
            type: Array,
            required: true,
            default: () => []
        },
    },
    data() {
        return {
            selectedClass : ['pagination-color-secondary', 'h-16', 'shadow-lg', 'rounded-md', 'flex', 'items-center', 'transition', 'duration-300'],
            buttonValues : [],
            buttonsActiveRange: [],
            firstPagVal: 1,
            secondPagVal: 2,
            thirdPagVal: 3,
            localList: [],
            partitionSize: 5,
            numberOfPagButtons: 0,
            currentPaginatedList: 0,
        }
    },
    watch :{
        // To take care of any filtering happening
        list :{
            handler(){
                this.initializeNumberOfPaginationButtons();
                this.initializeButtonValues();
                this.partitionList();
                this.initializeInitialPaginatedList();
            }
        }
    },
    async mounted(){
        await setTimeout(() => {
            this.$store.state.pageMode !== "Questions" || (this.initializeButtonValues());
        }, 0)
        this.initializeNumberOfPaginationButtons();
        this.partitionList();
        this.initializeInitialPaginatedList();
    },
    methods : {
        initializeInitialPaginatedList(){
            this.$emit("paginatedList", this.localList[0]);
        },
        initializeNumberOfPaginationButtons(){
            this.numberOfPagButtons = +Math.ceil(this.list.length / this.partitionSize);
        },
        partitionList(){
            this.localList = [];
            let partition = [];
            if (this.list.length <= this.partitionSize) {
                partition = this.list;
                this.localList.push(partition);
                return;
            }
            
            let partitionStart = 0;
            for (let j = 0; j < this.numberOfPagButtons; j++) {
                partitionStart = j * this.partitionSize;
                for (let i = partitionStart; i < partitionStart + this.partitionSize && i < this.list.length; i++) {
                    partition.push(this.list[i]);
                }
                this.localList.push(partition);
                partition = [];
            }
            
            console.log("behold", this.localList);
        },
        decrementActivePagBtns(){
            if (this.buttonValues.includes(this.buttonsActiveRange[0] - 1)) {
                this.buttonsActiveRange = this.buttonsActiveRange.map(el => el - 1);
                [this.firstPagVal, this.secondPagVal, this.thirdPagVal] = this.buttonsActiveRange;
                this.currentPaginatedList--;
                this.$emit("paginatedList", this.localList[this.currentPaginatedList - 1])
            }            
        },
        incrementActivePagBtns(){
            if (this.buttonValues.includes(this.buttonsActiveRange[2] + 1)) {
                this.buttonsActiveRange = this.buttonsActiveRange.map(el => el + 1);
                [this.firstPagVal, this.secondPagVal, this.thirdPagVal] = this.buttonsActiveRange;
                this.currentPaginatedList++;
                this.$emit("paginatedList", this.localList[this.currentPaginatedList - 1])
            }
        },
        handleActiveBtns(value, content){
            if (value.includes("first")) {
                this.$refs.firstPagVal.classList.add(...this.selectedClass);
                this.secondPagVal && (this.$refs.secondPagVal.classList.remove(...this.selectedClass));
                this.thirdPagVal &&(this.$refs.thirdPagVal.classList.remove(...this.selectedClass));
            }
            else if (value.includes("second")) {
                this.$refs.secondPagVal.classList.add(...this.selectedClass);
                this.$refs.firstPagVal.classList.remove(...this.selectedClass);
                this.thirdPagVal && (this.$refs.thirdPagVal.classList.remove(...this.selectedClass));
            }
            else if (value.includes("third")) {
                this.$refs.thirdPagVal.classList.add(...this.selectedClass);
                this.$refs.firstPagVal.classList.remove(...this.selectedClass);
                this.$refs.secondPagVal.classList.remove(...this.selectedClass);
            }
            this.currentPaginatedList = content;
            this.$emit("paginatedList", this.localList[this.currentPaginatedList - 1])
        },
        initializeButtonValues () {
            this.buttonValues = [];
            for (let i = 1; i <= this.numberOfPagButtons; i++) {
                this.buttonValues.push(i);
            }
            
            this.buttonsActiveRange = [];

            for (let i = 0; i < Math.min(3, this.buttonValues.length); i++) {
                this.buttonsActiveRange.push(this.buttonValues[i]);
            }
            
            [this.firstPagVal, this.secondPagVal, this.thirdPagVal] = this.buttonsActiveRange;
            this.$refs.firstPagVal.classList.add(...this.selectedClass);
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