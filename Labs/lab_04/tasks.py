"""
NSU Python — Lab 04
while Loops, Typing, Identity, and Functions

Complete Tasks 1–13.
Tasks 14–15 are optional bonus tasks.

Use only concepts covered in Lecture 04 and earlier lectures.
"""


# ============================================================
# Task 1 — Countdown with while
# ============================================================
# Ask the user for a positive integer.
#
# Use a while loop to print from that number down to 1.
# Then print:
#   Go!
#
# Example:
# Input: 5
# Output:
# 5
# 4
# 3
# 2
# 1
# Go!
#
# Make sure the loop variable changes.

# Write your code below:

number = int(input("Enter a positive integer: "))

while number > 0:
    print(number)
    number -= 1

print("Go!")

# ============================================================
# Task 2 — Repeat until zero
# ============================================================
# Repeatedly ask the user to enter an integer.
#
# Stop when the user enters 0.
#
# Before 0 is entered:
#   count how many non-zero numbers were entered;
#   calculate their sum.
#
# At the end print:
#   Count: ...
#   Sum: ...
#
# Example:
# Input: 5, -2, 7, 0
# Count: 3
# Sum: 10

# Write your code below:

count = 0
total = 0

number = int(input("Enter an integer: "))

while number != 0:
    count += 1
    total += number
    number = int(input("Enter an integer: "))

print(f"Count: {count}")
print(f"Sum: {total}")

# ============================================================
# Task 3 — Valid input with while True
# ============================================================
# Repeatedly ask the user for an integer from 1 to 10.
#
# If the value is outside this range:
#   print "Invalid value"
#   ask again.
#
# When the user enters a valid value:
#   print "Accepted"
#   stop the loop with break.
#
# Required:
# Use:
#   while True
#   break

# Write your code below:

while True:
    number = int(input("Enter an integer from 1 to 10 "))

    if number < 1 or number > 10:
        print("Invalid value")
    else:
        print("Accepted")
        break

# ============================================================
# Task 4 — continue in a while loop
# ============================================================
# Use a while loop to process numbers from 1 through 20.
#
# Skip numbers divisible by 3 using continue.
# Print all other numbers.
#
# IMPORTANT:
# Update the loop variable correctly so you do not create
# an infinite loop.

# Write your code below:

number = 1

while number <= 20:
    if number % 3 == 0:
        number += 1
        continue

    print(number)
    number += 1
# ============================================================
# Task 5 — Search with loop else
# ============================================================
numbers = [4, 8, 12, 16, 21, 24]

# Search for the first odd number.
#
# If an odd number is found:
#   print "First odd number: <value>"
#   stop using break.
#
# If the loop finishes without finding any odd number:
#   print "All values are even"
#
# Required:
# Use:
#   for
#   break
#   else

# Write your code below:

for number in numbers:
    if number % 2 != 0:
        print(f"First odd number: {number}")
        break
else:
    print("All values are even")

# ============================================================
# Task 6 — Multiplication table with nested loops
# ============================================================
# Use nested for loops to print a 5 x 5 multiplication table.
#
# Rows: 1 through 5
# Columns: 1 through 5
#
# Example first row:
# 1 2 3 4 5
#
# Example second row:
# 2 4 6 8 10
#
# Hint:
# Build each row using print(..., end=" ") and print().

# Write your code below:

for row in range(1, 6):
    for column in range(1, 6):
        print(row * column, end=" ")

    print()

# ============================================================
# Task 7 — Dynamic typing
# ============================================================
# Create a variable named value.
#
# First assign:
#   42
# Print the value and its type.
#
# Then assign:
#   3.14
# Print the value and its type.
#
# Then assign:
#   "Python"
# Print the value and its type.
#
# Finally assign:
#   [1, 2, 3]
# Print the value and its type.
#
# Observe that the same variable name can refer to objects
# of different types during program execution.

# Write your code below:

value = 42
print(value, type(value))

value = 3.14
print(value, type(value))

value = "Python"
print(value, type(value))

value = [1, 2, 3]
print(value, type(value))

# ============================================================
# Task 8 — Equality, identity, and references
# ============================================================
a = [10, 20]
b = [10, 20]
c = a

