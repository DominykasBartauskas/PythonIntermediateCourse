from budget_entries import Entries
class IncomeEntry(Entries):
    def __init__(self, entry_type, entry_sum, sender, more_info):
        super().__init__(entry_type, entry_sum)
        self.sender = sender
        self.more_info = more_info