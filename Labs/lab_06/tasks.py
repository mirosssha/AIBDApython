"""
NSU Python — Lab 06
Functions as Values: lambda, Sorting, Filtering, and map

Complete Tasks 1–12.
Tasks 13–14 are optional bonus tasks.

Use only concepts covered in Lecture 06 and earlier lectures.
"""

# ============================================================
# Task 1 — Functions as values
# ============================================================
# Create a function:
#
#   square(number)
#
# that returns number ** 2.
#
# Then:
# 1. assign the function object to a new variable called operation;
# 2. call square(5);
# 3. call operation(5);
# 4. print whether operation is square.
#
# Expected final comparison:
# True
#
# Important:
# operation = square
# stores the function object.
#
# operation = square()
# would call the function immediately.

# Write your code below:

def square(number):
    return number ** 2


operation = square

print(square(5))
print(operation(5))
print(operation is square)

print()
# ============================================================
# Task 2 — Passing a function as an argument
# ============================================================
# Create:
#
#   double(number)
#   triple(number)
#
# Then create:
#
#   apply(operation, value)
#
# apply() should call operation(value) and return the result.
#
# Examples:
# apply(double, 5) -> 10
# apply(triple, 5) -> 15
#
# Pass the function names WITHOUT parentheses.

# Write your code below:

def double(number):
    return number * 2

def triple(number):
    return number * 3

def apply(operation, value):
    return operation(value)

print(apply(double, 5))
print(apply(triple, 5))

print()

# ============================================================
# Task 3 — Higher-order function
# ============================================================
# Create:
#
#   transform(values, operation)
#
# It should:
# - create an empty result list;
# - loop through values;
# - apply operation() to each value;
# - append each result;
# - return the new list.
#
# Then create:
#
#   square(number)
#
# Test:
# transform([1, 2, 3, 4], square)
#
# Expected:
# [1, 4, 9, 16]

# Write your code below:

def transform(values, operation):
    result = []

    for value in values:
        value = operation(value)
        result.append(value)

    return result

def square(number):
    return number ** 2

print(transform([1, 2, 3, 4], square))

print()
# ============================================================
# Task 4 — Lambda expressions
# ============================================================
# Create these lambda functions:
#
#   double
#   add
#   is_even
#
# Requirements:
# double(5)    -> 10
# add(3, 4)    -> 7
# is_even(8)   -> True
# is_even(7)   -> False
#
# Each lambda must contain only one expression.

# Write your code below:

double = lambda a: a * 2
add = lambda a, b: a + b
is_even = lambda a: a % 2 == 0

print(double(5))
print(add(3, 4))
print(is_even(8))
print(is_even(7))

print()
# ============================================================
# Task 5 — sorted() versus list.sort()
# ============================================================
# Start with:
#
# numbers = [8, 3, 10, 1, 6]
#
# Part A:
# Use sorted() to create a NEW list called ordered.
#
# Print:
# - numbers
# - ordered
#
# Confirm that numbers did not change.
#
# Part B:
# Call numbers.sort().
# Print numbers again.
#
# Expected sorted order:
# [1, 3, 6, 8, 10]
#
# Also store the result of numbers.sort() in a variable:
#
#   result = numbers.sort()
#
# Print result.
#
# What does list.sort() return?

# Write your code below:

numbers = [8, 3, 10, 1, 6]

ordered = sorted(numbers)
print(numbers)
print(ordered)

numbers.sort()
print(numbers)

result = numbers.sort()

print(result)

print()
# ============================================================
# Task 6 — Descending order
# ============================================================
# Start with:
#
# scores = [82, 95, 73, 88, 61]
#
# Use sorted() with reverse=True.
#
# Store the result in:
#
#   high_to_low
#
# Expected:
# [95, 88, 82, 73, 61]
#
# The original scores list should remain unchanged.

# Write your code below:

scores = [82, 95, 73, 88, 61]
high_to_low = sorted(scores, reverse=True)

print(scores)
print(high_to_low)

print()
# ============================================================
# Task 7 — Sorting with key
# ============================================================
# Start with:
#
# words = ["pear", "watermelon", "fig", "banana", "kiwi"]
#
# Create:
#
#   shortest_first
#   longest_first
#
# shortest_first:
# sort by string length from shortest to longest.
#
# longest_first:
# sort by string length from longest to shortest.
#
# Use key=len for at least one of the two results.
#
# Do not manually calculate the lengths.

# Write your code below:

words = ["pear", "watermelon", "fig", "banana", "kiwi"]

shortest_first = sorted(words, key = len)
longest_first = sorted(words, key=len, reverse=True)

print(shortest_first)
print(longest_first)

