# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# list3 = [ ]

# print(list1)
# print(list2)
# print(list3)

a = [10, 20, 25, 30, 35]
b = [40, 45, 60, 75, 90]

c = [a*[a%2 != 0], b*[b%2 == 0]]
print(c)