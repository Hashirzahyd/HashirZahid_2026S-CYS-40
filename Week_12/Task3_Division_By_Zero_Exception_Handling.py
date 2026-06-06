num = int(input("Enter a number: "))
try:
    b = num / 0
    print(f"The result of dividing {num} by zero is {b}")
except Exception as e:
    print(f"Error: {e}")
