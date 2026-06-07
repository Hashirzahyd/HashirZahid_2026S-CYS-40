num = int(input("Enter total number of students: "))
i = 1
while i <= num:
    nm = input("Enter student name: ")
    rn = int(input("Enter roll number: "))
    got = int(input("Enter obtained marks: "))
    tot = int(input("Enter total marks: "))
    if tot <= 0 or tot > 300:
        print("enter valid numbers")
    elif got > tot:
        print("enter valid numbers")
    else:
        perc = (got / tot) * 100
        print("Percentage:", perc)
        if perc >= 90:
            print("Grade: A+")
        elif perc >= 85:
            print("Grade: A-")
        elif perc >= 80:
            print("Grade: B+")
        elif perc >= 75:
            print("Grade: B-")
        elif perc >= 70:
            print("Grade: C+")
        elif perc >= 65:
            print("Grade: C-")
        else:
            print("Grade: F")
    i += 1
