import calendar

start = int(input("Enter start year: "))
end = int(input("Enter end year: "))

for year in range(start, end):
    if calendar.isleap(year):
        print(f"The year {year} is a leapyear.")
    else:
        print(f"The year {year} is not a leapyear")

input("Press ENTER to close the app.")
