for i in range(1, 11):
    for j in range(1, 5):
        print(i*j, end="\t")
    print()

for i in range(1, 4):
    for j in range(2, 4):
        print(i, "and", j)

for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

rows = 5
for i in range(rows):
    sp = rows - i - 1
    print(" " * sp + "*" * (2*i + 1))

rows = 5
for i in range(rows):
    for s in range(rows - i - 1):
        print("  ", end="")
    for st in range(2*i + 1):
        print("*", end=" ")
    print()
