n1, n2 = 0, 1
print("Fibonacci sequence:")

for i in range(10):
    print(n1, end="  ")
    res = n1 + n2

    n1 = n2
    n2 = res