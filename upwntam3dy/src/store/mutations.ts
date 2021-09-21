import { stateType } from "./interfaces";

import { answerInterface } from '@/_utils/interfaces/answer'
import { questionInterface } from '@/_utils/interfaces/question'
import { userInterface } from '@/_utils/interfaces/user'

export const mutations = {
  loadUsers(state: stateType, payload: userInterface[]): void {
    state.users = payload;
  },
  loadAnswers(state: stateType, payload: answerInterface[]): void {
    state.answers = payload;
  },
  loadQuestions(state: stateType, payload: questionInterface[]): void {
    state.questions = payload;
  },
  loadCourseInfoPerTerm(state: stateType, payload: any): void {
    state.courseInfoPerTerm = payload;
  },

  createQuestion(state: stateType, payload: questionInterface): void {
    state.questions.push(payload);
  },

  setPageMode(state: stateType, payload: any): void {
    state.pageMode = payload;
  },
};
