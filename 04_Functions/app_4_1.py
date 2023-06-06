from calendar import isleap
from datetime import datetime
from dateutil.relativedelta import relativedelta


# Problem 1
def sum_of_three(a, b, c):
    return print("1.", a + b + c)


sum_of_three(1, 2, 3)


# Problem 2
def sum_of_list():
    list = []
    list_length = int(input("How many numbers would you like to add? "))
    for i in range(list_length):
        number = float(input("Enter a number: "))
        list.append(number)
    return print("2.", sum(list))
sum_of_list()


# Problem 3
def largest_number(*args):
    return print("3.", max(*args))


largest_number(2, 4, 8, 17, 1, 34)


# Problem 4
def text_reversed(text):
    return print("4.", text[::-1])


text_reversed("Cold beet soup")


# Problem 5
def text_details(text):
    words = len(list(text.split(" ")))
    text_list = list(text.split())
    uppercase, lowercase, numbers = 0, 0, 0
    for i in text_list:
        for n in i:
            if (n.isupper()) == True:
                uppercase += 1
            elif (n.islower()) == True:
                lowercase += 1
            elif (n.isnumeric()) == True:
                numbers += 1
    return print(
        f"5. Text contains {words} words of which there are {uppercase} uppercase, {lowercase} lowercase, {numbers} number characters.")


text_details("The 5 quick brown foxes jumped over the 3 lazy dogs.")


# Problem 6
def get_unique(numbers_list):
    list = []
    unique = set(numbers_list)
    for i in unique:
        list.append(i)
    return print(f"6. Unique numbers: {unique}")


get_unique([2, 4, 6, 8, 8, 8, 2, 4, 5])


# Problem 7
def get_prime(number):
    if number < 2:
        return print("7. Not a prime number.")
    for i in range(2, number):
        if number % i == 0:
            return print("7. Not a prime number.")
    return print("7. A prime number.")


get_prime(5)


# Problem 8
def reverse_list(list):
    reversed = list[::-1]
    return print(f'8. Reversed: {reversed}')


reverse_list(["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"])


# Problem 9
def get_leap(year):
    if isleap(year) == True:
        return print("9. Leap year.")
    else:
        return print("9. Not a leap year.")


get_leap(2008)


# Problem 10
def time_difference(input_date):
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
        f"10. You were born {years} years, {months} months, {days} days, "
        f"{hours} hours, {minutes} minutes, {seconds} seconds ago.")


time_difference("1994 09 03 12:45:27")
