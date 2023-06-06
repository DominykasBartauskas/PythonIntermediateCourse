from datetime import datetime, timedelta
from calendar import isleap
from dateutil.relativedelta import relativedelta


class DateManipulation:
    def __init__(self, anniversary: str) -> str:
        entered_anniversary = anniversary
        if entered_anniversary == '':
            self.anniversary = datetime.strptime("1994 09 03 12:45:25", "%Y %m %d %H:%M:%S")
        else:
            self.anniversary = datetime.strptime(entered_anniversary, "%Y %m %d %H:%M:%S")

    def date_difference(self):
        current_date = datetime.now()

        difference = relativedelta(current_date, self.anniversary)

        years = difference.years
        months = difference.months
        days = difference.days
        hours = difference.hours
        minutes = difference.minutes
        seconds = difference.seconds

        print(
            f"Difference: {years} years, {months} months, {days} days, "
            f"{hours} hours, {minutes} minutes, {seconds} seconds ago.")

    def is_leap(self):
        if isleap(self.anniversary.year) == True:
            return print(f'The year {self.anniversary.year} is a leap year.')
        else:
            return print(f'The year {self.anniversary.year} is not a leap year.')

    def days_subtract(self):
        subtract_days = int(input("Enter the amount of days to subtract: "))
        print(f'The new date after subtraction: {self.anniversary.date() - timedelta(days=subtract_days)}')

    def days_add(self):
        add_days = int(input("Enter the amount of days to add: "))
        print(f'The new date after addition: {self.anniversary.date() + timedelta(days=add_days)}')

    def __str__(self):
        return str(self.anniversary.date())


anniversary_object = DateManipulation(input("Please enter your anniversary date (YYYY-MM-DD): "))
anniversary_object.date_difference()
anniversary_object.is_leap()
anniversary_object.days_subtract()
anniversary_object.days_add()

print(anniversary_object)
