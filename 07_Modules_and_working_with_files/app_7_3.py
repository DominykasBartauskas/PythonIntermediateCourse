# <-- Nr. 1

import datetime

print(datetime.datetime.now())
print(datetime.date.today())
now = datetime.datetime.now()
time = now.strftime("%H:%M:%S")
print(time)

# <-- Nr. 2

from datetime import date

print(date.today())

# <-- Nr. 3

from datetime import date as data

print(data.today())
