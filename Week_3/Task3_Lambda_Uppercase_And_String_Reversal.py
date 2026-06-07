# LAB TASK 03: Convert a string to uppercase using a lambda, then reverse it using a UDF named invert.

upper = lambda s: s.upper()

text = input("Enter a string: ")
up = upper(text)

def invert(word):
    print(word[::-1])

invert(up)
