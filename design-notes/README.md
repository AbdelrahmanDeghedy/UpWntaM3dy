# API Endpoints

## System Roles

1. Not-Authed.
1. Admin (Authed).
2. Student (Authed).

---

### Organization

1. Endpoint:
```ts
"/api/v1/organizations"
```

2. Method.

- GET.

3. Body.

4. Permissions

    A. Read.
    
    - Admin

    B. Write.
        
    - N/A

5. Description.
- Get all available organizations.

---

### Organization

1. Endpoint:
```ts
"/api/v1/organizations/create"
```

2. Method.

- POST.

3. Body.

```ts
{
     organizationName: String,
     departmentName: departmentInterface[];
}
```

4. Permissions

    A. Read.
    
    - Admin

    B. Write.
        
    - Admin.

5. Description.
- Create a new organization.

---

### Department

1. Endpoint:
```ts
"/api/v1/departments"
```

2. Method.

- GET.

3. Body.

4. Permissions

    A. Read.
    
    - Admin

    B. Write.
        
    - N/A

5. Description.
- Get all available deparments.

---

### Department

1. Endpoint:
```ts
"/api/v1/departments/create"
```

2. Method.

- POST.

3. Body.

```ts
{
    name: String;
    terms: termInterface[];
}
```

4. Permissions

    A. Read.
    
    - Admin

    B. Write.
        
    - Admin

5. Description.
- Create a new department.

---

### Course

1. Endpoint:
```ts
"/api/v1/courses"
```

2. Method.

- GET.

3. Body.

4. Permissions

    A. Read.
    
    - Admin

    B. Write.
        
    - N/A

5. Description.
- Get all available courses.

---

### Course

1. Endpoint:
```ts
"/api/v1/courses/create"
```

2. Method.

- POST.

3. Body.

```ts
{
    name: String;
    terms: string[];
}
```

4. Permissions

    A. Read.
    
    - Admin

    B. Write.
        
    - Admin

5. Description.
- Create a new course.

---


### Auth

1. Endpoint:
```ts
"/api/v1/users/signup"
```

2. Method.

- POST.

3. Body.
```ts
{
    name: string,
    email: string,
    password: string,
    universityId: number,
    organization: string,
    department: string,
}
```

4. Permissions

    A. Read.
    
    - N/A

    B. Write.
        
    - All

5. Description.
- Sign up

---

### Auth

1. Endpoint:
```ts
"/api/v1/users/signin"
```

2. Method.

- POST.

3. Body.
```ts
{
    email: string,
    password: string,
}
```

4. Permissions

    A. Read.
    
    - N/A

    B. Write.
        
    - All

5. Description.
- Sign in

---


### Auth

1. Endpoint:
```ts
"/api/v1/users/signout"
```

2. Method.

- POST.

3. Body.

4. Permissions

    A. Read.
    
    - N/A

    B. Write.
        
    - Authed only.

5. Description.
- Sign out

---


### Auth

1. Endpoint:
```ts
"/api/v1/users/currentUser"
```

2. Method.

- GET.

3. Body.


4. Permissions

    A. Read.
    
    - Authed users only.

    B. Write.
        
    - N/A

5. Description.
- Get current user data

---


### Questions

1. Endpoint:
```ts
"/api/v1/:uid/questions"
```

2. Method.

- GET.

3. Body.


4. Permissions

    A. Read.
    
    - Authed users only.

    B. Write.
        
    - N/A

5. Description.
- Get all questions, that matches the user's: orgnization and department.

---


### Questions

1. Endpoint:
```ts
"/api/v1/:uid/questions/:qid"
```

2. Method.

- GET.

3. Body.


4. Permissions

    A. Read.
    
    - Authed users only.

    B. Write.
        
    - N/A

5. Description.
- Get question with id === qid, and it's one of the allowed questions to uid

---


### Questions

1. Endpoint:
```ts
"/api/v1/:uid/questions/create"
```

2. Method.

- POST.

3. Body.
```ts
{
    fullQuestionText: string,
}
```

4. Permissions

    A. Read.
    
    - N/A.

    B. Write.
        
    - Authed users only.

5. Description.
- Create a question for uid.
- The organization and department for the question will be extracted from the current user data.
---


### Questions

1. Endpoint:
```ts
"/api/v1/:uid/questions/:qid/edit"
```

2. Method.

- PUT.

3. Body.
```ts
{
    fullQuestionText: string,
}
```

4. Permissions

    A. Read.
    
    - Authed users only, and **only the question owner only**.

    B. Write.
        
    - N/A

5. Description.
- Edit a question with id === qid, written by user uid.

---


### Questions

1. Endpoint:
```ts
"/api/v1/:uid/questions/:qid/delete"
```

2. Method.

- DELETE.

3. Body.


4. Permissions

- Authed users only, and **only the question owner only**.


5. Description.
- Delete a question with id === qid, written by user uid.

---

### Answers

1. Endpoint:
```ts
"/api/v1/:uid/answers"
```

2. Method.

- GET.

3. Body.

4. Permissions

    A. Read.
    
    - Authed users only.

    B. Write.
        
    - N/A

5. Description.

- Get all answers for uid

---
### Answers

1. Endpoint:
```ts
"/api/v1/:uid/:qid/answers/create"
```

2. Method.

- POST.

3. Body.
```ts
{
    fullAnswerText: string,
}
```
4. Permissions

    A. Read.
    
    - N/A.

    B. Write.
        
    - Authed users only, and **uid only**

5. Description.

- Create an answer for question (qid), by user (uid).

---

### Answers

1. Endpoint:
```ts
"/api/v1/:uid/answers/:aid/edit"
```

2. Method.

- PUT.

3. Body.
```ts
{
    fullAnswerText: string,
}
```

4. Permissions

    A. Read.
    
    - N/A.

    B. Write.
        
    - Authed users only, and **uid only**

5. Description.

- Edit an answer with id === aid, by user (uid).
---

### Answers

1. Endpoint:
```ts
"/api/v1/:uid/answers/:aid/delete"
```

2. Method.

- DELETE.

3. Body.

4. Permissions
    - Authed users only, and **uid only**

5. Description.

- Delete an answer with id === aid, by user (uid).
---

### Users

1. Endpoint:
```ts
"/api/v1/users/leaderboard"
```

2. Method.

- GET.

3. Body.

4. Permissions

    A. Read.
    
    - Authed users only.

    B. Write.
        
    - N/A.

5. Description.

- Get all users ranked by points.
---

### Courses

1. Endpoint:
```ts
"/api/v1/:uid/:tid/courses"
```

2. Method.

- GET.

3. Body.

4. Permissions

    A. Read.
    
    - 

    B. Write.
        
    - N/A.

5. Description.

- Get all courses available for user (uid), on the term (tid).
---

