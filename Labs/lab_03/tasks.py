"""
NSU Python — Lab 03
Conditions and for Loops

Complete Tasks 1–12.
Tasks 13–14 are optional bonus tasks.

Use only concepts covered in Lecture 03.
"""

# ============================================================
# Task 1 — Positive, negative, or zero
# ============================================================
# Ask the user to enter an integer.

# Print exactly one of:
#   Positive
#   Negative
#   Zero
#
# Example:
# Input: -7
# Output: Negative

# Write your code below:

# ============================================================
# Task 2 — Age category
# ============================================================
# Ask the user for their age.
#
# Print:
#   Child      -> age < 13
#   Teenager   -> 13–17
#   Adult      -> 18–64
#   Senior     -> 65 or older
#
# Test boundary values: 12, 13, 17, 18, 64, 65.

# Write your code below:


# ============================================================
# Task 3 — Grade classifier
# ============================================================
# Ask the user for a score.
#
# First check whether the score is between 0 and 100 inclusive.
#
# For a valid score:
#   A    -> 90–100
#   B    -> 75–89
#   C    -> 60–74
#   Fail -> below 60
#
# For an invalid score print:
#   Invalid score

# Write your code below:


# ============================================================
# Task 4 — Access decision
# ============================================================
# Ask the user for:
#   age
#   whether they have a ticket: yes/no
#
# A person may enter only if:
#   age >= 18 AND they have a ticket.
#
# Print one of:
#   Access granted
#   Ticket required
#   Must be 18 or older

# Write your code below:


# ============================================================
# Task 5 — Even numbers with range()
# ============================================================
# Print all even numbers from 2 through 30.
#
# Required:
# Use range(start, stop, step).

# Write your code below:


# ============================================================
# Task 6 — Sum of multiples of 3
# ============================================================
# Calculate and print the sum of all multiples of 3
# from 3 through 99.
#
# Required:
# Use a for loop and an accumulator.
#
# Expected result:
# 1683

# Write your code below:


# ============================================================
# Task 7 — Count number categories
# ============================================================
numbers = [4, -2, 0, 7, -5, 9, 0, -1, 8]

# Count how many values are:
#   positive
#   negative
#   zero
#
# Print all three counts.
# Do not manually count the values.

# Write your code below:


# ============================================================
# Task 8 — Count vowels
# ============================================================
# Ask the user to enter a word or short text.
# Count how many vowels it contains.
#
# Treat uppercase and lowercase equally.
# Vowels: a e i o u
#
# Example:
# Input: Artificial Intelligence
# Output: 10
#
# Hint:
# Iterate directly over the string.

# Write your code below:


# ============================================================
# Task 9 — Student results
# ============================================================
scores = [85, 42, 67, 91, 58, 73, 100, 39]

# Count:
#   passed students: score >= 60
#   failed students: score < 60
#
# Also print the average score.
#
# Required:
# Use a loop to calculate the total.
#
# Expected:
# Passed: 5
# Failed: 3
# Average: 69.38

# Write your code below:


# ============================================================
# Task 10 — Search and stop
# ============================================================
names = ["Anna", "Boris", "Sasha", "Maria", "Oleg", "Dina"]

# Ask the user for a name.
# Search the list using a for loop.
#
# If found:
#   print "Found"
#   stop immediately with break
#
# If not found:
#   print "Not found"
#
# Do not use:
#   if target in names
#
# Hint:
# A Boolean variable such as found = False can help.

# Write your code below:


# ============================================================
# Task 11 — Skip invalid scores
# ============================================================
raw_scores = [78, -5, 91, 120, 66, 0, 88, 101, 54]

# Valid scores are from 0 to 100 inclusive.
#
# Use continue to skip invalid scores.
# For valid scores:
#   print each valid score
#   calculate the average of valid scores
#
# At the end print:
#   Valid scores: ...
#   Average: ...
#
# Required:
# Use continue.

# Write your code below:


# ============================================================
# Task 12 — Dictionary iteration
# ============================================================
student_scores = {
    "Anna": 92,
    "Boris": 58,
    "Sasha": 76,
    "Maria": 49,
    "Oleg": 84,
}

# Iterate using .items().
#
# Print:
#   Anna: Pass
#   Boris: Fail
#   ...
#
# Score >= 60 means Pass.
# Then print how many students passed.

# Write your code below:


# ============================================================
# BONUS Task 13 — FizzBuzz
# ============================================================
# Print numbers 1 through 30.
#
# If divisible by both 3 and 5 -> FizzBuzz
# If divisible only by 3       -> Fizz
# If divisible only by 5       -> Buzz
# Otherwise print the number.
#
# Hint:
# Check the most specific condition first.

# Write your code below:


# ============================================================
# BONUS Task 14 — Limited login attempts
# ============================================================
correct_pin = "4821"

