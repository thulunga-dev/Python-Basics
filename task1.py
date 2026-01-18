"""
Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
    o	Addition
    o	Subtraction
    o	Multiplication
    o	Division
"""

# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = float(num1/num2)

# Handle division by zero
if num2 !=0:
    division = num1/num2
else:
    division = "Undifined (division by zero)"

#Display the results
print(f"Addition : {addition}")
print(f"Substaction: {subtraction}")
print(f"Multiplication : {multiplication}")
print(f"Division: {division}")