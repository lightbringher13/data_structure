# functions with return
import statistics


def add(a, b):
    c = a+b


# implicitly by default func returns None
print(add(5, 4))

# functions with return


def add(a, b):
    c = a+b
    return c
    # return a+b


print(add(5, 4))

# coding assignment

# title() Capitalizes the first letter of each word
# capitalize() Capitalizes the first character of the string


def format_names(a, b):
    # can return f-string
    return f"{a.capitalize()} {b.capitalize()}"

    # print(f"{a.capitalize()} {b.capitalize()}")


print(format_names("jenny", "KHATRI"))

# return multiple values

# use statistic library to use mean mode median


def mean_median_mode(x):
    return statistics.mean(x), statistics.median(x), statistics.mode(x)
    print("End of function")  # ignored
    # list also possible
    # return [statistics.mean(x), statistics.median(x), statistics.mode(x)]


# default it is tuple
print(mean_median_mode([3, 5, 45, 3, 2, 1, 89]))

# create each variable possible
# a, b, c = mean_median_mode([3, 5, 45, 3, 2, 1, 89])
# print(f"mean is {a}, median is {b}, mode is {c}")


def add(a, b):
    if a == 0 and b == 0:
        return "you have entered zero for both variables"
    else:
        return a+b


var1 = int(input("enter a num: "))
var2 = int(input("enter a num: "))
print(add(var1, var2))

# coding exercise
# formatting string if both none return a msg


def format_names(a, b):
    if a == "" and b == "":
        return "you have entered zero for both variables"
    else:
        return a.capitalize(), b.title()


var1 = input("enter a string: ")
var2 = input("enter a string: ")
print(format_names(var1, var2))

# coding exercise
month_days1 = {
    1: 31,
    2: [28, 29],
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


# Corrected dictionary and renamed to avoid conflicts
month_days_dict = {
    1: 31,
    2: [28, 29],  # February can have 28 or 29 days
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def get_month_days(year, month):
    if month == 2:  # Handle February separately
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{month_days_dict[month][1]} days in February in {year}")
        else:
            print(f"{month_days_dict[month][0]} days in February in {year}")
    else:  # All other months
        print(f"{month_days_dict[month]} days in month {month} in {year}")


# Input year and month
year = int(input("Enter a year: "))
month = int(input("Enter a month (1-12): "))
if 1 <= month <= 12:  # Validate month input
    get_month_days(year, month)
else:
    print("Invalid month! Please enter a value between 1 and 12.")

 # use the return value


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


print(sub(add(4, 5), 6))
