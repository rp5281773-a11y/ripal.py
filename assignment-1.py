Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("hello wrold")
hello wrold
x=30
y=65
print(x+y)
95
# Ask the user for a number
num = int(input("Enter a number: "))

# Check if even or odd
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
Enter a number: 10
The number is even.

Enter a number: 7
The number is odd.
# Ask the user for a year
year = int(input("Enter a year: "))

# Check leap year conditions
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
Enter a year: 2000
2000 is a leap year.

Enter a year: 1900
1900 is not a leap year.

Enter a year: 2024
2024 is a leap year.
import math

print("The value of pi is:", math.pi)
The value of pi is: 3.141592653589793
# Store a constant value
PI = 3.14159
GRAVITY = 9.8
APP_NAME = "MyPythonApp"

# Print the constants
print("The value of PI is:", PI)
print("The value of GRAVITY is:", GRAVITY)
print("The name of the app is:", APP_NAME)
The value of PI is: 3.14159
The value of GRAVITY is: 9.8
The name of the app is: MyPythonApp
# Ask the user for a number
num = int(input("Enter a number: "))

# Method 1: Using multiplication
square1 = num * num
print("Square using multiplication:", square1)

# Method 2: Using exponentiation
square2 = num ** 2
print("Square using exponentiation:", square2)
Enter a number: 5
Square using multiplication: 25
Square using exponentiation: 25
print(f"The area of the circle is: {area:.2f}")
The area of the circle is: 78.54
# Store different values
num = 10
pi = 3.14
name = "Python"
is_active = True
items = [1, 2, 3]

# Check data types
print("Data type of num:", type(num))
print("Data type of pi:", type(pi))
print("Data type of name:", type(name))
print("Data type of is_active:", type(is_active))
print("Data type of items:", type(items))
Data type of num: <class 'int'>
Data type of pi: <class 'float'>
Data type of name: <class 'str'>
Data type of is_active: <class 'bool'>
Data type of items: <class 'list'>
import math

num = 25
print("Square root of", num, "is:", math.sqrt(num))
print("Value of pi is:", math.pi)
print("Cosine of 0 is:", math.cos(0))
Square root of 25 is: 5.0
Value of pi is: 3.141592653589793
Cosine of 0 is: 1.0
