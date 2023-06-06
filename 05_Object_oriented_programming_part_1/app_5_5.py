class Entries:
    def __init__(self, entry_sum, entry_type):
        self.entry_sum = entry_sum
        self.entry_type = entry_type

    def __str__(self):
        return f'{self.entry_type}: {self.entry_sum} USD.'


class BudgetingApp:
    def __init__(self):
        self.journal = []

    def entry_income(self, entry_sum):
        self.journal.append(Entries(entry_sum, 'Income'))

    def entry_expense(self, entry_sum):
        self.journal.append(Entries(entry_sum, 'Expense'))

    def get_balance(self):
        income = 0
        expense = 0
        for Entry in self.journal:
            if Entry.entry_type == 'Income':
                income += Entry.entry_sum
            elif Entry.entry_type == 'Expense':
                expense += Entry.entry_sum
        return income - expense

    def show_journal(self):
        for entry in self.journal:
            if entry.entry_type == 'Income':
                printGreen(entry)
            elif entry.entry_type == 'Expense':
                printRed(entry)


# <-- Text colors
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
            budget.entry_income(entry_sum)
            printGreen("Income added successfully!")
        case "2":
            entry_sum = float(input("Please enter the expense amount: "))
            budget.entry_expense(entry_sum)
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
