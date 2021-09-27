export interface courseInterface {
    name: string;
    tags: string[];
}

export interface termInterface {
    term: number,
    courses: courseInterface[],
}
export interface departmentInterface {
    name: string;
    terms: termInterface[];
}

export interface organization {
    name: string;
    departments: departmentInterface[];
}