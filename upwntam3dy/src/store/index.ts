import { createStore } from "vuex";
import { stateType } from "./interfaces";

import { mutations } from "./mutations";



export const store = createStore({
  state(): stateType {
    return {
      users: [],
      answers: [],
      questions: [],
      courseInfoPerTerm: [],
      pageMode: "questions",
      likePrimaryColor: "#4287f5",
      likeSecondaryColor: "#e3e3e3",
      bookmarkPrimaryColor: "#d4267a",
      bookmarkSecondaryColor: "#b5a1b2",
    };
  },
  mutations,
});
