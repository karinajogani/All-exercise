sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
# print(set(sample_list))

sample_set.update(set(sample_list))
print(sample_set)