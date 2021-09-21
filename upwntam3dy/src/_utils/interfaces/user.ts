export interface userInterface {
    universityId: number,
    name: string,
    points: number,
    rank: number,
    bio: string,
    picture: string,
    answers: {
      answerIds: number[],
    },
    bookmarks: {
      questionIds: number[],
    },
}