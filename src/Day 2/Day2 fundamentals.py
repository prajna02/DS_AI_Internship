# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 11:24:08 2026

@author: DELL
"""

#Variables

age = 23
name = "Pruthvi"
height = 5.8
is_student = True
print("Age:", age)
print("Name:", name)
print("Height:", height)
print("Student:", is_student)
print()

#Simple calculator program
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    print("Result:", a + b)

elif choice == '2':
    print("Result:", a - b)

elif choice == '3':
    print("Result:", a * b)

elif choice == '4':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("Invalid choice")
print()   
    
# Concatenation program
name = input("Enter your name: ")
print("Welcome " +name+ "!")
print()

#fstring program

name = input("Enter your name:")
age = input("Enter your age:")
message = f"My name is {name}, Iam {age} year old"
print(message)