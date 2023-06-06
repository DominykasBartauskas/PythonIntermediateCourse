class Entries:
    def __init__(self, entry_type, entry_sum):
        self.entry_type = entry_type
        self.entry_sum = entry_sum

    def __str__(self):
        return f'{self.entry_type}: {self.entry_sum} USD.'