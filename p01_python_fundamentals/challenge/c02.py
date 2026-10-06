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
   - Keeping only students with valid name, department, age, and unique id (second one will be count as invalid)
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



import json



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
    {
        "id": 2,
        "name": "Karim",
        "department": "EEE",
        "age": 22,
        "scores": {
            "math": 72,
            "python": 80,
            "database": 75
        }
    },
    {
        "id": 3,
        "name": "Hasan",
        "department": "CSE",
        "age": 20,
        "scores": {
            "math": 95,
            "python": 88,
            "database": 92
        }
    },
    {
        "id": 4,
        "name": "Nadia",
        "department": "BBA",
        "age": 23,
        "scores": {
            "math": 78,
            "python": 82,
            "database": 85
        }
    },
    {
        "id": 5,
        "name": "",
        "department": "CSE",
        "age": 21,
        "scores": {
            "math": 80,
            "python": 85,
            "database": 88
        }
    },
    {
        "id": 6,
        "name": "Sakib",
        "department": "EEE",
        "age": -5,
        "scores": {
            "math": 70,
            "python": 75,
            "database": 80
        }
    },
    {
        "id": 7,
        "name": "Mim",
        "department": "CSE",
        "age": 22,
        "scores": {
            "math": 105,
            "python": 91,
            "database": 87
        }
    },
    {
        "id": 8,
        "name": "Tanvir",
        "department": "",
        "age": 24,
        "scores": {
            "math": 76,
            "python": 81,
            "database": 79
        }
    },
    {
        "id": 9,
        "name": "Rafi",
        "department": "BBA",
        "age": 22,
        "scores": {
            "math": 88,
            "python": 84,
            "database": 90
        }
    },
    {
        "id": 10,
        "name": "Jannat",
        "department": "CSE",
        "age": 20,
        "scores": {
            "math": 92,
            "python": 95
        }
    },
    {
        "id": 3,
        "name": "Hasan Duplicate",
        "department": "CSE",
        "age": 20,
        "scores": {
            "math": 90,
            "python": 90,
            "database": 90
        }
    },
    {
        "id": 11,
        "name": "Fahim",
        "department": "EEE",
        "age": 21,
        "scores": {
            "math": 65,
            "python": -10,
            "database": 72
        }
    }
]


# print(json.dumps(students, indent=4))

cleaned_students = []
seen_ids = set()
for student in students:
   student_id = student["id"]
   name = student["name"]
   department = student["department"]
   age = student["age"]

   # validate basic information
   if not name or not department or age < 0 or age > 100 or student_id in seen_ids:
      continue
   
   seen_ids.add(student_id)
   
   # clean the scores
   valid_scores = {}
   for subject, score in student['scores'].items():
      if score < 0 or score > 100:
         continue
      valid_scores[subject] = score
      
   # calculate student's average
   total_score = sum(valid_scores.values())
   avg_score = total_score/len(valid_scores)
   
   
   cleaned_students.append({
      "id": student_id,
      "name": name,
      "department": department,
      "age": age,
      "scores": valid_scores,
      "average": avg_score
   })

#  group by dep
group_dep = {}
for student in cleaned_students:
   department = student["department"]
   
   if department not in group_dep:
      group_dep[department] = []
   
   group_dep[department].append(student)

print(group_dep)
