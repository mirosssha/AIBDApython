
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
age = int(input("Enter your age: "))
# TODO:
# Print:
# Hello, <name>!
# Next year you will be <age + 1> years old.
print(f"Hello, {name}!")
print(f"Next year you will be {age + 1} years old.")




# ============================================================
# Task 2 — Rectangle
# ============================================================

print("Task 2 — Rectangle")

# TODO:
# Ask the user to enter width and height.

width = 0.0
height = 0.0
width = float(input("width: "))
height = float(input("height: "))
# TODO:
# Calculate the area.

area = 0.0
area = width * height
# TODO:
# Calculate the perimeter.

perimeter = 0.0
perimeter = 2 * (width + height)

# TODO:
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")


# ============================================================
# Task 3 — Temperature Converter
# ============================================================

print("Task 3 — Temperature Converter")

# Formula:
# Fahrenheit = Celsius * 9 / 5 + 32

# TODO:
# Read Celsius temperature.

celsius = 0.0
celsius = float(input("Enter temperature in celsius: "))
# TODO:
# Calculate Fahrenheit temperature.

fahrenheit = 0.0
fahrenheit = celsius * 9 / 5 + 32
# TODO:
# Print the result.


print(f"Temperature in fahrenheit: {fahrenheit}")

# ============================================================
# Task 4 — Purchase Calculator
# ============================================================

print("Task 4 — Purchase Calculator")

# TODO:
# Ask for the number of items.

quantity = 0
quantity = int(input("Enter number of items: "))
# TODO:
# Ask for the price of one item.

price = 0.0
price = float(input("Enter price of an item: "))

# TODO:
# Calculate the total price.

total_price = 0.0
total_price = quantity * price
# TODO:
# Apply a 10% discount.

discounted_price = 0.0
discounted_price = total_price * 0.9
# TODO:
# Print both results.


print(f"Price before discount: {total_price:.2f}")
print(f"Price with the discount: {discounted_price:.2f}")


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

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)