"""
Write a python script to calculate square of a number. Number is entered by the user
"""

# taking input from the user
num = int(input("Enter a number : "))

# calculating square using exponent arithmetic operator 
sq = num**2

# printing square
print("Square of", num, "is", sq)
print("Square of %d is %d" %(num, sq))