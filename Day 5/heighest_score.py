student_scores = input("Input a list of student scores").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)

max_score = 0

for s in student_scores:
    if s > max_score:
        max_score = s
 


print(f"The max height is {max_score}")