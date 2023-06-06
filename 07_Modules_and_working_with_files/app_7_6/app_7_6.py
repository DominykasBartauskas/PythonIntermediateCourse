from budgeting_app import BudgetingApp
from text_colors import *

budget = BudgetingApp()
while True:
    printBlue("\n"
              "Here's a list of action you can do:\n"
              "1. Create income entry.\n"
              "2. Create expense entry.\n"
              "3. Show budget balance.\n"
              "4. Create a budget report with income and expenses.\n"
              "5. Save to external file.\n"
              "6. Load from external file.\n"
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
        case "5":
            budget.save_list()
        case "6":
            budget.load_list()
        case "9":
            printBlue("Thank you for using the Budgeting App!")
            break
        case _:
            printRed("Wrong choice. Please try again. \n")
