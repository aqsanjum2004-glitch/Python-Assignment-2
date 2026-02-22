# ===================================================================
# Program Name   : Personal Bio Card
# Author         : AQSA KHAN
# Date           : 21-Feb-2026
# Course         : Python Programming
# College        : Anjuman Institute Of Technology and Management
# Email          : aqsanjum2004@gmail.com
# Purpose        : To display student information in a nicely formatted
#                  bio card using variables and string formatting.
# Inputs         : None (all information stored in variables)
# Outputs        : Formatted student bio card displayed on console
# Logic/Methods  : 
#   - Store each piece of information in a separate variable
#   - Use string formatting to align text and create borders
#   - Use Unicode box characters to make it visually appealing
# ===================================================================

# ------------------------
# Step 1: Store student information in variables
# ------------------------
name = "AQSA KHAN"  # Student's full name
age = 22            # Student's age in years
course = "Python Programming"  # Course enrolled
college = "Anjuman Institute Of Technology and Management"  # College name
email = "aqsanjum2004@gmail.com"  # Student email address

# ------------------------
# Step 2: Display the bio card
# ------------------------
# Top border of the card
print("╔" + "═"*40 + "╗")

# Title centered inside the card
print("║{:^40}║".format("STUDENT BIO CARD"))

# Separator below title
print("╚" + "═"*40 + "╝")

# Display each field with proper alignment
print("║ Name   : {:<31}║".format(name))
print("║ Age    : {:<31}║".format(str(age) + " years"))
print("║ Course : {:<31}║".format(course))
print("║ College: {:<31}║".format(college))
print("║ Email  : {:<31}║".format(email))

# Bottom border of the card
print("╚" + "═"*40 + "╝")

# ------------------------
# End of Program
# ------------------------
