from calendar import isleap

year = int(input("Enter a year to check: "))

if isleap(year) == True:
    print("Leap year.")
else:
    print("Not a leap year.")