export interface questionInterface {
    id: number,
    ownerId: number,
    title: string,
    fullQuestionText : string,
    time: Date,
    likes: number,
    liked: false,
    course: {
      term: number,
      name: string,
      tags: string,
    },
    answersIds: number[],
}