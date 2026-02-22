Step 1: Import current year
from datetime import datetime

current_year = datetime.now().year

# Step 2: Take birth year input
try:
    birth_year = int(input("Enter your birth year: "))

    # Step 3: Calculate age in years
    age_years = current_year - birth_year

    # Step 4: Calculate other values
    age_months = age_years * 12
    age_days = age_years * 365          # approximate
    age_hours = age_days * 24
    age_minutes = age_hours * 60
    years_to_100 = 100 - age_years

    # Step 5: Display results
    print("\nYour Current Age:", age_years, "years")
    print("Age in Months:", age_months)
    print("Age in Days (approx):", age_days)
    print("Age in Hours:", age_hours)
    print("Age in Minutes:", age_minutes)
    print("Years until 100:", years_to_100)

except ValueError:
    print("Invalid input! Please enter a valid year.")

# End of Program
output:
Enter your birth year: 2004
Your Current Age: 22 years
Age in Months: 264
Age in Days (approx): 8030
Age in Hours: 192720
Age in Minutes: 11563200
Years until 100: 78
