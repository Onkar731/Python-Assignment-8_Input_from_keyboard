"""
Write a python script which takes the radius from the user and display area of the circle
"""

# taking radius from the user
# radius may be of type float thus, we uses a builtins conversion method called
# "float()" function which converts str into float

radius = float(input("Enter radius of the circle : "))

# calculating area of the circle - formula - pie*r*r
area = 3.14*radius*radius

# printing area of the circle
print("Area of the circle is", area)

# printing with format specifier
print("Area of the circle is %.2f" %(area))