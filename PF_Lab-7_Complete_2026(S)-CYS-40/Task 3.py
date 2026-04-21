#Task-03: Condition on obtained marks and total marks
obtained_marks = int(input("Enter your marks: "))
total_marks = int(input("Enter total marks: "))
if total_marks <= 0 or total_marks > 300:
    print("enter valid numbers")
elif obtained_marks > total_marks:
    print("enter valid numbers")
else:
    result = (obtained_marks / total_marks) * 100
    print(result)
    if result >= 90:
        print("A+")
    elif result >= 85:
        print("A-")
    elif result >= 80:
        print("B+")
    elif result >= 75:
        print("B-")
    elif result >= 70:
        print("C+")
    elif result >= 65:
        print("C-")
    elif result >= 60:
        print("F")