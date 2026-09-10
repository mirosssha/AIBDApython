
"""
Lab 01 — Python Basics

Complete all tasks below.

Topics:
- variables
- basic data types
- input and output
- type conversion
- arithmetic operators
- basic PEP 8
"""


# ============================================================
# Task 1 — Personal Information
# ============================================================

print("Task 1 — Personal Information")

# TODO:
# Ask the user to enter their name.

name = input("Enter your name: ")

# TODO:
# Ask the user to enter their age.
# Remember that input() returns a string.

age = 0

# TODO:
# Print:
# Hello, <name>!
# Next year you will be <age + 1> years old.


print()


# ============================================================
# Task 2 — Rectangle
# ============================================================

print("Task 2 — Rectangle")

# TODO:
# Ask the user to enter width and height.

width = 0.0
height = 0.0

# TODO:
# Calculate the area.

area = 0.0

# TODO:
# Calculate the perimeter.

perimeter = 0.0

# TODO:
# Print the results.


print()


# ============================================================
# Task 3 — Temperature Converter
# ============================================================

print("Task 3 — Temperature Converter")

# Formula:
# Fahrenheit = Celsius * 9 / 5 + 32

# TODO:
# Read Celsius temperature.

celsius = 0.0

# TODO:
# Calculate Fahrenheit temperature.

fahrenheit = 0.0

# TODO:
# Print the result.


print()


# ============================================================
# Task 4 — Purchase Calculator
# ============================================================

print("Task 4 — Purchase Calculator")

# TODO:
# Ask for the number of items.

quantity = 0

# TODO:
# Ask for the price of one item.

price = 0.0

# TODO:
# Calculate the total price.

total_price = 0.0

# TODO:
# Apply a 10% discount.

discounted_price = 0.0

# TODO:
# Print both results.


print()


# ============================================================
# Task 5 — Arithmetic Operators
# ============================================================

print("Task 5 — Arithmetic Operators")

a = 17
b = 5

# TODO:
# Print the result of each operation:
#
# a + b
# a - b
# a * b
# a / b
# a // b
# a % b
# a ** b



# ============================================================
# Task 6 — Data Types
# ============================================================

print("Task 6 — Data Types")

integer_value = 42
float_value = 3.14
complex_value = 2 + 3j
text_value = "Python"
boolean_value = True

# TODO:
# Use type() to print the type of every variable above.
#
# Example:
# print(type(integer_value))


print()


# ============================================================
# Task 7 — Comparisons and Boolean Logic
# ============================================================

print("Task 7 — Comparisons and Boolean Logic")

age = 22
is_master_student = True

# TODO:
# Print the result of the following expressions:
#
# age >= 18
# age < 30
# age == 22
# age != 25
#
# age >= 18 and is_master_student
# age < 18 or is_master_student
# not is_master_student
#
# Predict each result before running the program.


print()


# ============================================================
# Task 8 — Python Collections
# ============================================================

print("Task 8 — Python Collections")

# TODO:
# Create:
#
# 1. A list containing three programming languages.
# 2. A tuple containing three numbers.
# 3. A set containing several city names.
# 4. A dictionary describing a student with:
#       name
#       age
#       university

programming_languages = []
numbers = ()
cities = set()
student = {}

# TODO:
# Print all four variables.
#
# TODO:
# Use type() to print the type of each collection.


print()


# ============================================================
# Task 9 — Indexing and Slicing
# ============================================================

print("Task 9 — Indexing and Slicing")

numbers = [0, 1, 2, 3, 4, 5, 6, 7]

# TODO:
# Print the first element.

# TODO:
# Print the last element.

# TODO:
# Print elements from index 1 up to index 4.
#
# Expected:
# [1, 2, 3]

# TODO:
# Print every second element.
#
# Expected:
# [0, 2, 4, 6]


word = "Python"

# TODO:
# Print the first character.

# TODO:
# Print the last character.

# TODO:
# Print:
# Pyt


print()


# ============================================================
# Task 10 — Dictionaries and Membership
# ============================================================

print("Task 10 — Dictionaries and Membership")

student = {
    "name": "Anna",
    "age": 22,
    "city": "Novosibirsk",
}

# TODO:
# Print the student's name.

# TODO:
# Print the student's age.

# TODO:
# Check whether "age" exists in the dictionary.
# Print the result.

# TODO:
# Check whether "email" exists in the dictionary.
# Print the result.


numbers = [10, 20, 30, 40]

# TODO:
# Check whether 20 is in numbers.

# TODO:
# Check whether 50 is in numbers.


print()


# ============================================================
# Task 11 — Formatted Output
# ============================================================

print("Task 11 — Formatted Output")

# TODO:
# Ask the user to enter the radius of a circle.

radius = 0.0

# Use:
# area = 3.14159 * radius ** 2

area = 0.0

# TODO:
# Print the radius and area using an f-string.
#
# Example:
# Radius: 10.0
# Area: 314.16
#
# Print the area with exactly two digits after the decimal point.
#
# Hint:
# {value:.2f}


print()


# ============================================================
# Task 12 — Trip Cost Calculator
# ============================================================

print("Task 12 — Trip Cost Calculator")

# A car consumes a certain number of liters of fuel
# for every 100 kilometers.

# TODO:
# Ask the user to enter:
#
# distance in kilometers
# fuel consumption in liters per 100 km
# fuel price per liter

distance = 0.0
fuel_consumption = 0.0
fuel_price = 0.0

# TODO:
# Calculate how many liters of fuel are required.
#
# Formula:
# liters_needed = distance / 100 * fuel_consumption

liters_needed = 0.0

# TODO:
# Calculate the total cost of the trip.

trip_cost = 0.0

# TODO:
# Print something similar to:
#
# Distance: 450.0 km
# Fuel required: 36.00 liters
# Trip cost: 2160.00
#
# Use f-strings and two decimal places where appropriate.
