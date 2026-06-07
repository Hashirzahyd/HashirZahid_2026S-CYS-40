# LAB TASK 01: Write a program that convert a binary number into its decimal equivalent.
binary = input("Enter a binary number: ")
decimal = 0
power = 0
for digit in reversed(binary):
    decimal = decimal + int(digit) * (2 ** power)
    power = power + 1
print("Answer is:", decimal)
