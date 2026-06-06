for i in range(1, 4):
    for j in range(2, 4):
        print(i, "and", j)

for i in range(1, 10):
    for j in range(i):
        print("*", end="")
    print()

rows = 10
for i in range(rows):
    sp = rows - i - 1
    print(" " * sp + "*" * (2*i + 1))
