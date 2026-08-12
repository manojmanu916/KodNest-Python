n = int(input())
scores = []

# Read and store all scores
for i in range(n):
    num = int(input())
    scores.append(num)

search_score = int(input())

# Display the highest, lowest and total scores
print("Highest Score:", max(scores))
print("Lowest Score:", min(scores))
print("Total Score:", sum(scores))

# Display whether search_score is present
if search_score in scores:
    print("Search Result: Found")
else:
    print("Search Result: Not Found")
