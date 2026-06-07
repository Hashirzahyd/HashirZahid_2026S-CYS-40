marks = int(input("Enter your marks: "))
total = int(input("Enter total marks: "))
per = (marks / total) * 100
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
