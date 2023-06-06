from datetime import datetime

class Worker:
    def __init__(self, name, hourly_wage, works_since):
        self.name = name
        self.hourly_wage = hourly_wage
        self._works_since = datetime.strptime(works_since, "%Y %m %d")

    def __str__(self):
        return f"Worker {self.name} works since {self._works_since.date()} and is paid {self.hourly_wage} USD/hour."

    def _count_workdays(self):
        current_date = datetime.now()
        difference = current_date - self._works_since
        days = divmod(difference.days, 1)
        return days[0]

    def calculate_wage(self):
        return f"Worker {self.name} has been paid {self.hourly_wage * self._count_workdays() * 8} USD."

class NormalWorker(Worker):
    def calculate_wage(self):
        return f"Worker {self.name} has been paid {round(self.hourly_wage * (self._count_workdays() * 8 / 7 * 5))} USD."

worker_obj = Worker("Adomas", 18, "2023 05 24")
normal_worker_obj = NormalWorker("Tadas", 18, "2023 05 24")
print(worker_obj)
print(normal_worker_obj)
print(worker_obj.calculate_wage())
print(normal_worker_obj.calculate_wage())