# Give the user at most 3 attempts to enter the PIN.
#
# Use:
#   for
#   range()
#   break
#
# Correct PIN:
#   Access granted
#
# Three wrong attempts:
#   Access denied
#
# Do NOT use a while loop.

# Write your code below:
# ============================================================
# EXTRA Task 15 — Largest of three numbers
# ============================================================
# Ask the user to enter three integers.
#
# Print the largest number.
#
# Do NOT use:
#   max()
#
# Example:
# Input:
# 12
# 7
# 19
#
# Output:
# Largest: 19
#
# Think carefully about equal values.

# Write your code below:


# ============================================================
# EXTRA Task 16 — Number statistics
# ============================================================
numbers = [12, -4, 7, 0, 15, -9, 8, -2, 0, 21]

# Using one for loop, calculate:
#   number of positive values
#   number of negative values
#   number of zeros
#   sum of positive values
#   sum of negative values
#
# Expected:
# Positive: 5
# Negative: 3
# Zero: 2
# Positive sum: 63
# Negative sum: -15
#
# Do not manually calculate the values.

# Write your code below:


# ============================================================
# EXTRA Task 17 — Highest and lowest score
# ============================================================
scores = [71, 85, 42, 96, 58, 83, 67, 91]

# Find the highest and lowest scores using a for loop.
#
# Do NOT use:
#   max()
#   min()
#   sorted()
#
# Hint:
# Start with:
# highest = scores[0]
# lowest = scores[0]
#
# Expected:
# Highest: 96
# Lowest: 42

# Write your code below:


# ============================================================
# EXTRA Task 18 — Temperature analysis
# ============================================================
temperatures = [12, 18, 25, 31, 7, 22, 35, 16, 29, 4]

# Classify every temperature:
#
#   Cold -> below 10
#   Mild -> 10–19
#   Warm -> 20–29
#   Hot  -> 30 or above
#
# Example output:
# 12: Mild
# 18: Mild
# 25: Warm
# ...
#
# After processing all temperatures, print how many
# temperatures belong to each category.

# Write your code below:


# ============================================================
# EXTRA Task 19 — Running balance
# ============================================================
transactions = [500, -120, -80, 250, -700, 300, -200]

# The starting balance is:
balance = 1000

# Process every transaction in order.
#
# Positive numbers mean money added.
# Negative numbers mean money spent.
#
# After each transaction print the current balance.
#
# Example:
# Transaction: 500
# Balance: 1500
#
# At the end print:
# Final balance: ...
#
# Also count how many transactions were:
#   deposits
#   withdrawals

# Write your code below:


# ============================================================
# EXTRA Task 20 — Find first number divisible by 7 and 11
# ============================================================
# Search numbers from 1 through 500.
#
# Find the FIRST number that is divisible by both 7 and 11.
#
# Print the number and immediately stop the loop.
#
# Required:
#   for
#   range()
#   break
#
# Expected:
# 77

# Write your code below:


# ============================================================
# EXTRA Task 21 — Limited number guessing
# ============================================================
secret_number = 37

# Give the user at most 5 attempts to guess the secret number.
#
# After each incorrect guess:
#
#   if guess < secret_number:
#       print "Too low"
#
#   if guess > secret_number:
#       print "Too high"
#
# Correct guess:
#   print "Correct"
#   stop immediately
#
# If all 5 attempts are used without success:
#   print "Out of attempts"
#
# Required:
#   for
#   range()
#   if / elif / else
#   break
#
# Do NOT use while.

# Write your code below:


# ============================================================
# EXTRA Task 22 — Count increases
# ============================================================
values = [10, 14, 13, 18, 22, 20, 25, 25, 30]

# Count how many times a value is greater than
# the value immediately before it.
#
# Comparisons:
# 10 -> 14   increase
# 14 -> 13   no
# 13 -> 18   increase
# ...
#
# Expected:
# Increases: 5
#
# Hint:
# Start looping from index 1:
#
# for i in range(1, len(values)):
#
# Compare:
# values[i]
# values[i - 1]

# Write your code below:


# ============================================================
# EXTRA Task 23 — Prime number check
# ============================================================
# Ask the user to enter an integer greater than 1.
#
# Determine whether the number is prime.
#
# A prime number is divisible only by 1 and itself.
#
# Examples:
# 7  -> Prime
# 12 -> Not prime
# 29 -> Prime
#
# Required:
# Use a for loop to test divisors.
#
# Do NOT use any library.
#
# Hint:
# Try dividing by numbers from 2 up to number - 1.
# If one divides exactly, the number is not prime.

# Write your code below:


# ============================================================
# EXTRA Task 24 — Multiplication table
# ============================================================
# Print a multiplication table from 1 to 5.
#
# Expected format:
#
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25
#
# Required:
# Use nested for loops.
#
# Hint:
#
# for row in range(...):
#     for column in range(...):
#         ...

# Write your code below:

# ============================================================
# EXTRA Task 25 — Second largest value
# ============================================================
numbers = [12, 7, 19, 3, 19, 14, 8]

