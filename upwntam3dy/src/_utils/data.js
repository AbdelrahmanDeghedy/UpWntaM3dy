const users = [
    {
        UnniversityId : 18010917,
        name : "Abdelrahman Deghedy",
        points : 532,
        rank : 2,
        bio : "Be input-driven, not output-driven",
        picture : "",
        answers : {
            answerIds : [5, 8, 4]
        },
        bookmarks : {
            questionIds : [1, 5, 8]
        }
    },
    {
        UnniversityId : 18010918,
        name : "Habiba Deghedy",
        points : 532,
        rank : 2,
        bio : "Be input-driven, not output-driven",
        picture : "",
        answers : {
            answerIds : [5, 8, 4]
        },
        bookmarks : {
            questionIds : [1, 5, 8]
        }
    },
]

const answers = [
    {
        id : 10,
        ownerId : 180110918,
        questionOfAnswerId : 4,
        text : "It's 3!",
        time : Date.now(),
        likes : 20,   
    },
    {
        id : 5,
        ownerId : 180110917,
        questionOfAnswerId : 2,
        text : "It's 3!",
        time : Date.now(),
        likes : 5,   
    }
]

const questions = [
    {
        id : 4,
        ownerId :18010917,
        text : "What's the square root of 9?",
        time : Date.now(),
        likes : 15,
        course : {
            term : 5,
            name : "Operating Systems",
            tags : "lec1",
        },
        answersIds : [
            10
        ]
    },
    {
        id : 2,
        ownerId :18010918,
        text : "What's the square root of 16?",
        time : Date.now(),
        likes : 5,
        course : {
            term : 5,
            name : "Operating Systems",
            tags : "lec2",
        },
        answersIds : [
            5
        ]
    }
]