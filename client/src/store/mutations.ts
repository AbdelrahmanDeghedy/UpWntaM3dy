import { stateType } from "./interfaces";

import { answerInterface } from '@/_utils/interfaces/answer'
import { questionInterface } from '@/_utils/interfaces/question'
import { userInterface } from '@/_utils/interfaces/user'

export const mutations = {
  loadUsers(state: stateType, payload: userInterface[]): void {
    state.users = [];
    state.users = payload;
  },
  loadAnswers(state: stateType, payload: answerInterface[]): void {
    state.answers = [];
    state.answers = payload;
  },
  loadQuestions(state: stateType, payload: questionInterface[]): void {
    if (!payload) return;
    state.questions = [];
    state.questions = [...payload];
  },
  loadBackupQuestions(state: stateType, payload: questionInterface[]): void {
    state.backupQuestions = payload;
  },
  loadCourseInfoPerTerm(state: stateType, payload: any): void {
    state.courseInfoPerTerm = payload;
  },

  createQuestion (state: stateType, payload: questionInterface): void {
    state.backupQuestions.push(payload);
  },

  // editQuestionContent (state: stateType, payload : { id: number, title: string, fullQuestionText : string }): void {
  //   const modifiedQuestionId = state.questions.findIndex((question) => {
  //     return String(question.id) === String(payload.id);
  //   });
    
  //   state.questions[modifiedQuestionId].title = payload.title;
  //   state.questions[modifiedQuestionId].fullQuestionText = payload.fullQuestionText;
  // },

  filterQuestions (state: stateType, filterText : string): void {
    state.questions = state.backupQuestions.filter((question) => {
      return question.title.toLowerCase().includes(filterText.toLowerCase());
    })
  },
  filterQuestionsByTags (state: stateType, tag : string): void {
    state.questions = state.backupQuestions.filter((question) => {
      let matcher = false;
      question.commaSeparatedTags.split(",").forEach(questionTag => {
        if (questionTag.trim().toLowerCase() === tag.trim().toLowerCase()) {
          matcher = true
        }
      })
      return matcher;
    })
  },

  clearFilterTags (state: stateType): void {
    state.questions = state.backupQuestions;
  },


  createAnswer (state: stateType, payload: answerInterface): void {
    state.answers.push(payload);
  },

  setPageMode(state: stateType, payload: any): void {
    state.pageMode = payload;
  },

  toggleScrollToAnswer(state: stateType): void {
    state.scrollToAnswer = !state.scrollToAnswer;
  },

  createUser(state: stateType, payload: userInterface): void {
    state.users.push(payload);
  },

  setToken (state: stateType, payload: string) : void {
    state.token = payload;
  },

  setCurrentUser (state: stateType, payload: userInterface) : void {
    state.currentUser = payload;
  }
};
