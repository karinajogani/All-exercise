str1 = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print("original list is : " + str(str1))
str2 = list(filter(None, str1))
print("modified list is :" + str(str2))