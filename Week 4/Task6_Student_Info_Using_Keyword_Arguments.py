# LAB TASK 06: Define a function student(n, a) that prints student name and age using keyword arguments.

def student(n, a):
    print(f"name:{n}")
    print(f"age:{a}")
    return

n = str(input("please enter your name:"))
a = int(input("please enter your age:"))
student(n, a)
