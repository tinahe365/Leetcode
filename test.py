# Create a sample dictionary
student_scores = {"Alice": 90, "Bob": 85}

# 1. Access an existing key
score_alice = student_scores.get("Alice")
print(f"Alice's score: {score_alice}")
# Output: Alice's score: 90

# 2. Access a non-existent key without a default value (returns None)
score_dave = student_scores.get("Dave")
print(f"Dave's score: {score_dave}")
# Output: Dave's score: None
print(student_scores)

# 3. Access a non-existent key with a specified default value
score_eve = student_scores.get("Eve", 0)
print(f"Eve's score: {score_eve}")
# Output: Eve's score: 0

# 4. Use for counting occurrences (a common use case)
counts = {}
data = ['a', 'b', 'a', 'c', 'b', 'a']
for item in data:
    counts[item] = counts.get(item, 0) + 1
print(f"Counts: {counts}")
# Output: Counts: {'a': 3, 'b': 2, 'c': 1}
