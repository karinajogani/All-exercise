a = "America"
b = "Japan"
def mix_string(a, b):
    first_char = a[0] + b[0]
    middle_char = a[int(len(a) / 2):int(len(a) / 2) + 1] + b[int(len(b) / 2):int(len(b) / 2) + 1]
    last_char = a[len(a) - 1] + b[len(b) - 1]
    res = first_char + middle_char + last_char
    print("Mix String is ", res)

mix_string(a, b)
