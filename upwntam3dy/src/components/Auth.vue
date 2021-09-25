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
            >

            <input 
                class="w-96 p-4 rounded-xl shadow outline-none mb-4"
                type="email"
                placeholder="Email Address"
            >

            <input 
                class="w-96 p-4 rounded-xl shadow outline-none mb-4"
                type="password"
                placeholder="Password"
            >

            <input 
                v-if="authMode === 'signup'"
                class="w-96 p-4 rounded-xl shadow outline-none mb-4"
                type="text"
                placeholder="University ID"
            >

            <the-button 
                :content="submitBtnContent"
                type="secondary"
                size="large"
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
            alternativeOperation: "Sign Up"
        }
    },
    methods: {
        switchToSignup(){
            this.authMode = "signup";
            this.authHeader = "Create An Account";
            this.headerText = "Already Have An Account?";
            this.submitBtnContent = "Sign Up";
        },
        switchToSignin(){
            this.authMode = "signin";
            this.authHeader = "Sign In";
            this.headerText = "Didn’t have an account?";
            this.submitBtnContent = "Sign In";  
        },
    }
})
</script>

<style scoped lang="scss">

</style>
