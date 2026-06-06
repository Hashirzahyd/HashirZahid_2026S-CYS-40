# LAB TASK 05: Calculate semester GPA using grade points and credit hours via a user-defined function.

def calculate_gpa(subjects):
    total_points = 0
    total_credit = 0
    for i in range(subjects):
        gp = float(input("Enter grade point: "))
        ch = int(input("Enter credit hours: "))
        total_points = total_points + (gp * ch)
        total_credit = total_credit + ch
    gpa = total_points / total_credit
    return gpa

sub = int(input("Enter number of subjects: "))
result = calculate_gpa(sub)
print("Semester GPA =", result)
