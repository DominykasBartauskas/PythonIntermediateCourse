class Car:
    def __init__(self, year, model, fuel_type):
        self.year = year
        self.model = model
        self.fuel_type = fuel_type

    def __str__(self):
        return f"Your {self.model} was built in {self.year} and uses {self.fuel_type} to function."

    def driving(self):
        print("Is driving.")

    def parked(self):
        print("Is parked.")

    def fuel_refilled(self):
        print("Fuel was pumped.")

class EV(Car):
    def fuel_refilled(self):
        print("Battery was charged.")

    def autonomous_driving(self):
        print("Is driving autonomously.")

car1 = Car(2005, "BMW 320d", "diesel")
car2 = EV(2021, "Tesla Model S", "electricity")
print(car1)
print(car2)

print(f'\n{car1.model}:')
car1.driving(), car1.parked(), car1.fuel_refilled()
print(f'\n{car2.model}:')
car2.driving(), car2.parked(), car2.fuel_refilled(), car2.autonomous_driving()