num = int(input("Enter a number: "))
try:
    ans = num / 0
    print("Result:", ans)
except ZeroDivisionError as e:
    print("Cannot divide by zero!")
    print("Error:", e)
