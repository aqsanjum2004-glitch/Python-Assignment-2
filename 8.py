# Program to check whether a year is a leap year

year = int(input("Enter a year: "))

# Checking leap year conditions
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a Leap Year.")
            print("Reason: It is divisible by 4, divisible by 100, and also divisible by 400.")
        else:
            print(year, "is NOT a Leap Year.")
            print("Reason: It is divisible by 100 but NOT divisible by 400.")
    else:
        print(year, "is a Leap Year.")
        print("Reason: It is divisible by 4 and NOT divisible by 100.")
else:
    print(year, "is NOT a Leap Year.")
    print("Reason: It is NOT divisible by 4.")
