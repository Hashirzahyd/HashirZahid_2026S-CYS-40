# LAB TASK 07: Define a function maximum(a, b, c) that returns the largest of three numbers.

def maximum(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

number1 = int(input("please enter number1:"))
number2 = int(input("please enter number2:"))
number3 = int(input("please enter number3:"))
print(maximum(number1, number2, number3))
