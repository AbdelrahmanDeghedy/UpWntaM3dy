<template>
    <div class="bg-yellow-200 m-8 rounded-xl shadow-lg p-6 flex flex-col items-center relative">
        <div class="text-2xl font-semibold">{{ authHeader }}</div>
        <div class="mt-2">
            {{ headerText }}
            <span class="text-blue-700 cursor-pointer" @click="authMode === 'signin' ? switchToSignup() : switchToSignin()">
                {{ alternativeOperation }}
            </span>
        </div>
        <div class="signup-form flex flex-col items-center mt-4">
            <input 
                v-if="authMode === 'signup'"
                class="w-96 p-4 rounded-xl shadow outline-none mb-4"
                type="text"
                placeholder="Full Name"
                v-model="name"
            >

            <input 
                class="w-96 p-4 rounded-xl shadow outline-none mb-4"
                type="email"
                placeholder="Email Address"
                v-model="email"
            >

            <input 
                class="w-96 p-4 rounded-xl shadow outline-none mb-4"
                type="password"
                placeholder="Password"
                v-model="password"
            >

            <input 
                v-if="authMode === 'signup'"
                class="w-96 p-4 rounded-xl shadow outline-none mb-4"
                type="text"
                placeholder="University ID"
                v-model="uniId"
            >

            <the-button 
                :content="submitBtnContent"
                type="secondary"
                size="large"
                @click="authMode === 'signin' ? signin() : signup()"
            />
        </div>
    </div>
</template>

<script lang="ts">
import TheButton from '@/components/TheButton.vue';

export default({
    components: {
        TheButton
    },
    data() {
        return {
            authMode: "signin", // or "signup"
            submitBtnContent: "Sign In",
            authHeader: "Sign In",
            headerText: "Didn’t have an account?",
            alternativeOperation: "Sign Up",
            name: "",
            email: "",
            password: "",
            uniId: ""
        }
    },
    methods: {
        switchToSignup(){
            this.$router.push({ name: "Signup" });
            this.authMode = "signup";
            this.authHeader = "Create An Account";
            this.headerText = "Already Have An Account?";
            this.submitBtnContent = "Sign Up";
        },
        switchToSignin(){
            this.$router.push({ name: "Signin" });
            this.authMode = "signin";
            this.authHeader = "Sign In";
            this.headerText = "Didn’t have an account?";
            this.submitBtnContent = "Sign In";  
        },
        signin(){
            console.log("sign in!!!!");
            this.$store.state.users.forEach((user) => {
                if (user.email === this.email && user.password === this.password) {
                    console.log("signed in>>>");
                    this.$router.push({ name: "Questions", params: { 'user_id': user.universityId } });
                }
            })
        },
        signup(){
            console.log("sign up!!!!");
            this.$store.commit ("createUser", {
                email: this.email,
                password: this.password,
                universityId: this.uniId,
                name: this.name,
                points: 0,
                rank: null,
                bio: "404, Not found!",
                picture: "",
                answers: {
                    answerIds: [],
                },
                bookmarks: {
                    questionIds: [],
                },
            });
        },
    }
})
</script>

<style scoped lang="scss">

</style>
