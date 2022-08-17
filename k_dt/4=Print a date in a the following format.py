from datetime import datetime

given_date = datetime(2020, 2, 25)

output = given_date.strftime('%A %d %B %Y')
print(output)