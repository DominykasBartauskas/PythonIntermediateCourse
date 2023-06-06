from datetime import datetime, timedelta

current = datetime.now()

print(current)
print(current - timedelta(days=5))
print(current + timedelta(hours=8))
print(current.strftime("%Y %m %d, %H:%M:%S"))
