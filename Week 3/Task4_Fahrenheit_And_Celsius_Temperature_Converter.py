# LAB TASK 04: Convert temperature between Fahrenheit and Celsius using user-defined functions.
# Formula: C = (F - 32) * 5/9    F = (C * 9/5) + 32

def f_to_c(f):
    c = (f - 32) * 5 / 9
    return c

def c_to_f(c):
    f = (c * 9 / 5) + 32
    return f

choice = int(input("1. F to C\n2. C to F\nEnter choice: "))
if choice == 1:
    f = float(input("Enter Fahrenheit: "))
    print("Celsius =", f_to_c(f))
else:
    c = float(input("Enter Celsius: "))
    print("Fahrenheit =", c_to_f(c))
