export interface answerInterface {
    id: number,
    ownerId: number,
    questionOfAnswerId: number,
    text: string,
    time: Date,
    likes: number,
    liked: boolean,
}