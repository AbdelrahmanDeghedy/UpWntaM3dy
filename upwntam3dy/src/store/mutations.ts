import { stateType } from "./interfaces";

export const mutations = {
  loadUsers(state: stateType, payload: any): void {
    state.users = payload;
  },
  loadAnswers(state: stateType, payload: any): void {
    state.answers = payload;
  },
  loadQuestions(state: stateType, payload: any): void {
    state.questions = payload;
  },
  loadCourseInfoPerTerm(state: stateType, payload: any): void {
    state.courseInfoPerTerm = payload;
  },

  setPageMode(state: stateType, payload: any): void {
    state.pageMode = payload;
  },
};
