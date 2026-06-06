# CLI Based Student Record System
records = {}

def add_student():
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    records[name] = marks
    print("Student added.")

def view_students():
    if len(records) == 0:
        print("No records found.")
    else:
        for name, marks in records.items():
            print(name, ":", marks)

def delete_student():
    name = input("Enter name to delete: ")
    if name in records:
        del records[name]
        print("Deleted.")
    else:
        print("Student not found.")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")
    ch = input("Enter choice: ")
    if ch == "1":
        add_student()
    elif ch == "2":
        view_students()
    elif ch == "3":
        delete_student()
    elif ch == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
