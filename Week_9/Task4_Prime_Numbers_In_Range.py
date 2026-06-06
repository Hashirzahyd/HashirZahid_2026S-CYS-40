start = int(input("Enter start: "))
end = int(input("Enter end: "))
total = 0
for number in range(start, end):
    if number > 1:
        prime = True
        for x in range(2, number):
            if number % x == 0:
                prime = False
                break
        if prime:
            print(number)
            total = total + number
print("Sum is:", total)
