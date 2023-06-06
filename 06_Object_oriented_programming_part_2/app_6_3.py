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


class ExpenseEntry(Entries):
    def __init__(self, entry_type, entry_sum, payment_type, paid_for):
        super().__init__(entry_type, entry_sum)
        self.payment_type = payment_type
        self.paid_for = paid_for


class BudgetingApp:
    def __init__(self):
        self.journal = []

    def entry_income(self, entry_sum, sender, more_info):
        self.journal.append(IncomeEntry('Income', entry_sum, sender, more_info))

    def entry_expense(self, entry_sum, payment_type, paid_for):
        self.journal.append(ExpenseEntry('Expense', entry_sum, payment_type, paid_for))

    def get_balance(self):
        income = 0
        expense = 0
        for entry in self.journal:
            if isinstance(entry, IncomeEntry):
                income += entry.entry_sum
            elif isinstance(entry, ExpenseEntry):
                expense += entry.entry_sum
        return income - expense

    def show_journal(self):
        for entry in self.journal:
            if isinstance(entry, IncomeEntry):
                printGreen(f'{entry.entry_type}: {entry.entry_sum} USD. Received from {entry.sender} for {entry.more_info}.')
            elif isinstance(entry, ExpenseEntry):
                printRed(f'{entry.entry_type}: {entry.entry_sum} USD. Paid using {entry.payment_type} for {entry.paid_for}.')


# --- Text colors
def printRed(skk):
    print(f"\033[91m {skk}\033[00m")


def printGreen(skk):
    print(f"\033[92m {skk}\033[00m")


def printBlue(skk):
    print(f"\033[96m {skk}\033[00m")


budget = BudgetingApp()
while True:
    printBlue("\n"
              "Here's a list of action you can do:\n"
              "1. Create income entry.\n"
              "2. Create expense entry.\n"
              "3. Show budget balance.\n"
              "4. Create a budget report with income and expenses.\n"
              "9. Exit the Budgeting App.\n")
    menu_input = input("Enter the number (1 - 5) of the action you want to do: \n")
    match menu_input:
        case "1":
            entry_sum = float(input("Please enter the income amount: "))
            sender = str(input("Please enter the sender: "))
            more_info = str(input("Please enter more info about the transaction: "))
            budget.entry_income(entry_sum, sender, more_info)
        case "2":
            entry_sum = float(input("Please enter the expense amount: "))
            payment_type = str(input("Please enter the payment type: "))
            paid_for = str(input("Please enter the goods that were purchased: "))
            budget.entry_expense(entry_sum, payment_type, paid_for)
            printGreen("Expense added successfully!")
        case "3":
            balance = budget.get_balance()
            if balance >= 0:
                printGreen(f"Your current balance is: {balance} USD.")
            else:
                printRed(f"Your current balance is: {balance} USD.")
        case "4":
            budget.show_journal()
        case "9":
            printBlue("Thank you for using the Budgeting App!")
            break
        case _:
            printRed("Wrong choice. Please try again. \n")
