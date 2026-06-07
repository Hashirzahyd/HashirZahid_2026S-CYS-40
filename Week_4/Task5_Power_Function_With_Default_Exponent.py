# LAB TASK 05: Define a function power(base, exponent=2) using a default argument for the exponent.

def power(base, exponent=2):
    result = base ** exponent
    return result

print(power(5))
print(power(5, 3))
