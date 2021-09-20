export const users = [
  {
    universityId: 18010917,
    name: "Abdelrahman Deghedy",
    points: 532,
    rank: 2,
    bio: "Be input-driven, not output-driven",
    picture: "",
    answers: {
      answerIds: [5, 8, 4],
    },
    bookmarks: {
      questionIds: [1, 5, 8],
    },
  },
  {
    universityId: 18010918,
    name: "Habiba Deghedy",
    points: 532,
    rank: 2,
    bio: "Be input-driven, not output-driven",
    picture: "",
    answers: {
      answerIds: [5, 8, 4],
    },
    bookmarks: {
      questionIds: [1, 5, 8],
    },
  },
];

export const answers = [
  {
    id: 10,
    ownerId: 180110918,
    questionOfAnswerId: 4,
    text: "It's 3!",
    time: Date.now(),
    likes: 20,
  },
  {
    id: 5,
    ownerId: 180110917,
    questionOfAnswerId: 2,
    text: "It's 3!",
    time: Date.now(),
    likes: 5,
  },
];

export const questions = [
  {
    id: 4,
    ownerId: 18010917,
    title: "What's the square root of 9?",
    fullQuestionText : "What's the square root of 9, please?",
    time: new Date(2021, 3, 5),
    likes: 15,
    course: {
      term: 5,
      name: "Operating Systems",
      tags: "lec1",
    },
    answersIds: [10],
  },
  {
    id: 2,
    ownerId: 18010918,
    title: "What's the square root of 16?",
    fullQuestionText : "What's the square root of 16, please?",
    time: new Date(2021, 3, 5),
    likes: 5,
    course: {
      term: 5,
      name: "Operating Systems",
      tags: "lec2",
    },
    answersIds: [5, 1],
  },
];

export const courseInfoPerTerm = [
  {
    term: "1",
    courses: [
      {
        name: "Data Structure",
        tags: ["chapter1"],
      },
      {
        name: "Micro Processor 2",
        tags: ["chapter1"],
      },
      {
        name: "Electromagnetic 2",
        tags: ["chapter1"],
      },
      {
        name: "Operating Systems",
        tags: ["chapter1"],
      },
    ],
  },
  {
    term: "2",
    courses: [
      {
        name: "Eskat",
        tags: ["chapter1"],
      },
      {
        name: "MicroController",
        tags: ["chapter1"],
      },
      {
        name: "Energy",
        tags: ["chapter1"],
      },
      {
        name: "Math1",
        tags: ["chapter1"],
      },
    ],
  },
];
