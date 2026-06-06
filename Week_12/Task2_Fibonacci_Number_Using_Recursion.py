def fab(n):
    if n == 0 or n == 1:
        return n
    else:
        return fab(n-1) + fab(n-2)

num = int(input("Enter a number: "))
result = fab(num)
print(f"The {num}th Fibonacci number is: {result}")
