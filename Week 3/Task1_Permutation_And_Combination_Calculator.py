# LAB TASK 01: Calculate Permutation and Combination of n and r using user-defined functions.
# Formula: P(n,r) = n! / (n-r)!   C(n,r) = n! / (r! x (n-r)!)

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def permutation(n, r):
    p = factorial(n) / factorial(n - r)
    return p

def combination(n, r):
    c = factorial(n) / (factorial(r) * factorial(n - r))
    return c

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))
p = permutation(n, r)
c = combination(n, r)
print("Permutation =", p)
print("Combination =", c)
