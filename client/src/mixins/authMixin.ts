
export default {
    mixins: [],
    mounted(){
        this.loadTokenFromLocalStorage();
    },
    methods: {
        loadTokenFromLocalStorage(){
            const token = window.localStorage.getItem("token");
            this.$store.commit ("setToken", token);
        },
        async login(userInfo : {email: string, password: string}){
            const res = await fetch(`${this.$store.state.baseUrl}/users/login`, {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify({
                  email : userInfo.email,
                  password : userInfo.password
                }),
              });
        
              const data = await res.json();
              window.localStorage.setItem("token", data.token);
              this.$store.commit ("setToken", data.token);
              this.$store.commit ("setCurrentUser", data.user);
              return data;
        },
        async signup(userInfo : { email: string, password: string, name: string, universityId: number, department: string }){
            const res = await fetch(`${this.$store.state.baseUrl}/users/signup`, {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                email : userInfo.email,
                password : userInfo.password,
                name : userInfo.name,
                universityId : userInfo.universityId,
                department: userInfo.department
              }),
            });
            const data = await res.json();
            window.localStorage.setItem("token", data.token);
            this.$store.commit ("setToken", data.token);
            this.$store.commit ("setCurrentUser", data.user);
            return data;
        },
        async editCurrentUser(userInfo : { email ?: string, password ?: string, name ?: string, universityId ?: number, department ?: string, bio ?: string, rank ?: string, points ?: number, picture ?: string }){
            const res = await fetch(`${this.$store.state.baseUrl}/users/edit`, {
              method: "PUT",
              headers: {
                "Content-Type": "application/json",
                "Authorization" : `Bearer ${this.$store.state.token}`
              },
              body: JSON.stringify({
                email : userInfo?.email,
                password : userInfo?.password,
                name : userInfo?.name,
                universityId : userInfo?.universityId,
                department : userInfo?.department,
                bio : userInfo?.bio,
                rank : userInfo?.rank,
                points : userInfo?.points,
                picture : userInfo?.picture
              }),
            });
            const data = await res.json();
            console.log(data);
        },
        async getCurrentUser(){
            const res = await fetch(`${this.$store.state.baseUrl}/users/currentUser`, {
                method: "GET",
                headers: {
                  "Content-Type": "application/json",
                  "Authorization" : `Bearer ${this.$store.state.token}`
                },
              });
        
              const data = await res.json();
              return data;
        },
        logout(){
            window.localStorage.removeItem('token');
        },
        isLoggedIn () : boolean{
            return !!this.$store.state.token;
        },
    
    }
  }
  