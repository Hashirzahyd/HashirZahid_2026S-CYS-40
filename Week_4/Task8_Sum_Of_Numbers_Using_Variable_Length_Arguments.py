# LAB TASK 08: Define a function total() using variable length arguments that sums numbers entered by user.

def total(sum):
    sum = 0
    for x in range(0, 5):
        num = int(input("enter number:"))
        sum = sum + num
    return sum

num = 0
print(total(num))
