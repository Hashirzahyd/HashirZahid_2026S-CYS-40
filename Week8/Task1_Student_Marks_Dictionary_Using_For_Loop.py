data = {}

got = int(input("Enter marks obtained: "))
out_of = int(input("Enter total marks: "))
if out_of <= 0 or out_of > 300:
    print("enter valid numbers")
elif got > out_of:
    print("enter valid numbers")
else:
    perc = (got / out_of) * 100
    print("Percentage =", perc)
    if perc >= 90:
        print("A+")
    elif perc >= 85:
        print("A-")
    elif perc >= 80:
        print("B+")
    elif perc >= 75:
        print("B-")
    elif perc >= 70:
        print("C+")
    elif perc >= 65:
        print("C-")
    else:
        print("F")

num = int(input("Enter number of students: "))
for x in range(num):
    sname = input("Enter name: ")
    smarks = int(input("Enter marks: "))
    data[sname] = smarks

print(data)
