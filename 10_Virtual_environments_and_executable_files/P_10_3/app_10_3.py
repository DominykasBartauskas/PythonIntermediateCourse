from tkinter import *


class HelloApp:
    def __init__(self, root):
        self.root = root
        self.last_entry = StringVar(root, "")

        self.menu = Menu(root)
        self.root.config(menu=self.menu)
        self.submenu = Menu(self.menu, tearoff=0)

        self.menu.add_cascade(label="Menu", menu=self.submenu)
        self.submenu.add_command(label="Clear", command=self.clear_name)
        self.submenu.add_command(label="Restore", command=self.restore_name)
        self.submenu.add_separator()
        self.submenu.add_command(label="Exit", command=root.destroy)

        self.label1 = Label(root, text="Enter your name:")
        self.label1.grid(row=0, column=0, sticky=E)
        self.field1 = Entry(root)
        self.field1.grid(row=0, column=1)
        self.button1 = Button(root, text="Confirm", command=self.print_name)
        self.button1.grid(row=0, column=2)
        self.result = Label(root, text="")
        self.result.grid(row=1, columnspan=3)

        self.statusbar = Label(root, text="", bd=1, relief=SUNKEN, anchor=W)
        self.statusbar.grid(row=2, columnspan=3, sticky=W + E)

        root.bind("<Return>", lambda event: self.print_name())
        root.bind("<Escape>", lambda event: root.destroy())

    def print_name(self):
        self.user_input = self.field1.get()
        self.result["text"] = f"Hello, {self.user_input}!"
        self.last_entry.set(self.user_input)
        self.statusbar["text"] = "Created."

    def clear_name(self):
        self.result["text"] = ""
        self.statusbar["text"] = "Cleared."

    def restore_name(self):
        self.result["text"] = f"Hello, {self.last_entry.get()}!"
        self.statusbar["text"] = "Restored."


def main():
    root = Tk()
    # <-- App name and icon
    root.title('Names App')
    root.iconbitmap("icon.ico")
    # <--
    HelloApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
