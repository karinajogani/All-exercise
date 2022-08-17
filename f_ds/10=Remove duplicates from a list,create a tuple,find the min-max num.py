list1 = [87, 52, 44, 53, 54, 87, 52, 53]

print("list:", list1)

list1 = list(set(list1))
print("unique items:", list1)

t = tuple(list1)
print("tuple:", t)

print("minimum number is: ", min(t))
print("maximum number is: ", max(t))