from calendar import isleap

list = []
for year in range(1900, 2100):
    if isleap(year) == True:
        list.append(year)
    else:
        continue

print(list)
