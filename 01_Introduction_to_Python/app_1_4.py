num1 = int(input("Enter number #1: "))
num2 = int(input("Enter number #2: "))

user_choice = input("What operation (+, -, *, /) would you like to perform? ")

match user_choice:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case _:
        print("Wrong input, try again.")
