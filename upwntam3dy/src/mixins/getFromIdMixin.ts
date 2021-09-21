export default {
  methods: {
    getUsernameFromId(uid){
      if (!uid) return "";
        return this.$store.state.users.filter(user => {
          return user.universityId === uid
        })[0].name;
      },
    getAnswersOfQuestion(qId) {
    if (!qId) return "";
    const answers = [];
    this.$store.state.answers.forEach((answer) => {
        if (String(answer.questionOfAnswerId) === String(qId)) {
        answers.push(answer);
        }
    });
    return answers;
    },
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
