Step 1: Take inputs
    total_bill = float(input("Enter total bill amount: "))
    people = int(input("Enter number of people: "))
    tax_percent = float(input("Enter tax percentage: "))
    tip_percent = float(input("Enter tip percentage: "))

    # Step 2: Calculate tax amount
    tax_amount = (tax_percent / 100) * total_bill

    # Step 3: Calculate bill after tax
    bill_after_tax = total_bill + tax_amount

    # Step 4: Calculate tip amount (based on after-tax amount)
    tip_amount = (tip_percent / 100) * bill_after_tax

    # Step 5: Final total
    final_total = bill_after_tax + tip_amount

    # Step 6: Per person amount
    if people > 0:
        per_person = final_total / people
    else:
        per_person = 0

    # Step 7: Display results
    print("\n=== BILL BREAKDOWN ===")
    print("Subtotal: ₹{:.2f}".format(total_bill))
    print("Tax ({}%): ₹{:.2f}".format(tax_percent, tax_amount))
    print("After tax: ₹{:.2f}".format(bill_after_tax))
    print("Tip ({}%): ₹{:.2f}".format(tip_percent, tip_amount))
    print("Total: ₹{:.2f}".format(final_total))
    print("Per person: ₹{:.2f}".format(per_person))

except ValueError:
    print("Invalid input! Please enter numeric values only.")

# End of Program
output:
Enter total bill amount: 2500
Enter number of people: 5
Enter tax percentage: 8
Enter tip percentage: 12
..........................
=== BILL BREAKDOWN ===
Subtotal: ₹2500.00
Tax (8%): ₹200.00
After tax: ₹2700.00
Tip (12%): ₹324.00
Total: ₹3024.00
Per person: ₹604.80
