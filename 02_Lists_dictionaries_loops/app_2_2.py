sum = 0
while True:
    num = int(input("Enter a number: "))

    if num > 0:
        sum += num
        continue
    else:
        print(sum)
        break
