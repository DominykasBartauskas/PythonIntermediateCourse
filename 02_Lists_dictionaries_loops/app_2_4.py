import random

while True:
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num3 = random.randint(1, 6)

    print(f"Your lucky numbers are: {num1}, {num2}, {num3}.")

    if num1 == 5 or num2 == 5 or num3 == 5:
        print("You lost.")
        break
    else:
        print("You won!")
        break
