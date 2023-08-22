student_heights = input("Input a list of student hieghts").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

total = 0
count = 0

for s in student_heights:
    total += s
    count += 1

avg = round(total / count)

print(f"The average height is {avg}")