def test_factorial():
    result = 1
    for i in range(1, 6):
        result = result * i
    assert result == 120

def test_fibonacci():
    def fab(n):
        if n == 0 or n == 1:
            return n
        return fab(n-1) + fab(n-2)
    assert fab(6) == 8

test_factorial()
test_fibonacci()
print("All tests passed.")
