# Movie Ticket Pricing System

age = int(input("Enter age: "))
day = input("Enter day of the week: ").strip().lower()
tickets = int(input("Enter number of tickets: "))

# Determine base price based on age
if age < 3:
    price = 0
    category = "Free"
elif 3 <= age <= 12:
    price = 150
    category = "Child"
elif 13 <= age <= 59:
    price = 300
    category = "Adult"
else:
    price = 200
    category = "Senior"

base_amount = price * tickets

# Determine discount
if day in ["friday", "saturday", "sunday"]:
    discount = base_amount * 0.20
    discount_text = "20% Weekend Discount Applied"
else:
    discount = 0
    discount_text = "No Discount"

final_amount = base_amount - discount

# Display result
print("\n===== MOVIE BILL =====")
print("Age Category:", category)
print("Price per Ticket: ₹", price)
print("Number of Tickets:", tickets)
print("Base Amount: ₹", base_amount)
print("Discount:", discount_text)
print("Discount Amount: ₹", round(discount, 2))
print("Final Amount to Pay: ₹", round(final_amount, 2))

output:

If:
Age = 65
Day = Sunday
Tickets = 3
Then:
Price per ticket = ₹200
Base amount = ₹600
20% discount = ₹120
Final amount = ₹480
