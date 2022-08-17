from datetime import datetime

given_date = datetime(2020, 2, 25)
stringdate = given_date.strftime("%y-%m-%d %H:%M:%S")
print(stringdate)
