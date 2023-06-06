def side_comparison():
    num = input("Enter a number: ")

    side_a = int(num[:len(num) // 2])
    side_b = int(num[len(num) // 2:])

    if side_a == side_b:
        print(True)
    else:
        print(False)


side_comparison()
