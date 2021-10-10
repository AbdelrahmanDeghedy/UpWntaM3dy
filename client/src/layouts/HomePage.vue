<template>
    <div class="home-container h-screen flex justify-center items-center">
        <div class="content-container w-1/3">
            <div class="flex justify-center items-center header-text">
                Make Student life great again!
            </div>
            <div class="mt-4 flex justify-center items-center secondary-text">Made by students, for students. We focus on student needs, and try to provide the best experience for them.</div>
            <div class="mt-4 flex justify-center items-center">
                <the-button 
                    content = "Get Started"
                    :size="$store.state.mobileResponsive === true ? 'small' : 'large'"
                    type="secondary"
                    @click="handleClick()"
                />
            </div>
        </div>
    </div>
</template>

<script>
import TheButton from '@/components/TheButton.vue'

export default({
    components: {
        TheButton,
    },
    data() {
        return {
            
            }
    },
    methods : {
        jwtDecode(t) {
            const payload = JSON.parse(window.atob(t.split('.')[1]));
            return payload
        },
        handleClick(){
        if (this.$store.state.token) {
            this.$store.commit("setPageMode", "questions");
            this.$router.push ({ name: "Questions", params: { user_id: this.jwtDecode(this.$store.state.token).sub } });
        } else {
            this.$store.commit("setPageMode", "auth");
            this.$router.push ({ name: "Signin" });
        }   

        },
    }
})
</script>

<style>

.home-container {
	background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
	background-size: 400% 400%;
	animation: gradient 15s ease infinite;
	height: 100vh;
}

@keyframes gradient {
	0% {
		background-position: 0% 50%;
	}
	50% {
		background-position: 100% 50%;
	}
	100% {
		background-position: 0% 50%;
	}
}



.header-text {
    font-family: Roboto;
    font-style: italic;
    font-weight: bold;
    font-size: 4rem;
    text-align: center;
    text-decoration-line: underline;
    text-transform: capitalize;
    color: #FFFFFF;
}

.secondary-text {
    font-family: Roboto;
    font-style: normal;
    font-weight: normal;
    font-size: 1.5rem;
    text-align: center;
    text-transform: capitalize;

    color: #FFFFFF;
}

@media screen and (max-width: 900px) {
  .header-text {
    font-size: 2rem;
  }

   .secondary-text {
    font-size: 1rem;
  }

  .content-container {
      width: 60%;
  }
}


</style>
