import { stateType } from './interfaces';

export const mutations = {
    loadUsers (state : stateType, payload : any) {
        state.users = payload;
    },
    loadAnswers (state : stateType, payload : any) {
        state.answers = payload;
    },
    loadQuestions (state : stateType, payload : any) {
        state.questions = payload;
    },
    loadCourseInfoPerTerm (state : stateType, payload : any) {
        state.courseInfoPerTerm = payload;
    },
}