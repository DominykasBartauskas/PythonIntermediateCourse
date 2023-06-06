import pickle

from income_entry import IncomeEntry
from expense_entry import ExpenseEntry
from text_colors import *

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

    def save_list(self):
        with open("budget.pkl", "wb") as budget_list:
            pickle.dump(self.journal, budget_list)

    def load_list(self):
        with open("budget.pkl", "rb") as budget_list:
            data = pickle.load(budget_list)
            for entry in data:
                self.journal.append(entry)
