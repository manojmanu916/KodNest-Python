number_count = int(input())

positive_count = 0
negative_count = 0
zero_count = 0
total_sum = 0

for _ in range(number_count):
    num = int(input())
    total_sum += num
    
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"Positive: {positive_count}")
print(f"Negative: {negative_count}")
print(f"Zero: {zero_count}")
print(f"Total: {total_sum}")
