def add_vat(spent):
    return spent * 1.21


def add_tip(sum):
    return sum * 1.15


def calc_total(spent):
    return print(f"Your total equals to {round(add_tip(add_vat(spent)), 2)}€.")


spent = float(input("Enter spent amount: "))
calc_total(spent)
