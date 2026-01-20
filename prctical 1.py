Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello")
hello
>>> # Simple Interest Calculation

# Input values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Output result
print("Simple Interest =", simple_interest)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Maximum number is:", max(a, b))
for i in range(1, 6):
    print(i)
1
2
3
4
5
# Input string
string = input("Enter a string: ")

# Find the length
length = len(string)

# Output the length
print("Length of the string is:", length)
Length of the string is: 13
# Printing a welcome message
print("Welcome to Python!")
Welcome to Python!
# Input string
string = input("Enter a string: ")

# Print the first character
print("The first character is:", string[0])
The first character is: H
# Input string
string = input("Enter a string: ")

# Print the last character
print("The last character is:", string[-1])
The last character is: o
# Input number
num = float(input("Enter a number: "))

# Check if the number is positive or negative
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
Enter a number: 5
The number is positive.
Enter a number: -3
The number is negative.
Enter a number: 0
The number is zero.
# Input three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Add the numbers
sum_of_numbers = num1 + num2 + num3

# Output the result
print("The sum of the three numbers is:", sum_of_numbers)
Enter the first number: 5
Enter the second number: 7
Enter the third number: 3
Enter the first number: 5
Enter the second number: 7
Enter the third number: 3

SyntaxError: multiple statements found while compiling a single statement
>>> The sum of the three numbers is: 15.0
# Taking input from the user
num = input("Enter a number: ")

# Output the entered number
print("You entered:", num)
You entered: 25
