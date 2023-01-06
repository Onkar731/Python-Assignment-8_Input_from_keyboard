"""
Write a python script which takes a character from the user and display its unicode
"""

# taking character as an input from the user
char = input("Enter a character : ")

# printing unicode of the character using builtins method - "ord()"
print("Unicode of", char, "is", ord(char))
print("Unicode of %s is %d" %(char, ord(char)))