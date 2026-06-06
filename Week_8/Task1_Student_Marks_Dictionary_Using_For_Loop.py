marks = int(input("Enter your marks: "))
total = int(input("Enter total marks: "))
if total <= 0 or total > 300:
    print("enter valid numbers")
elif marks > total:
    print("enter valid numbers")
else:
    per = (marks / total) * 100
    print(per)
    if per >= 90:
        print("A+")
    elif per >= 85:
        print("A-")
    elif per >= 80:
        print("B+")
    elif per >= 75:
        print("B-")
    elif per >= 70:
        print("C+")
    elif per >= 65:
        print("C-")
    elif per >= 60:
        print("F")

info = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    m = int(input("Enter student marks: "))
    info[name] = m
print(info)
