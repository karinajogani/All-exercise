import os

size = os.stat("C:\\Users\\g50\\Desktop\\python.txt").st_size
if size == 0:
    print('file is empty')
else:
    print("file is not empty")