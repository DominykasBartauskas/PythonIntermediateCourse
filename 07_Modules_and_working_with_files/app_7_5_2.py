import pickle

class Worker:
    def __init__(self, fname, lname, wage):
        self.fname = fname
        self.lname = lname
        self.wage = wage

    def __str__(self):
        return f'First name: {self.fname}.\n' \
               f'Last name: {self.lname}.\n' \
               f'Wage: {self.wage}.\n'

with open("workers.pkl", "rb") as file:
    data = pickle.load(file)
    for i in data:
        print(i)