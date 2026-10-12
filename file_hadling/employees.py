# Writing initial employee details
with open("employees.txt", "w") as file:
    file.write("ID: 101, Name: Priya, Role: Developer\n")
    file.write("ID: 102, Name: Vikram, Role: Tester\n")

# Appending another employee
with open("employees.txt", "a") as file:
    file.write("ID: 103, Name: Ananya, Role: Manager\n")

# Reading line by line using file handling
print("--- Employee Details ---")
with open("employees.txt", "r") as file:
    for line in file:
        print(line.strip())