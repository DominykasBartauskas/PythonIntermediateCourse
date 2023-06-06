from datetime import datetime


class TextManipulation:
    def __init__(self, filename, text):
        self.filename = filename
        self.text = text

    def write_text(self):
        with open(f"{filename}.txt", "w", encoding="utf-8") as file:
            file.write(self.text)

    def write_time(self):
        with open(f"{filename}.txt", "a", encoding="utf-8") as file:
            file.write("\n" + str(datetime.now()))

    def write_numbering(self):
        with open(f"{filename}.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        with open(f"{filename}.txt", "w", encoding="utf-8") as file:
            for i, line in enumerate(lines, 1):
                modified = f"{i}. {line}"
                file.write(modified)

    def write_change(self):
        with open(f"{filename}.txt", "r", encoding="utf-8") as file:
            data = file.read()
            print(data)
            to_replace = input("Enter the text to replace: ")
            replace_with = input("Enter the text that will replace: ")
            data = data.replace(to_replace, replace_with)

        with open(f"{filename}.txt", "w", encoding="utf-8") as file:
            file.write(data)

    def count_text(self):
        with open(f"{filename}.txt", "r", encoding="utf-8") as file:
            data = file.read()
            uppercase, lowercase, numeric = 0, 0, 0
            for i in data:
                if i.isupper():
                    uppercase += 1
                elif i.islower():
                    lowercase += 1
                elif i.isnumeric():
                    numeric += 1
            words = len(data.split())
            print(
                f"The text contains {words} words, which have {uppercase} uppercase characters, {lowercase} lowercase characters and {numeric} numbers.")

    def print_file(self):
        with open(f"{filename}.txt", "r", encoding="utf-8") as file:
            print(file.read())

    def print_reversed(self):
        with open(f"{filename}.txt", "r", encoding="utf-8") as file:
            data = file.read()[::-1]
            print("Reversed data: \n", data)


filename = input("Enter file name: ")
text = input("Enter your text: ")
app = TextManipulation(filename, text)
app.write_text()
app.write_time()
app.write_numbering()
app.write_change()
app.count_text()
