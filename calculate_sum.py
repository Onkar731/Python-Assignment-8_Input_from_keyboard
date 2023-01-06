"""
Write a python script to take input two numbers from the user,
then calculate their sum and display the result
"""

# taking two number input from the user
# input() function returns the input value in the "str" format, so we need to convert
# it into particular format using builtins conversion methods
# ex. int(), bool(), float(), complex(), str() etc.

num1, num2 = int(input("Enter two numbers : ")), int(input())

# adding two numbers
sum = num1 + num2

# printing sum
print("Sum of", num1, "and", num2, "is", sum)