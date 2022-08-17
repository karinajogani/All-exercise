set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}

print("intersection of set1 and set2 is:", set1 & set2)

a = [57, 83, 29]

set1.difference_update(a)
print("set1 after removing comman element", set1)