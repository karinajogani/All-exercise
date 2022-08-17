import string

str = "/*Jon is @developer & musician"
print(str)

str1 = str.translate(str.maketrans('', '', string.punctuation))

print(str1)