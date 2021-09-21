import { answerInterface } from '@/_utils/interfaces/answer'
import { questionInterface } from '@/_utils/interfaces/question'
import { userInterface } from '@/_utils/interfaces/user'

export interface stateType {
  users: userInterface[];
  answers: answerInterface[];
  questions: questionInterface[];
  backupQuestions: questionInterface[],
  
  courseInfoPerTerm: [];
  
  pageMode: "questions" | "questionDetails" | "questionCreate";

  likePrimaryColor: string;
  likeSecondaryColor: string;
  bookmarkPrimaryColor: string;
  bookmarkSecondaryColor: string;
}
