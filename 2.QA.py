


# ------------------------
# Step 1: Take input from user
# ------------------------

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # ------------------------
    # Step 2: Perform operations
    # ------------------------

    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Handle division separately to avoid ZeroDivisionError
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Undefined (cannot divide by zero)"

    modulus = num1 % num2 if num2 != 0 else "Undefined"
    exponent = num1 ** num2

    # ------------------------
    # Step 3: Display results
    # ------------------------

    print("\nResults:")
    print(f"{num1} + {num2} = {addition}")
    print(f"{num1} - {num2} = {subtraction}")
    print(f"{num1} * {num2} = {multiplication}")

    if num2 != 0:
        print(f"{num1} / {num2} = {round(division, 2)}")
        print(f"{num1} % {num2} = {modulus}")
    else:
        print(f"{num1} / {num2} = {division}")
        print(f"{num1} % {num2} = {modulus}")

    print(f"{num1} ^ {num2} = {exponent}")

except ValueError:
    print("Invalid input! Please enter numeric values only.")

# ------------------------
# End of Program
# ------------------------
