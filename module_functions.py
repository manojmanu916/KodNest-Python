def calculation(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b if b != 0 else None
    return add, sub, mul, div


# Alias in case original name 'claculation' is expected
claculation = calculation

if __name__ == "__main__":
    add, sub, mul, div = calculation(10, 2)
    print(f"Addition: {add}")
    print(f"Subtraction: {sub}")
    print(f"Multiplication: {mul}")
    print(f"Division: {div}")
