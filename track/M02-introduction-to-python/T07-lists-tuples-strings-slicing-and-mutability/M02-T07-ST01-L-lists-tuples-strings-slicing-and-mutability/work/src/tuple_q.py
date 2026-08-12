# Read the course details
Course_name = input()
Current_week = input()
Course_status = input()

# Create the original tuple
course_details = (Course_name, Current_week, Course_status)

# Read the updated week
updated_week = input()

# Create and assign a new tuple
course_details = (course_details[0], updated_week, course_details[2])

# Display the updated tuple
print(course_details)
