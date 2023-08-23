student_scores = {
    "Harry" : 81,
    "B" : 78,
    "C" : 99,
    "D": 74,
    "N": 62
}

student_grades = {}
grade = ''

for student in student_scores:
    score = student_scores[student]
    
    if score <= 70:
        grade = 'Fail'
        
    elif 71 <= score <= 80:
        grade = 'Acceptable'
        
    else:
        grade = "Mamma mia pizza"
        
    student_grades[student] = grade

print(student_grades)