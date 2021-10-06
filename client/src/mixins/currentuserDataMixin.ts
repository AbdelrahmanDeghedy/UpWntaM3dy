
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
        async getAllQuestions(){
            const res = await fetch(`${this.$store.state.baseUrl}/questions/`, {
                method: "GET",
                headers: {
                  "Content-Type": "application/json",
                  "Authorization" : `Bearer ${this.$store.state.token}`
                },
              });
        
              const data = await res.json();
              return data;
        },
        async getAllQuestionsSortedByLikes(){
          const res = await fetch(`${this.$store.state.baseUrl}/questions/sortedByLikes`, {
              method: "GET",
              headers: {
                "Content-Type": "application/json",
                "Authorization" : `Bearer ${this.$store.state.token}`
              },
            });
      
            const data = await res.json();
            return data;
      },
      async getAllQuestionsSortedByAnswers(){
        const res = await fetch(`${this.$store.state.baseUrl}/questions/sortedByAnswersCount/`, {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              "Authorization" : `Bearer ${this.$store.state.token}`
            },
          });
    
          const data = await res.json();
          return data;
      },
        async createQuestion(questionBody: { title: string, body: string, department: string, commaSeparatedTags: string }){
            const res = await fetch(`${this.$store.state.baseUrl}/questions/create`, {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                  "Authorization" : `Bearer ${this.$store.state.token}`
                },
                body: JSON.stringify({
                    title : questionBody.title,
                    body : questionBody.body,
                    department: questionBody.department,
                    commaSeparatedTags: questionBody.commaSeparatedTags,
                  }),
              });
        
              const data = await res.json();
              return data;
              console.log(data);
        },
        async editQuestion(qid: string, questionBody: { title ?: string, body ?: string, department ?: string, commaSeparatedTags ?: string }){
            const res = await fetch(`${this.$store.state.baseUrl}/questions/${qid}/edit`, {
                method: "PUT",
                headers: {
                  "Content-Type": "application/json",
                  "Authorization" : `Bearer ${this.$store.state.token}`
                },
                body: JSON.stringify({
                    title : questionBody?.title,
                    body : questionBody?.body,
                    department: questionBody?.department,
                    commaSeparatedTags: questionBody?.commaSeparatedTags,
                  }),
              });
        
              const data = await res.json();
              console.log(data);
        },
        async deleteQuestion(qid: string){
            const res = await fetch(`${this.$store.state.baseUrl}/questions/${qid}/delete`, {
                method: "DELETE",
                headers: {
                  "Content-Type": "application/json",
                  "Authorization" : `Bearer ${this.$store.state.token}`
                },
              });
        
              const data = await res.json();
              console.log(data);
        },
        async likeQuestion(qid: string){
            const res = await fetch(`${this.$store.state.baseUrl}/questions/${qid}/like`, {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                  "Authorization" : `Bearer ${this.$store.state.token}`
                },
              });
        
              const data = await res.json();
              return data;
        },
        async dislikeQuestion(qid: string){
            const res = await fetch(`${this.$store.state.baseUrl}/questions/${qid}/dislike`, {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                  "Authorization" : `Bearer ${this.$store.state.token}`
                },
              });
        
              const data = await res.json();
              return data;
        },
        async bookmarkQuestion(qid: string){
            const res = await fetch(`${this.$store.state.baseUrl}/questions/${qid}/bookmark`, {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                  "Authorization" : `Bearer ${this.$store.state.token}`
                },
              });
        
              const data = await res.json();
              return data;
        },
        async removeBookmarkQuestion(qid: string){
            const res = await fetch(`${this.$store.state.baseUrl}/questions/${qid}/removeBookmark`, {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                  "Authorization" : `Bearer ${this.$store.state.token}`
                },
              });
        
              const data = await res.json();
              return data;
        },



        async getQuestionAnswers(qid: string){
          const res = await fetch(`${this.$store.state.baseUrl}/answers/${qid}/`, {
              method: "GET",
              headers: {
                "Content-Type": "application/json",
                "Authorization" : `Bearer ${this.$store.state.token}`
              },
            });
      
            const data = await res.json();
            return data;
      },
        async createQuestionAnswer(qid: string, questionBody: { body: string }){
          const res = await fetch(`${this.$store.state.baseUrl}/answers/${qid}/create`, {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
                "Authorization" : `Bearer ${this.$store.state.token}`
              },
              body: JSON.stringify({
                  body : questionBody.body,
                }),
            });
      
            const data = await res.json();
            console.log(data);
      },
      async editAnswer(aid: string, questionBody: { body ?: string }){
        const res = await fetch(`${this.$store.state.baseUrl}/answers/${aid}/edit`, {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
              "Authorization" : `Bearer ${this.$store.state.token}`
            },
            body: JSON.stringify({
                body : questionBody?.body,
              }),
          });
    
          const data = await res.json();
          console.log(data);
      },
      async deleteAnswer(aid: string){
        const res = await fetch(`${this.$store.state.baseUrl}/answers/${aid}/delete`, {
            method: "DELETE",
            headers: {
              "Content-Type": "application/json",
              "Authorization" : `Bearer ${this.$store.state.token}`
            },
          });
    
          const data = await res.json();
          console.log(data);
      },
      async likeAnswer(aid: string){
        const res = await fetch(`${this.$store.state.baseUrl}/answers/${aid}/like`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "Authorization" : `Bearer ${this.$store.state.token}`
            },
          });
    
          const data = await res.json();
          console.log(data);
    },
    async dislikeAnswer(aid: string){
        const res = await fetch(`${this.$store.state.baseUrl}/answers/${aid}/dislike`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "Authorization" : `Bearer ${this.$store.state.token}`
            },
          });
    
          const data = await res.json();
          console.log(data);
      },
      async bookmarkAnswer(aid: string){
        const res = await fetch(`${this.$store.state.baseUrl}/answers/${aid}/bookmark`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "Authorization" : `Bearer ${this.$store.state.token}`
            },
          });
    
          const data = await res.json();
          console.log(data);
    },
    async removeBookmarkAnswer(aid: string){
        const res = await fetch(`${this.$store.state.baseUrl}/answers/${aid}/removeBookmark`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "Authorization" : `Bearer ${this.$store.state.token}`
            },
          });
    
          const data = await res.json();
          console.log(data);
    },
    
    
    async getLeaderboard(){
      const res = await fetch(`${this.$store.state.baseUrl}/users/leaderboard`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            "Authorization" : `Bearer ${this.$store.state.token}`
          },
        });
  
        const data = await res.json();
        return data;
  },
    }
  }
  