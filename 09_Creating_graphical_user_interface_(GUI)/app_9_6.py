from tkinter import *
import pickle


class BudgetAppGUI:
    def __init__(self, root):
        self.root = root
        self.entries = Entries
        self.journal = []

        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.submenu = Menu(self.menu, tearoff=0)

        # <-- Menubar
        self.menu.add_cascade(label="Menu", menu=self.submenu)
        self.submenu.add_command(label="Create income entry", command=self.new_income)
        self.submenu.add_command(label="Create expense entry", command=self.new_expense)
        self.submenu.add_separator()
        self.submenu.add_command(label="Show balance", command=self.get_balance)
        self.submenu.add_separator()
        self.submenu.add_command(label="Save", command=self.save_list)
        self.submenu.add_command(label="Load", command=self.load_list)
        self.submenu.add_separator()
        self.submenu.add_command(label="Exit", command=self.root.destroy)

        # <-- Journal
        self.scrollbar = Scrollbar(root)
        self.scrollbar.pack(side="right", fill="both")

        self.listbox = Listbox(root, height=10)
        for entry in self.journal:
            if entry.entry_type == "Income":
                detailed = f'{entry.entry_type}: {entry.entry_sum} USD. Received from {entry.sender} for {entry.more_info}.'
                self.listbox.insert(END, detailed)
            else:
                detailed = f'{entry.entry_type}: {entry.entry_sum} USD. Paid using {entry.payment_type} for {entry.paid_for}.'
                self.listbox.insert(END, detailed)
        self.listbox.pack(fill="both")

        # <-- Statusbar
        self.statusbar = Label(root, text="", bd=1, relief=SUNKEN, anchor=W)
        self.statusbar.pack(side="bottom", fill="x")

    def update_listbox(self):
        self.listbox.delete(0, END)
        for entry in self.journal:
            if entry.entry_type == "Income":
                detailed = f'{entry.entry_type}: {entry.entry_sum} USD. Received from {entry.sender} for {entry.more_info}.'
                self.listbox.insert(END, detailed)
            else:
                detailed = f'{entry.entry_type}: {entry.entry_sum} USD. Paid using {entry.payment_type} for {entry.paid_for}.'
                self.listbox.insert(END, detailed)

    def new_income(self):
        income_entry_window = Toplevel(self.root)
        income_entry_window.title("Create income entry")

        self.IE_label1 = Label(income_entry_window, text="Amount: ")
        self.IE_label1.grid(row=0, column=0, sticky=E)
        self.IE_field1 = Entry(income_entry_window)
        self.IE_field1.grid(row=0, column=1)
        self.IE_label2 = Label(income_entry_window, text="Sender: ")
        self.IE_label2.grid(row=1, column=0, sticky=E)
        self.IE_field2 = Entry(income_entry_window)
        self.IE_field2.grid(row=1, column=1)
        self.IE_label3 = Label(income_entry_window, text="Details: ")
        self.IE_label3.grid(row=2, column=0, sticky=E)
        self.IE_field3 = Entry(income_entry_window)
        self.IE_field3.grid(row=2, column=1)
        self.IE_button1 = Button(income_entry_window, text="Confirm", command=self.entry_income)
        self.IE_button1.grid(row=3, columnspan=2)

    def entry_income(self):
        entry_sum = self.IE_field1.get()
        sender = self.IE_field2.get()
        more_info = self.IE_field3.get()
        self.journal.append(IncomeEntry('Income', entry_sum, sender, more_info))
        self.update_listbox()
        self.statusbar["text"] = "Income entry added."
        self.IE_button1.master.destroy()

    def new_expense(self):
        expense_entry_window = Toplevel(self.root)
        expense_entry_window.title("Create income entry")

        self.EE_label1 = Label(expense_entry_window, text="Amount: ")
        self.EE_label1.grid(row=0, column=0, sticky=E)
        self.EE_field1 = Entry(expense_entry_window)
        self.EE_field1.grid(row=0, column=1)
        self.EE_label2 = Label(expense_entry_window, text="Type: ")
        self.EE_label2.grid(row=1, column=0, sticky=E)
        self.EE_field2 = Entry(expense_entry_window)
        self.EE_field2.grid(row=1, column=1)
        self.EE_label3 = Label(expense_entry_window, text="Details: ")
        self.EE_label3.grid(row=2, column=0, sticky=E)
        self.EE_field3 = Entry(expense_entry_window)
        self.EE_field3.grid(row=2, column=1)
        self.EE_button1 = Button(expense_entry_window, text="Confirm", command=self.entry_expense)
        self.EE_button1.grid(row=3, columnspan=2)

    def entry_expense(self):
        entry_sum = self.EE_field1.get()
        payment_type = self.EE_field2.get()
        paid_for = self.EE_field3.get()
        self.journal.append(ExpenseEntry('Expense', entry_sum, payment_type, paid_for))
        self.update_listbox()
        self.statusbar["text"] = "Expense entry added."
        self.EE_button1.master.destroy()

    def get_balance(self):
        income = 0
        expense = 0
        for entry in self.journal:
            if isinstance(entry, IncomeEntry):
                income += float(entry.entry_sum)
            elif isinstance(entry, ExpenseEntry):
                expense += float(entry.entry_sum)
        balance = income - expense
        self.statusbar["text"] = f"Balance: {balance} USD."

    def save_list(self):
        with open("budget.pkl", "wb") as budget_list:
            pickle.dump(self.journal, budget_list)
            self.statusbar["text"] = "File saved."
            budget_list.close()

    def load_list(self):
        self.journal.clear()
        with open("budget.pkl", "rb") as budget_list:
            self.journal = pickle.load(budget_list)
        self.update_listbox()
        self.statusbar["text"] = "File loaded."
        budget_list.close()


class Entries:
    def __init__(self, entry_type, entry_sum):
        self.entry_type = entry_type
        self.entry_sum = entry_sum

    def __str__(self):
        return f'{self.entry_type}: {self.entry_sum} USD.'


class IncomeEntry(Entries):
    def __init__(self, entry_type, entry_sum, sender, more_info):
        super().__init__(entry_type, entry_sum)
        self.sender = sender
        self.more_info = more_info

    def __str__(self):
        return f'{self.entry_type}: {self.entry_sum} USD.'


class ExpenseEntry(Entries):
    def __init__(self, entry_type, entry_sum, payment_type, paid_for):
        super().__init__(entry_type, entry_sum)
        self.payment_type = payment_type
        self.paid_for = paid_for

    def __str__(self):
        return f'{self.entry_type}: {self.entry_sum} USD.'


def main():
    root = Tk()
    root.title("Budgeting App")
    root.geometry("500x180")
    BudgetAppGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
