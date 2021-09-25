<template>
    <div class="bg-yellow-200 m-8 rounded-xl shadow-lg p-6 flex flex-col">
        <div class="flex items-center">
            <div class="w-1/4 ml-20 flex justify-center items-center">
                <the-button 
                    content="Saved Answers"
                    type="primary"
                    size="large"
                />
            </div>
            <div class=" w-2/4 flex flex-col items-center py-8">
                <div class="w-48 h-48 rounded-full overflow-hidden shadow-lg flex justify-center items-center">
                    <img 
                        class="w-48 h-48"
                        src="https://www.imgonline.com.ua/examples/bee-on-daisy.jpg" 
                        alt="profile pic"
                    >
                </div>
                <div class="mt-4 text-2xl font-bold">
                    Abdelrahman Deghedy
                </div>
                <div class="mt-2 w-96 text-center">
                    I'm Abdelrahman. I aspire to make the world a better place. I like engaging with others and learning from them.
                </div>
            </div>
            <div class="mr-20 w-1/4 flex justify-center items-center">
                <the-button 
                    content="Edit Bio"
                    type="primary"
                    size="large"
                />
            </div>
        </div>
        <div class="flex justify-center text-xl py-4">
            <div class="flex flex-col items-center mr-10">
                <div class="opacity-50">Answers</div>
                <div>20</div>
            </div>
            <div class="flex flex-col items-center mx-10">
                <div class="opacity-50">Points</div>
                <div>50</div>
            </div>
            <div class="flex flex-col items-center ml-10">
                <div class="opacity-50">Rank</div>
                <div>2</div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import TheButton from '@/components/TheButton.vue'

export default({
    components: {
        TheButton,
    },
    data() {
        return {
            //
        }
    },
})
</script>

<style scoped lang="scss">

</style>
