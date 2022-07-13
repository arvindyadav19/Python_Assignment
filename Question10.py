# Q10) Write a Program to take integer input from the user as year and check
# whether the given year is a leap year or not.
# Hint: A year must either be divisible by 400 or divisible by 4 and not 100.

# year % 400  --> For Century Years
# year %  4   and year % 100 !=0     ----> For Normal years


year = int(input("Enter the year:"))


if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
    print("Year is a Leap Year")
else:
    print("Year is not leap year")