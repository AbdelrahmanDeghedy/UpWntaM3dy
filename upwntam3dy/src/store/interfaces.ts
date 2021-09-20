export interface stateType {
  users: [];
  answers: [];
  questions: [];
  courseInfoPerTerm: [];
  
  pageMode: "questions" | "questionDetails" | "questionCreate";

  likePrimaryColor: string;
  likeSecondaryColor: string;
  bookmarkPrimaryColor: string;
  bookmarkSecondaryColor: string;
}
