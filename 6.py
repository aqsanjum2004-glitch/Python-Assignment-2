# Program to calculate total, percentage, grade and result

# Taking input for 5 subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

# Calculating total
total = sub1 + sub2 + sub3 + sub4 + sub5

# Calculating percentage
percentage = (total / 500) * 100

# Determining grade
if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

# Checking pass or fail condition (all subjects >= 40)
if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40 and sub5 >= 40:
    result = "Pass"
else:
    result = "Fail"

# Displaying results
print("\n===== STUDENT RESULT =====")
print("Subject 1:", sub1)
print("Subject 2:", sub2)
print("Subject 3:", sub3)
print("Subject 4:", sub4)
print("Subject 5:", sub5)
print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Final Result:", result)

..............

output:
Enter marks for Subject 1: 78
Enter marks for Subject 2: 85
Enter marks for Subject 3: 69
Enter marks for Subject 4: 92
Enter marks for Subject 5: 74

===== STUDENT RESULT =====
Subject 1: 78.0
Subject 2: 85.0
Subject 3: 69.0
Subject 4: 92.0
Subject 5: 74.0
Total Marks: 398.0 / 500
Percentage: 79.6 %
Grade: B (Good)
Final Result: Pass
