from module_functions import calculation

# Taking values to perform calculations
num1 = 10
num2 = 5

# Calling the function from module_functions
add, sub, mul, div = calculation(num1, num2)

# Displaying the results
print("===== CALCULATION RESULTS =====")
print(f"Numbers: {num1} and {num2}")
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")
