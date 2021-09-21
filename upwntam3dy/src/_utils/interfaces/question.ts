export interface questionInterface {
    id: number,
    ownerId: number,
    title: string,
    fullQuestionText : string,
    time: Date,
    likes: number,
    liked: false,
    answersIds: number[],
}