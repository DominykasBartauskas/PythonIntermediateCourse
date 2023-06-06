from datetime import datetime

zen_text = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!\n'''


def write_zen(text):
    with open("zen.txt", "w", encoding="utf-8") as file_zen:
        file_zen.write(text)


def print_zen():
    with open("zen.txt", "r", encoding="utf-8") as file_zen:
        print(file_zen.read())


def write_time():
    with open("zen.txt", "a", encoding="utf-8") as file_zen:
        file_zen.write(str(datetime.now()))


def write_numbering():
    with open("zen.txt", "r", encoding="utf-8") as file_zen:
        lines = file_zen.readlines()

    with open("zen.txt", "w", encoding="utf-8") as file_zen:
        for i, line in enumerate(lines, 1):
            modified = f"{i}. {line}"
            file_zen.write(modified)


def write_change(text):
    with open("zen.txt", "r", encoding="utf-8") as file_zen:
        data = file_zen.read()
        data = data.replace("Beautiful is better than ugly", text)

    with open("zen.txt", "w", encoding="utf-8") as file_zen:
        file_zen.write(data)


def print_reversed():
    with open("zen.txt", "r", encoding="utf-8") as file_zen:
        data = file_zen.read()[::-1]
        print("Reversed data: \n", data)


def count_text():
    with open("zen.txt", "r", encoding="utf-8") as file_zen:
        data = file_zen.read()
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


def copy_uppercase():
    with open("zen.txt", "r", encoding="utf-8") as file_zen:
        with open("zen_upper.txt", "w", encoding="utf-8") as file_upper:
            for line in file_zen:
                file_upper.write(line.upper())


write_zen(zen_text)
write_time()
write_numbering()
write_change("Gražu yra geriau nei bjauru.")
print_reversed()
print_zen()
count_text()
copy_uppercase()
