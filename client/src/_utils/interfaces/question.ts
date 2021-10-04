export interface questionInterface {
    id: number,
    ownerId: number,
    title: string,
    body : string,
    pub_date: Date,
    likes: number,
    answerIds: number[],
    commaSeparatedTags: string,
    department: string,
}