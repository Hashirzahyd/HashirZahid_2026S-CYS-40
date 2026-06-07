for i in range(1, 4):
    for j in range(2, 5):
        print(i, "and", j)

for i in range(1, 8):
    print("*" * i)

sz = 8
for i in range(sz):
    print(" " * (sz - i - 1) + "*" * (2*i + 1))
