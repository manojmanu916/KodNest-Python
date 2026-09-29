students = [
    ["Alice", 85, 90, 70],
    ["Bob", 70, 80, 92],
    ["Charlie", 90, 80, 80],
    ["David", 60, 75, 60],
    ["Eva", 88, 92, 93],
    ["Frank", 72, 65, 80],
    ["Grace", 80, 85, 82]
]


# 1. Calculate average for each student
averages = {}

for student in students:
    name = student[0]
    marks = student[1:]
    average = round(sum(marks) / len(marks), 2)
    averages[name] = average


# 2. Students who scored 80 or above in ALL subjects
top_students = [
    student[0]
    for student in students
    if all(mark >= 80 for mark in student[1:])
]


# 3. Students who scored below 70 in at least one subject
weak_students = [
    student[0]
    for student in students
    if any(mark < 70 for mark in student[1:])
]


# 4. Dictionary containing students with average 80 or above
high_performers = {
    name: average
    for name, average in averages.items()
    if average >= 80
}


# 5. Find the highest-scoring student
highest_student = max(averages, key=averages.get)
highest_average = averages[highest_student]


# 6. Calculate subject averages
math_average = round(
    sum(student[1] for student in students) / len(students), 2
)

science_average = round(
    sum(student[2] for student in students) / len(students), 2
)

english_average = round(
    sum(student[3] for student in students) / len(students), 2
)


# 7. Print the report
print("===== STUDENT REPORT =====")

for name, average in averages.items():
    print(f"{name} -> Average: {average:.2f}")

print("\nTop Students:")
print(top_students)

print("\nStudents needing improvement:")
print(weak_students)

print("\nHighest Scoring Student:")
print(f"{highest_student} -> {highest_average:.2f}")

print("\nSubject Averages:")
print(f"Math: {math_average:.2f}")
print(f"Science: {science_average:.2f}")
print(f"English: {english_average:.2f}")