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
            <div :class="$store.state.mobileResponsive ? 'flex-col' : ''" class="flex items-center">
                <div :class="$store.state.mobileResponsive ? 'order-3' : 'w-1/4 ml-20'" class="items-center">
                    <the-button 
                        v-if="String(this.$route.params.user_id) === String(currentUserId.currentUserId)"
                        @click="toggleSavedAnswers = !toggleSavedAnswers"
                        content="Saved Questions"
                        type="primary"
                        size="large"
                        :disabled="disableBtn"
                        :key="disableBtn"
                    />
                </div>
                <div :class="$store.state.mobileResponsive ? 'w-full' : 'w-2/4'" class="flex flex-col items-center py-8">
                    <div class="w-48 h-48 rounded-full overflow-hidden shadow-lg flex justify-center items-center">
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
                    :class="$store.state.mobileResponsive ? 'order-2 mb-2': 'mr-20 w-1/4'" class="flex justify-center items-center"
                    @click="editBio"
                >
                    <the-button 
                        v-if="String(this.$route.params.user_id) === String(currentUserId.currentUserId)"
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

        <!-- Answers -->
        <div class="ml-4" v-if="toggleSavedAnswers">
          <!-- <div v-for="answer in answers" :key='answer'>
            <answer-card :answer="answer" @syncAnswersLikeState="syncAnswersLikeState" />
            <hr class="mx-2" />
          </div> -->

            <div class="flex flex-col mt-4">
                <question-card
                    v-for="(question) in renderedQuestions"
                    :key="question"
                    :question="question"
                />
            </div>

            <pagination-buttons 
                class="mb-10"
                :list="questions"
                @paginatedList="syncCurrentList"
            />
        </div>

    </div>
</template>

<script lang="ts">
import TheButton from '@/components/TheButton.vue'
import ThePopup from '@/components/ThePopup.vue'
import profileInfo from '@/mixins/profileInfo'
import authMixin from '@/mixins/authMixin'
import getFromIdMixin from '@/mixins/getFromIdMixin'
// import AnswerCard from "@/components/AnswerCard.vue";
import QuestionCard from "@/components/QuestionCard.vue";
import PaginationButtons from '@/components/PaginationButtons.vue';

export default({
    mixins: [authMixin, getFromIdMixin],
    components: {
        TheButton,
        ThePopup,
        // AnswerCard,
        QuestionCard,
        PaginationButtons
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
            currentUserId: "",
            toggleSavedAnswers: false,
            questions : [],
            renderedQuestions: [],
        }
    },
    async mounted(){
        await this.initializeValues();
        this.prepareSavedQuestions();
    },
    methods: {
        syncCurrentList(questions){
            this.renderedQuestions = questions;
        },
        async onFileChanged(e){
            const FR = new FileReader();
            FR.addEventListener("load", async (ev) => {
                await this.editCurrentUser({ picture: ev.target.result })
                this.userImg = ev.target.result;
            }); 
            
            FR.readAsDataURL( e.target.files[0] );

        },
        async prepareSavedQuestions(){            
            const bookmarkedQuestionIds = (await this.getUserFromUniversityId(this.currentUserId.currentUserId)).bookmarkedQuestionIds;
            this.$store.state.questions.forEach(question => {
                if (bookmarkedQuestionIds.includes(question.id)) {
                    this.questions.push(question)
                }
            })
            console.log("currentUser", this.questions);
        },
        async initializeValues(){
            this.currentUserId = await this.getCurrentUser();
            let profile;
            if (String(this.$route.params.user_id) === String(this.currentUserId.currentUserId)) {
                // Profile of current user
                profile =  await this.getUserFromUniversityId(this.currentUserId.currentUserId);
            } else {
                profile =  await this.getUserFromUniversityId(this.$route.params.user_id);
            }
            this.username = profile.name;
            this.userImg = profile.picture;
            this.bioText = profile.bio;
            this.rank = profile.rank;
            this.pointsCount = profile.points;
            this.answersCount = profile.answerIds.length;
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
