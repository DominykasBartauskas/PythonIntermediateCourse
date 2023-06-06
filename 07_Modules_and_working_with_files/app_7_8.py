import os
from datetime import datetime

current_date = datetime.today()

os.chdir(r"C:\Users\barta\Desktop")
os.mkdir("New_Catalog")
os.chdir(r"New_Catalog")

print("Current working directory: {0}".format(os.getcwd()))

with open("file.txt", "w", encoding="utf-8") as file:
    file.write(str(current_date))

with open("file.txt", "r", encoding="utf-8") as file:
    date = os.stat("file.txt").st_ctime
    print(f'File creation date: {datetime.fromtimestamp(date)}.')
    print(f'File size: {os.stat("file.txt").st_size} bytes.')
