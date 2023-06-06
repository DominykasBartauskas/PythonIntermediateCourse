from datetime import datetime
from dateutil.relativedelta import relativedelta

while True:
    try:
        input_date = input("Enter your birth date and time (format: 'YYYY MM DD H:M:S'): ")
        date_format = "%Y %m %d %H:%M:%S"
        user_date = datetime.strptime(input_date, date_format)
        current_date = datetime.now()

        difference = relativedelta(current_date, user_date)

        years = difference.years
        months = difference.months
        days = difference.days
        hours = difference.hours
        minutes = difference.minutes
        seconds = difference.seconds

        print(
            f"You were born {years} years, {months} months, {days} days, "
            f"{hours} hours, {minutes} minutes, {seconds} seconds ago.")
        break
    except ValueError as error:
        print("Your entered date is incorrect. Please check for formating mistakes.")
        print("Details: ", error, "\n")