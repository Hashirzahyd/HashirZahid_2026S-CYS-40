student_dict = {}
total_students = int(input("Enter number of students: "))

for i in range(total_students):
    name = input("\nEnter student name: ")
    while True:
        total_marks = int(input("Enter total marks: "))
        if total_marks <= 0:
            print("Total marks must be greater than 0")
        else:
            break
    while True:
        ob_marks = int(input("Enter obtained marks: "))
        if ob_marks > total_marks:
            print("Obtained marks cannot be greater than total marks")
        else:
            break
    result = (ob_marks / total_marks) * 100

    if result >= 90:
        grade = "A+"
    elif result >= 85:
        grade = "A"
    elif result >= 80:
        grade = "B+"
    elif result >= 75:
        grade = "B"
    elif result >= 70:
        grade = "C+"
    elif result >= 65:
        grade = "C"
    elif result >= 60:
        grade = "D"
    else:
        grade = "F"
    student_dict[name] = {
        "Obtained Marks": ob_marks,
        "Total Marks": total_marks,
        "Percentage": result,
        "Grade": grade
    }
print("\nStudent Records:")
for student, details in student_dict.items():
    print(student, ":", details)