# Before running the program, predict:
#
# a == b
# a is b
# a == c
# a is c
#
# Print all four results.
#
# Then print:
#   id(a)
#   id(b)
#   id(c)
#
# Finally:
#   append 30 to c
#   print a
#   print b
#   print c
#
# Explain to yourself why a changes but b does not.

# Write your code below:

a = [10, 20]
b = [10, 20]
c = a

print(a == b)
print(a is b)
print(a == c)
print(a is c)

print(id(a))
print(id(b))
print(id(c))

c.append(30)

print(a)
print(b)
print(c)

# ============================================================
# Task 9 — Function: is_even
# ============================================================
# Write a function:
#
#   is_even(number)
#
# It should return:
#   True  if number is even
#   False otherwise
#
# Then call it with:
#   4
#   7
#   0
#
# Print the returned results.
#
# IMPORTANT:
# The function must return the Boolean result.
# Do not print from inside the function.

# Write your code below:

def is_even(number):
    return number % 2 == 0


print(is_even(4))
print(is_even(7))
print(is_even(0))

# ============================================================
# Task 10 — Function: calculate_discount
# ============================================================
# Write a function:
#
#   calculate_discount(price, percent)
#
# It should return the final price after the discount.
#
# Formula:
# final_price = price - price * percent / 100
#
# Test it with:
#   calculate_discount(1000, 15)
#   calculate_discount(250, 20)
#
# Print each returned result.

# Write your code below:

def calculate_discount(price, percent):
    final_price = price - price * percent / 100
    return final_price


print(calculate_discount(1000, 15))
print(calculate_discount(250, 20))

# ============================================================
# Task 11 — return versus print
# ============================================================
# The function below is not useful if later code needs
# to reuse the calculated value:
#
# def rectangle_area(width, height):
#     print(width * height)
#
# Rewrite it so that it RETURNS the area.
#
# Then:
#   store the result for width=5, height=4
#   print the result
#   calculate result * 2 and print it
#
# Goal:
# Demonstrate why return is different from print.

# Write your code below:

def rectangle_area(width, height):
    return width * height


result = rectangle_area(5, 4)

print(result)
print(result * 2)

# ============================================================
# Task 12 — Function returning multiple values
# ============================================================
# Write a function:
#
#   min_max(numbers)
#
# It receives a list of numbers.
#
# Use loops and conditions to find:
#   the minimum value
#   the maximum value
#
# Return both values.
#
# Do NOT use:
#   min()
#   max()
#
# Test with:
values = [7, 2, 9, -1, 5, 12, 3]
#
# Unpack the result into:
#   smallest
#   largest
#
# Then print them.

# Write your code below:
def min_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

    return smallest, largest

smallest, largest = min_max(values)

print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
# ============================================================
# Task 13 — Integrated task: validated average
# ============================================================
# Write a function:
#
#   average(total, count)
#
# Rules:
#   if count == 0:
#       return None
#   otherwise:
#       return total / count
#
# Then write a loop that asks the user for count until
# the user enters a value >= 0.
#
# Ask once for total.
#
# Call average(total, count).
#
# If the returned result is None:
#   print "Cannot calculate average"
#
# Otherwise:
#   print the average with 2 decimal places.
#
# Required:
# Use:
#   function
#   while loop
#   condition
#   return
#   is None

# Write your code below:

def average(total, count):
    if count == 0:
        return None
    return total / count


while True:
    count = int(input("Enter count: "))
    if count >= 0:
        break

total = float(input("Enter total: "))
result = average(total, count)

if result is None:
    print("Cannot calculate average")
else:
    print(f"Average: {result:.2f}")

# ============================================================
# BONUS Task 14 — Guess the number
# ============================================================
# Use:
# secret_number = 37
#
# Repeatedly ask the user to guess the number.
#
# Print:
#   Too low
#   Too high
#   Correct
#
# Stop only when the guess is correct.
#
# Also count how many attempts were needed.
#
# Required:
# Use a while loop.

# Write your code below:


# ============================================================
# BONUS Task 15 — Function-based number statistics
# ============================================================
# Write a function:
#
#   number_statistics(numbers)
#
# It should use a loop to count:
#   positive numbers
#   negative numbers
#   zeros
#
# Return all three counts.
#
# Test with:
# data = [3, -1, 0, 8, -5, 0, 2, -9]
#
# Print:
#   Positive: ...
#   Negative: ...
#   Zero: ...
#
# Do not use list comprehensions.

# Write your code below:
