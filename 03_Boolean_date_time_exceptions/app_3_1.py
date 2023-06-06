while True:
    try:
        num = int(input("Enter a whole number: "))

        result = bool(num > 0)

        if result is True:
            print(True)
            break
        else:
            print(False)
            break
    except ValueError as error:
        print("Your entered number is incorrect (not a whole number). Try again.")
        print("Details: ",  error, "\n")

