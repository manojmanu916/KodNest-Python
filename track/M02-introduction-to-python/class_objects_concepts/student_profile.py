class StudentProfile:
    def __init__(
        self,
        student_id,
        name,
        course,
        score=0.0,
        is_placed=False
    ):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.is_placed = is_placed

    def __str__(self):
        placement_status = (
            "Placed" if self.is_placed
            else "Not Placed"
        )
        return f"{self.student_id} | {self.name} | {self.course} | {self.score} | {placement_status}"


student_one = StudentProfile(
    name="Asha",
    score=85.0,
    student_id=101,
    course="Python"
)

student_two = StudentProfile(
    course="Java",
    student_id=102,
    name="Rahul",
    score=0,
)

print(student_one)
print(student_two)
