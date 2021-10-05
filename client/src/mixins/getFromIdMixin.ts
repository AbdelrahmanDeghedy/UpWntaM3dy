export default {
  methods: {
    getUserFromUniversityId(uid){
      if (!uid) return null;
      return this.$store.state.users.filter(user => {
        return String(user.universityId) === String(uid)
      })[0];
    },
    getUsernameFromUniversityId(uid){
      if (!uid) return "";
      console.log("uid", uid);
        return this.$store.state.users.filter(user => {
          return String(user.universityId) === String(uid)
        })[0]?.name;
      },
      getUsernameFromId(id){
        return this.$store.state.users.filter(user => {
          return String(user.id) === String(id)
        })[0]?.name;
      },
    // getAnswersOfQuestion(qId) {
    // if (!qId) return "";
    // const answers = [];
    // this.$store.state.answers.forEach((answer) => {
    //     if (String(answer.questionOfAnswerId) === String(qId)) {
    //     answers.push(answer);
    //     }
    // });
    // return answers;
    // },
    findQuestionById (qId) {
    if (!qId) return "";
    return this.$store.state.questions.filter((question) => {
        if (String(question.id) === String(qId)) {
        return question;
        }
    })[0]
    }
  }
}
