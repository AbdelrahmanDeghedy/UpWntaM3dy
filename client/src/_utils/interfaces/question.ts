export interface questionInterface {
    id: number,
    owner: number,
    title: string,
    body : string,
    pub_date: Date,
    likes: number,
    answerIds: number[],
    commaSeparatedTags: string,
    department: string,
}