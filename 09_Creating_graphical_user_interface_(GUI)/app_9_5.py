from tkinter import *
from calendar import isleap


class LeapYearApp:
    def __init__(self, root):
        self.root = root

        self.label1 = Label(root, text="Enter year:")
        self.label1.grid(row=0, column=0, sticky=E)
        self.field1 = Entry(root)
        self.field1.grid(row=0, column=1)
        self.button1 = Button(root, text="Confirm", command=self.get_leap)
        self.button1.grid(row=0, column=2)
        self.result = Label(root, text="")
        self.result.grid(row=1, columnspan=3)

        root.bind("<Return>", lambda event: self.get_leap())
        root.bind("<Escape>", lambda event: root.destroy())

    def get_leap(self):
        self.user_input = int(self.field1.get())
        if isleap(self.user_input) == True:
            self.result["text"] = f"{self.user_input} is a leap year."
        else:
            self.result["text"] = f"{self.user_input} is not a leap year."


def main():
    root = Tk()
    LeapYearApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
