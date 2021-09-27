# API Endpoints

## System Roles

1. Admin.
2. Student.

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