# Find the second largest DISTINCT value.
#
# Expected:
# Second largest: 14
#
# Do NOT use:
#   sorted()
#   max()
#
# Hint:
# Keep track of:
#   largest
#   second_largest
#
# Be careful with duplicate values.

# Write your code below:


# ============================================================
# EXTRA Task 26 — Count consecutive positives
# ============================================================
numbers = [2, 5, 7, -1, 3, 4, 8, 9, -2, 6]

# Find the longest sequence of consecutive positive numbers.
#
# Sequences:
# 2, 5, 7       -> length 3
# 3, 4, 8, 9    -> length 4
# 6             -> length 1
#
# Expected:
# Longest positive sequence: 4
#
# Hint:
# Use:
#   current_count
#   longest_count

# Write your code below:


# ============================================================
# EXTRA Task 27 — Number frequency
# ============================================================
numbers = [4, 2, 7, 4, 8, 4, 2, 9, 4, 1]

# Ask the user for a number.
#
# Count how many times that number occurs in the list.
#
# Example:
# Input: 4
# Output:
# Occurrences: 4
#
# Do NOT use:
#   .count()

# Write your code below:


# ============================================================
# EXTRA Task 28 — Simple password checker
# ============================================================
password = input("Enter password: ")

# A valid password must:
#   contain at least 8 characters
#   contain at least one digit
#   contain at least one uppercase English letter
#
# Print:
#   Valid password
# or
#   Invalid password
#
# Do NOT use:
#   any()
#
# Hint:
# You can iterate over the password.
#
# Useful strings:
digits = "0123456789"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Write your code below:


# ============================================================
# EXTRA Task 29 — Local maximum
# ============================================================
values = [3, 7, 4, 8, 5, 9, 2, 6, 1]

# A value is a local maximum if it is greater than
# both the value before it and the value after it.
#
# Example:
# 3, 7, 4
#    ^
# 7 is a local maximum.
#
# Find and print all local maxima.
#
# Do not check the first or last element.
#
# Expected:
# 7
# 8
# 9
# 6
#
# Hint:
# Use indexes:
# values[i - 1]
# values[i]
# values[i + 1]

# Write your code below:


# ============================================================
# EXTRA Task 30 — Pair with target sum
# ============================================================
numbers = [2, 4, 7, 11, 15, 3]
target = 10

# Find two DIFFERENT elements whose sum is equal to target.
#
# Expected:
# 7 + 3 = 10
#
# Required:
# Use nested for loops.
#
# Stop when the first valid pair is found.
#
# Do NOT use:
#   set()
#
# Hint:
#
# for i in range(...):
#     for j in range(...):

# Write your code below:


# ============================================================
# EXTRA Task 31 — Grade distribution
# ============================================================
scores = [95, 82, 67, 73, 58, 91, 49, 88, 76, 100, 61]

# Count how many students received:
#
# A    -> 90–100
# B    -> 75–89
# C    -> 60–74
# Fail -> below 60
#
# Print:
# A: ...
# B: ...
# C: ...
# Fail: ...
#
# Then determine which category contains the most students.
#
# Example:
# Most common: B

# Write your code below:


# ============================================================
# EXTRA Task 32 — Find duplicate values
# ============================================================
numbers = [4, 7, 2, 4, 9, 7, 5, 2]

# Print every value that appears more than once.
#
# Expected:
# 4
# 7
# 2
#
# Do not print the same duplicate more than once.
#
# For this task, try solving it with nested loops.
#
# Do NOT use:
#   set()
#   .count()

# Write your code below:


# ============================================================
# EXTRA Task 33 — Closest number to target
# ============================================================
numbers = [5, 17, 23, 41, 8, 31]
target = 20

# Find the number closest to the target.
#
# Expected:
# Closest: 17
#
# You may use:
# abs()
#
# Do NOT use:
# min()

# Write your code below:


# ============================================================
# EXTRA Task 34 — Detect first repeated value
# ============================================================
numbers = [5, 3, 8, 2, 3, 9, 5]

# Find the first value that appears for the second time.
#
# Reading from left to right:
#
# 5 -> first time
# 3 -> first time
# 8 -> first time
# 2 -> first time
# 3 -> repeated
#
# Expected:
# First repeated: 3
#
# Stop searching immediately after finding it.
#
# Required:
# Use break.

# Write your code below:


# ============================================================
# EXTRA Task 35 — Prime numbers from 2 to 100
# ============================================================
# Print every prime number from 2 through 100.
#
# Expected beginning:
# 2
# 3
# 5
# 7
# 11
# ...
#
# Required:
# Use nested for loops.
#
# Hint:
# For each number, test whether another number divides it.
#
# Do NOT use external libraries.

# Write your code below:


# ============================================================
# EXTRA Task 36 — Number triangle
# ============================================================
# Print:
#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
#
# Required:
# Use nested for loops.

# Write your code below:
