import { answerInterface } from '@/_utils/interfaces/answer'
import { questionInterface } from '@/_utils/interfaces/question'
import { userInterface } from '@/_utils/interfaces/user'

export interface stateType {
  users: userInterface[];
  answers: answerInterface[];
  questions: questionInterface[];
  backupQuestions: questionInterface[],
  
  courseInfoPerTerm: [];
  
  pageMode: "questions" | "questionDetails" | "questionCreate" | "profile" | "auth" | "leaderboard" | "home" | "notfound";

  likePrimaryColor: string;
  likeSecondaryColor: string;
  bookmarkPrimaryColor: string;
  bookmarkSecondaryColor: string;

  scrollToAnswer: boolean;

  currentUser : userInterface;
  
  token : string;

  baseUrl : string;

  alternativeImg : string;

  mobileResponsive: boolean;
}
