# LAB TASK 04: Write a program that asks the user what kind of password they want and generates it.
import random
import string
length = int(input("Enter length: "))
characters = ""
upper = input("Uppercase? y/n: ")
lower = input("Lowercase? y/n: ")
digit = input("Digits? y/n: ")
special = input("Special? y/n: ")
if upper == "y":
    characters = characters + string.ascii_uppercase
if lower == "y":
    characters = characters + string.ascii_lowercase
if digit == "y":
    characters = characters + string.digits
if special == "y":
    characters = characters + string.punctuation
password = ""
for p in range(length):
    password = password + random.choice(characters)
print("Password is:", password)
