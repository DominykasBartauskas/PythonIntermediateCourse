from budget_entries import Entries
class ExpenseEntry(Entries):
    def __init__(self, entry_type, entry_sum, payment_type, paid_for):
        super().__init__(entry_type, entry_sum)
        self.payment_type = payment_type
        self.paid_for = paid_for