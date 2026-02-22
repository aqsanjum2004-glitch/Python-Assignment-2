# Function-Based Calculator Program

# -------------------------------
# Basic Mathematical Functions
# -------------------------------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a % b

def power(a, b):
    return a ** b

# -------------------------------
# Main Calculator Menu
# -------------------------------
def calculator():
    while True:
        print("\n===== CALCULATOR MENU =====")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Power (^)")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "7":
            print("Exiting calculator. Goodbye!")
            break
        
        if choice not in ["1","2","3","4","5","6"]:
            print("Invalid choice! Select 1-7.")
            continue
        
        # Take inputs
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        # Perform calculation
        if choice == "1":
            print(f"Result: {a} + {b} = {add(a,b)}")
        elif choice == "2":
            print(f"Result: {a} - {b} = {subtract(a,b)}")
        elif choice == "3":
            print(f"Result: {a} * {b} = {multiply(a,b)}")
        elif choice == "4":
            print(f"Result: {a} / {b} = {divide(a,b)}")
        elif choice == "5":
            print(f"Result: {a} % {b} = {modulus(a,b)}")
        elif choice == "6":
            print(f"Result: {a} ^ {b} = {power(a,b)}")

# -------------------------------
# Run the Calculator
# -------------------------------
calculator()
