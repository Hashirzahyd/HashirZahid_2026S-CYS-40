def greet():
    print("Hello!")
greet()

def myInfo():
    name = "Hashir"
    age = 19
    dept = "Computer Engineering"
    roll = "2026(S)-CYS-40"
    print(name, age, dept, roll)

myInfo()

def add(a, b, c):
    return a + b + c

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print(add(n1, n2, 5))

print(len("Hashir"))
print(max(10, 25))
print(min(10, 25))

x = float(input("Enter a value: "))
print(type(x))

def showInfo(name, roll):
    print("Name:", name)
    print("Roll:", roll)

showInfo("Hashir", "2026(S)-CYS-40")
