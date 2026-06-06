# LAB TASK 02: Find the larger of two numbers using a lambda, then print its multiplication table using a UDF.

large = lambda a, b: a if a > b else b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
big = large(num1, num2)

def table(n):
    limit = int(input("Enter range of table: "))
    for i in range(1, limit + 1):
        print(n, "x", i, "=", n * i)

table(big)