print()
# ============================================================
# Task 8 — Case-insensitive sorting
# ============================================================
# Start with:
#
# cities = [
#     "berlin",
#     "Algiers",
#     "cairo",
#     "Amsterdam",
#     "zurich"
# ]
#
# Sort the list alphabetically without treating uppercase
# and lowercase letters as separate groups.
#
# Use:
#
#   key=str.lower
#
# Store the result in:
#
#   ordered_cities
#
# The original capitalization must stay unchanged.

# Write your code below:

cities = [
    "berlin",
    "Algiers",
    "cairo",
    "Amsterdam",
    "zurich"
]

ordered_cities = sorted(cities, key=str.lower)

print(ordered_cities)

print()
# ============================================================
# Task 9 — Sorting tuples with lambda
# ============================================================
# Start with:
#
# students = [
#     ("Anna", 82),
#     ("Boris", 95),
#     ("Mira", 88),
#     ("Daniel", 73)
# ]
#
# Sort students by score from highest to lowest.
#
# Use:
#
#   sorted()
#   key=lambda ...
#   reverse=True
#
# Expected first item:
# ("Boris", 95)

# Write your code below:

students = [
    ("Anna", 82),
    ("Boris", 95),
    ("Mira", 88),
    ("Daniel", 73)
]

ordered_students = sorted(students, key = lambda student: student[1], reverse = True)

print(ordered_students)

print()
# ============================================================
# Task 10 — Filtering values
# ============================================================
# Start with:
#
# scores = [45, 70, 82, 39, 91, 60, 58]
#
# Use filter() and a lambda to keep only scores >= 60.
#
# Convert the filter result to a list.
#
# Expected:
# [70, 82, 91, 60]

# Write your code below:

scores = [45, 70, 82, 39, 91, 60, 58]

passing_scores = list(filter(lambda score: score >=60, scores))

print(passing_scores)

print()
# ============================================================
# Task 11 — Transforming values with map()
# ============================================================
# Start with:
#
# prices = [100, 250, 80, 40]
#
# Use map() and a lambda to increase every price by 10%.
#
# Convert the result to a list.
#
# Expected:
# [110.0, 275.0, 88.0, 44.0]
#
# Note:
# Floating-point output may sometimes contain small
# representation differences.

# Write your code below:

prices = [100, 250, 80, 40]
new_prices = list(
    map(lambda price: price * 1.10, prices)
)

print(new_prices)

print()
# ============================================================
# Task 12 — Filter, sort, and map together
# ============================================================
# Start with:
#
# students = [
#     {"name": "Anna", "score": 82},
#     {"name": "Boris", "score": 55},
#     {"name": "Mira", "score": 91},
#     {"name": "Daniel", "score": 67},
#     {"name": "Sara", "score": 48}
# ]
#
# Step 1:
# Use filter() to keep students with score >= 60.
#
# Step 2:
# Use sorted() to order the passing students from
# highest score to lowest score.
#
# Step 3:
# Use map() to create a list containing only their names.
#
# Expected names:
# ["Mira", "Anna", "Daniel"]
#
# Use lambda expressions for the filter, sorting key,
# and map transformation.

# Write your code below:

students = [
    {"name": "Anna", "score": 82},
    {"name": "Boris", "score": 55},
    {"name": "Mira", "score": 91},
    {"name": "Daniel", "score": 67},
    {"name": "Sara", "score": 48}
]

A_students = list(filter(lambda student: student["score"] >= 60, students))

sorted_students = sorted(A_students, key = lambda student: student['score'], reverse = True)

names = list(map(lambda student: student["name"], sorted_students))

print("Task 12")
print(names)
# ============================================================
# Task 13 — BONUS: Sort records by multiple ideas
# ============================================================
# Start with:
#
# products = [
#     {"name": "Keyboard", "price": 70},
#     {"name": "Mouse", "price": 25},
#     {"name": "Monitor", "price": 220},
#     {"name": "USB Cable", "price": 10}
# ]
#
# Create:
#
#   by_price
#   by_name_length
#
# by_price:
# sort from cheapest to most expensive.
#
# by_name_length:
# sort by the length of the product name,
# from shortest to longest.
#
# Use lambda expressions as sorting keys.

# Write your code below:


# ============================================================
# Task 14 — BONUS: Student ranking pipeline
# ============================================================
# Start with:
#
# students = [
#     ("Anna", 82),
#     ("Boris", 55),
#     ("Mira", 91),
#     ("Daniel", 67),
#     ("Sara", 48),
#     ("Omar", 76)
# ]
#
# Build this pipeline:
#
# 1. filter() -> keep scores >= 60
# 2. sorted() -> highest score first
# 3. map() -> convert each tuple to a string:
#
#       "Name: score"
#
# Expected:
# [
#     "Mira: 91",
#     "Anna: 82",
#     "Omar: 76",
#     "Daniel: 67"
# ]
#
# Store the final result in:
#
#   ranking
#
# Print ranking.

# Write your code below:
