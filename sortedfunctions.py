students = [ 
    ("ajay", 80),
    ("rohit", 60),
    ("chinmay", 90),
    ("suraj", 70)
]

sorted_students = sorted(students, key=lambda student: student[1])

print(*sorted_students)