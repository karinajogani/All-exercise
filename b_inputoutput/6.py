def skipLineSlicing(f, skip):
    try:
        f = open("C:\\Users\\g50\\Desktop\\python.txt")
        skipLineSlicing(f, 5)
    finally:
        f.close()

# ##
# def skipLine(f, skip):
#   lines = f.readlines()
#   skip = skip - 5
#   for line_no, line in enumerate(lines):
#     if line_no==skip:
#       pass
#     else:
#       print(line, end="")