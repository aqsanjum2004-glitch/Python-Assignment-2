#Create an ATM simulation with initial balance = ₹10,000.

#Menu: 1. Check Balance 2. Deposit Money 3. Withdraw Money 4. Exit

Rules:

- Check sufficient balance before withdrawal

- Minimum balance of ₹500 must remain at all times

- Display transaction messages and updated balance after each transaction

Sample Run:

ATM SIMULATOR

#1. Check Balance

#2. Deposit

#3. Withdraw

#4. Exit

#Enter choice: 3

#Enter amount to withdraw: 2000

Withdrawal successful!

New balance: ₹8000

#Prgm
# ATM Simulation Program

balance = 10000   # Initial balance

while True:
    print("\n===== ATM SIMULATOR =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance: ₹", balance)

    elif choice == 2:
        deposit = float(input("Enter amount to deposit: ₹"))
        if deposit > 0:
            balance += deposit
            print("Deposit successful!")
            print("Updated Balance: ₹", balance)
        else:
            print("Invalid deposit amount!")

    elif choice == 3:
        withdraw = float(input("Enter amount to withdraw: ₹"))
        
        if withdraw <= 0:
            print("Invalid withdrawal amount!")

        elif withdraw > balance:
            print("Insufficient balance!")

        elif balance - withdraw < 500:
            print("Minimum balance of ₹500 must be maintained.")
            print("Withdrawal denied!")

        else:
            balance -= withdraw
            print("Withdrawal successful!")
            print("Updated Balance: ₹", balance)

    elif choice == 4:
        print("Thank you for using ATM. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1-4.")
