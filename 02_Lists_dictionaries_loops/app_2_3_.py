print("Stop inputing by typing 'STOP'.")
list = []
while True:

    word = input("Enter a word: ")
    if word == "STOP":
        break
    else:
        list.append(word)

for i in list:
    print(f"Word: {i}, length: {len(i)}, index: {list.index(i) + 1}")
