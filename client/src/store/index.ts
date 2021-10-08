import { createStore } from "vuex";
import { stateType } from "./interfaces";

import { mutations } from "./mutations";



export const store = createStore({
  state(): stateType {
    return {
      users: [],
      answers: [],
      questions: [],
      backupQuestions: [],
      courseInfoPerTerm: [],
      pageMode: "questions",
      likePrimaryColor: "#4287f5",
      likeSecondaryColor: "#e3e3e3",
      bookmarkPrimaryColor: "#d4267a",
      bookmarkSecondaryColor: "#b5a1b2",
      scrollToAnswer: false,
      currentUser : null,
      token : null,
      baseUrl : "http://localhost:5000",
      alternativeImg: 'https://media.istockphoto.com/vectors/male-profile-flat-blue-simple-icon-with-long-shadow-vector-id522855255?k=20&m=522855255&s=612x612&w=0&h=fLLvwEbgOmSzk1_jQ0MgDATEVcVOh_kqEe0rqi7aM5A=',
      mobileResponsive: true,
    };
  },
  mutations,
});
