# 1. Write data to the file (overwrites existing content)
file = open("students.txt", "w")
file.write("Aarav\nMeera\nKabir\n")
file.close()

# 2. Append new data to the file
file = open("students.txt", "a")
file.write("Rohan\n")
file.close()

# 3. Read and print all data from the file
file = open("students.txt", "r")
print("--- Student Records ---")
print(file.read())
file.close()