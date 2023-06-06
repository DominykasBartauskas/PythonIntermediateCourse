row = "not empty"
text = ""

while row != "":
    row = input("Enter text: ")
    if row != "":
        text += row + "\n"
    else:
        break

filename = input("Enter file name: ")

with open(f"{filename}.txt", "w", encoding="utf-8") as file:
    file.write(text)
