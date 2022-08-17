set1 = {27, 43, 34}
set2 = {34, 93, 22, 27, 43, 53, 48}
a = set1.issubset(set2)
c = set1.issuperset(set2)
print("set1 is subset of set2", a)
print("set1 is superset of set2", c)
b = set2.issubset(set1)
d = set2.issuperset(set1)
print("set1 is subset of set2", b)
print("set1 is superset of set2", d)

set1.clear()
print("set1", set1)
print("set2", set2)
