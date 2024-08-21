#Create a program that determines whether a given year is a leap year.

#A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
#Use an if-else statement to make this determination.

leap_year = int(input("enter the year : "))
if leap_year % 4 ==0 and leap_year % 100 != 0 or leap_year % 400 == 0:
    print(f"leap year -> {leap_year}")
else:
    print(f"not a leap year -> {leap_year}")

