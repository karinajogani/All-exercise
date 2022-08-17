from ast import If


str = "Emma25 is Data scientist50 and AI Expert"
print(str)
res = []
temp = str.split()
for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)
for i in res:
    print(i)
