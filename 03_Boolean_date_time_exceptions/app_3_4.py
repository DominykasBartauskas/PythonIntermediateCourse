import time

while True:
    try:
        word = input("Enter a word: ")
        delay = float(input("Enter a delay between words (in seconds): "))
    except ValueError as error:
        print("Enter a valid number.")
        print("Details: ", error, "\n")

    for i in range(5):  # <-- Range given to prevent endless loop.
        print(word)
        time.sleep(delay)
    break
