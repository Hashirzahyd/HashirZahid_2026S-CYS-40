# LAB TASK 09: Define a function average(*numbers) that calculates the average of multiple numbers.

def average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(average(1, 5, 9, 17))
