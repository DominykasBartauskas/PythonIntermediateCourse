from statistics import mean, median

# <-- Nr. 1
list = []
for n in range(0, 51):
    list.append(n)

# <-- Nr. 2
list2 = []
for n in list:
    list2.append(n * 10)

# <-- Nr. 3
list3 = []
for n in list:
    if n % 7 == 0:
        list3.append(n)
    else:
        continue

# <-- Nr. 4
list4 = []
for n in list:
    list4.append(n ** 2)

# <-- Nr. 5
list_sum = sum(list4)
list_min = min(list4)
list_max = max(list4)
list_mean = mean(list4)
list_median = median(list4)

# <-- Nr. 6
list4.sort()
print(list4[::-1])





