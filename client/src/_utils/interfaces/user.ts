export interface userInterface {
    email: string,
    universityId: number,
    name: string,
    points: number,
    rank: number,
    bio: string,
    picture: string,
    questionIds : number[], 
    answerIds: number[],
    bookmarkedQuestionIds : number[],
    bookmarkedAnswerIds : number[],
    department: String,
    likedAnswerIds : number[],
    likedQuestionIds : number[],
}