<template>
    <div class="bg-yellow-200 m-8 rounded-xl shadow-lg p-6 flex flex-col relative">
       <the-popup v-if="showPopup">
                <div class="w-full h-full flex flex-col justify-between p-4">
                    <div class="mt-2">
                        <input 
                            v-model="bioText"
                            placeholder="Enter a cool bio!"
                            type="text" 
                            class=" rounded-lg h-14 w-full p-2 px-4 outline-none border border-black focus:border-2 focus:border-blue-700 shadow-sm"
                        /> 
                    </div>
                            
                    <div class="flex items-center">
                        <the-button 
                            content="Save"
                            type="ternary"
                            size="small"
                            @click="saveChanges"
                        />
                        <div 
                            class="ml-4 text-black cursor-pointer text-lg"
                            @click="discardChanges"
                        >
                            Cancel
                        </div>
                    </div>
                </div>
        </the-popup>     
       
        
        <div ref="profileContainer" class="">
            <div class="flex items-center">
                <div class="w-1/4 ml-20 flex justify-center items-center">
                    <the-button 
                        content="Saved Answers"
                        type="primary"
                        size="large"
                        :disabled="disableBtn"
                        :key="disableBtn"
                    />
                </div>
                <div class=" w-2/4 flex flex-col items-center py-8">
                    <div  class="w-48 h-48 rounded-full overflow-hidden shadow-lg flex justify-center items-center">
                        <input type="file" @change="onFileChanged" class="z-50 bg-gray-200 w-48 absolute h-32 rounded-full opacity-0 cursor-pointer">
                        <img 
                            class="w-48 h-48 relative"
                            :src="userImg || $store.state?.alternativeImg"
                            alt="profile pic"
                        >
                    </div>
                    <div class="mt-4 text-2xl font-bold">
                        {{ username }}
                    </div>
                    <div class="mt-2 w-96 text-center">
                        {{ bioText }}
                    </div>
                </div>
                <div 
                    class="mr-20 w-1/4 flex justify-center items-center"
                    @click="editBio"
                >
                    <the-button 
                        content="Edit Bio"
                        type="primary"
                        size="large"
                        :disabled="disableBtn"
                        :key="disableBtn"
                    />
                </div>
            </div>
            <div class="flex justify-center text-xl py-4">
                <div class="flex flex-col items-center mr-10">
                    <div class="opacity-50">Answers</div>
                    <div>{{ answersCount }}</div>
                </div>
                <div class="flex flex-col items-center mx-10">
                    <div class="opacity-50">Points</div>
                    <div>{{ pointsCount }}</div>
                </div>
                <div class="flex flex-col items-center ml-10">
                    <div class="opacity-50">Rank</div>
                    <div>{{ rank }}</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import TheButton from '@/components/TheButton.vue'
import ThePopup from '@/components/ThePopup.vue'
import profileInfo from '@/mixins/profileInfo'
import authMixin from '@/mixins/authMixin'
import getFromIdMixin from '@/mixins/getFromIdMixin'

export default({
    mixins: [authMixin, getFromIdMixin],
    components: {
        TheButton,
        ThePopup
    },
    data() {
        return {
            showPopup: false,
            disableBtn: false,
            bioText: "",
            username: "",
            answersCount: 0,
            pointsCount: 0,
            rank: -1,
            userImg: "",

        }
    },
    async mounted(){
        const currentUser = await this.currentUser();
        console.log(currentUser);
        this.initializeValues();
        // console.log(this.$store.state.alternativeImg);
    },
    methods: {
        async onFileChanged(e){
            const uploadedImg = URL.createObjectURL(e.target.files[0]);
            this.userImg = uploadedImg;
            await this.editCurrentUser({ picture: uploadedImg })
        },
        async initializeValues(){
            const currentUser = await this.currentUser();

            this.username = currentUser.name;
            this.userImg = currentUser.picture;
            this.bioText = currentUser.bio;
            this.rank = currentUser.rank;
            this.pointsCount = currentUser.points;
            this.answersCount = currentUser.questionIds.length;
        },
        editBio(){
            this.currentBio = this.bioText;
            this.enablePopup();
        },
        async saveChanges(){
            this.getCurrentUser().bio = this.bioText;
            await this.editCurrentUser({ bio: this.bioText })
            this.disablePopup();
        },
        disablePopup(){
            this.showPopup = false;
            this.$refs.profileContainer.classList.remove("blur-sm", "filter")
            this.disableBtn = false;            
        },
        enablePopup(){
            this.showPopup = true;
            this.$refs.profileContainer.classList.add("blur-sm", "filter")
            this.disableBtn = true;
        },
        async discardChanges(){
            this.bioText = (await this.currentUser()).bio;
            this.disablePopup();
        },
    }
})
</script>

<style scoped lang="scss">

</style>
