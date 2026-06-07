def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n_terms = int(input("Enter the number of terms in the Fibonacci series: "))
for i in range(n_terms):
    print(fibonacci(i),end=" ")