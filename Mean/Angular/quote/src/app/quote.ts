export class Quote {
    constructor(
        public id: number = null,
        public text: string = "",
        public author: string = "",
        public totalvote: number = 0,
        public created_at: Date = new Date(),
        public updated_at: Date = new Date()
    ){}
}
