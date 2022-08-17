import string

str = '/*Jon is @developer & musician!!'

replace_char = '#'

for char in string.punctuation:
    str = str.replace(char, replace_char)

print(str)
