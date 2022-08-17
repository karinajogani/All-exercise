from unittest import result


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = [i + j for i in list1 for j in list2]
print(result)



# list3 = zip(list1, list2)
# print(list3)