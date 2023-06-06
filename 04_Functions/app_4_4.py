def nearby_numbers():
    num = input("Enter number: ")
    num_li = []
    for i in num:
        num_li.append(i)

        num_li_2 = list(map(int, num_li))

    for i in num_li_2:
        num1 = i - 1
        num2 = i + 1

        print(f'{i} - {num1}{num2}', end=', ')


nearby_numbers()
