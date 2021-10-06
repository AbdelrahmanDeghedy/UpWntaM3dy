<template>
    <div class="bg-yellow-200 m-8 rounded-xl shadow-lg p-6 flex flex-col items-center relative">
        <div class="text-2xl font-semibold">{{ authHeader }}</div>
        <div class="mt-2">
            {{ headerText }}
            <span class="text-blue-700 cursor-pointer" @click="authMode === 'signin' ? switchToSignup() : switchToSignin()">
                {{ alternativeOperation }}
            </span>
        </div>
        <form class="signup-form flex flex-col items-center mt-4">
            <input 
                v-if="authMode === 'signup'"
                class="w-96 p-4 rounded-xl shadow outline-none mb-4"
                type="text"
                placeholder="Full Name"
                v-model="name"
                required
            >

            <input 
                class="w-96 p-4 rounded-xl shadow outline-none mb-4"
                type="email"
                placeholder="Email Address"
                v-model="email"
                required
            >

            <input 
                class="w-96 p-4 rounded-xl shadow outline-none mb-4"
                type="password"
                placeholder="Password"
                v-model="password"
                required
            >

            <input 
                v-if="authMode === 'signup'"
                class="w-96 p-4 rounded-xl shadow outline-none mb-4"
                type="text"
                placeholder="University ID"
                v-model="uniId"
                required
            >

            <input 
                v-if="authMode === 'signup'"
                class="w-96 p-4 rounded-xl shadow outline-none mb-4"
                type="text"
                placeholder="Bio (optional)"
                v-model="bio"
            >

            <div>
                {{ authResponse }}
            </div>

            <the-button 
                :content="submitBtnContent"
                size="large"
                type="primary"
                @click.prevent="authMode === 'signin' ? signin() : createAccount()"
            />
        </form>
    </div>
</template>

<script lang="ts">
import TheButton from '@/components/TheButton.vue';
import authMixin from '@/mixins/authMixin';


export default({
    mixins: [authMixin],
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
            uniId: "",
            bio: "",
            authResponse: ""
        }
    },
    methods: {
        switchToSignup(){
            this.$router.push({ name: "Signup" });
            this.authMode = "signup";
            this.authHeader = "Create An Account";
            this.headerText = "Already Have An Account?";
            this.submitBtnContent = "Sign Up";
            this.alternativeOperation = "Sign in";
        },
        switchToSignin(){
            this.$router.push({ name: "Signin" });
            this.authMode = "signin";
            this.authHeader = "Sign In";
            this.headerText = "Didn’t have an account?";
            this.submitBtnContent = "Sign In";
            this.alternativeOperation = "Sign up";
        },
        async signin(){
            if (!this.email || !this.password)  return;
            const res = await this.login ({ email: this.email, password: this.password })
            console.log(res);
            if (res.msg === 'success') {
                this.$store.commit("setPageMode", "questions");
                this.$router.push({ name: "Questions", params: { 'user_id': res.user.universityId } });

            } else {
                this.authResponse = res.msg;
            }
        },
                
        async createAccount(){
            if (!this.email || !this.password || !this.name || !this.uniId)  return;
            const res = await this.signup ({ email: this.email, password: this.password, name: this.name, universityId: this.uniId, department: "Comm", bio: this.bio });
            console.log(res);
            if (res.msg === 'success') {
                this.$store.commit("setPageMode", "questions");
                this.$router.push({ name: "Questions", params: { 'user_id': res.user.universityId } });

            } else {
                this.authResponse = res.msg;
            }
            
        },
    }
})
</script>

<style scoped lang="scss">

</style>
