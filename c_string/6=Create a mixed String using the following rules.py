a = "Abc"
b = "Xyz"

a1 = len(a)
b1 = len(b)
length = a1 if a1 > b1 else b1
result = ""

b = b[::-1]

for i in range(length):
    if i < a1:
        result = result + a1[i]
    if i < b1:
        result = result + b1[i]

print(result)
