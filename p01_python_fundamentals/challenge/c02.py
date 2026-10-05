"""
Medium: Clean and Group Nested Student Records

You are given a list of student records containing nested data.

Your task is to clean the data and group students by department.

Requirements:
1. Create a list containing at least 8 student records.
2. Each student should contain:
   - id
   - name
   - department
   - age
   - scores
3. The scores should be stored as nested data for multiple subjects.
4. Some records should contain invalid or missing data, such as:
   - Missing name
   - Missing department
   - Invalid age
   - Score below 0 or above 100
   - Missing subject score
   - Duplicate student ID
5. Clean the records by:
   - Removing invalid students
   - Removing duplicate student IDs
   - Ignoring invalid subject scores
   - Keeping only students with valid name, department, and age
6. Calculate each valid student's average score.
7. Group the cleaned students by department.
8. For each department, display:
   - Number of students
   - Student names
   - Department average score
   - Highest-scoring student
9. Display the final cleaned and grouped result in a readable format.

Example structure:

students = [
    {
        "id": 1,
        "name": "Rahim",
        "department": "CSE",
        "age": 21,
        "scores": {
            "math": 85,
            "python": 90,
            "database": 78
        }
    },
    ...
]

Expected output structure:

===== CSE =====

Students: 3
Names: Rahim, Karim, Hasan
Department Average: ...
Highest Student: ...

===== EEE =====

Students: 2
Names: ...
Department Average: ...
Highest Student: ...

Constraints:
- Use lists and dictionaries.
- Use loops.
- Use if/else conditions.
- Use nested data access.
- Do not use pandas or external libraries.
- Try to keep the solution clean and readable.

Challenge:
After grouping the students, sort each department's students from highest average score to lowest average score.
"""
