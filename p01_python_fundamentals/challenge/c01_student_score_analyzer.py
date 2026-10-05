"""
Student Score Analyzer

Build a Python program that analyzes a student's scores.

Requirements:
1. Ask the user to enter the student's name.
2. Ask for scores in 5 subjects:
   - Bangla
   - English
   - Mathematics
   - Science
   - ICT
3. Each score must be between 0 and 100.
4. Calculate:
   - Total score
   - Average score
   - Highest score
   - Lowest score
5. Determine whether the student passed or failed.
   - Passing average: 40 or above
6. Display a simple student report containing all the information.

Example Input:
Student name: Rahim
Bangla: 75
English: 82
Mathematics: 91
Science: 68
ICT: 88

Expected Output:
===== Student Score Report =====

Name: Rahim

Bangla: 75
English: 82
Mathematics: 91
Science: 68
ICT: 88

Total: ...
Average: ...
Highest: ...
Lowest: ...
Status: ...

Constraints:
- Use variables.
- Use input().
- Use appropriate numeric conversion.
- Use if/else for the pass/fail decision.
- Do not use functions, lists, loops, or external libraries yet.

Challenge:
What should happen if the user enters a score below 0 or above 100?

"""



# Ask the user to enter the student's name.
student_name = input('Enter your name: ')

# Ask for scores in 5 subjects: [Bangla, English, Mathematics, Science, ICT]
subjects = [ 'Bangla', 'English', 'Mathematics', 'Science', 'ICT']
length = len(subjects)

scores = [0, 0, 0, 0, 0]
hightest_inx = 0
lowest_inx = 0
total_score = 0
avg_score = 0

for i in range(length):
  score = -1
  while(score < 0 or score > 100):
    score = int(input(f'Enter score for {subjects[i]}: '))
  scores[i] = score
  
  if(scores[hightest_inx] < score):
    hightest_inx = i
  if (scores[lowest_inx] > score):
    lowest_inx = i
  
  total_score += score

  
avg_score = total_score/length



# Display
print('\nName: '+ student_name)

for i in range(length):
  print(f"{subjects[i]}: {scores[i]}")

print(f"\nTotal score: {total_score} \nAverage score: {avg_score} \nHighest score: {scores[hightest_inx]} \nLowest score: {scores[lowest_inx]}\n")

if(avg_score >= 40):
  print('Status: PASS')
else:
  print('Status: FAILED')