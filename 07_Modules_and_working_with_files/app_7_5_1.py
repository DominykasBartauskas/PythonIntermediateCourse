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

worker1 = Worker("Tadas", "Petrauskas", 1400)
worker2 = Worker("Petras", "Petrauskas", 1200)
worker3 = Worker("Jonas", "Jonaitis", 700)

with open("workers.pkl", "wb") as file:
    pickle.dump((worker1, worker2, worker3), file)