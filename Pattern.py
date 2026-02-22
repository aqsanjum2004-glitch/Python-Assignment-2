# Pattern Printing Program

def pattern1(height):
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def pattern2(height):
    for i in range(1, height + 1):
        for j in range(i):
            print(i, end=" ")
        print()

def pattern3(height):
    for i in range(height, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

def pattern4(height):
    for i in range(1, height + 1):
        # Increasing sequence
        for j in range(1, i + 1):
            print(j, end="")
        # Decreasing sequence
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

def print_patterns():
    print("===== PATTERN MENU =====")
    print("1. Pattern 1 (1 to n in rows)")
    print("2. Pattern 2 (Repeated numbers)")
    print("3. Pattern 3 (Reverse triangle)")
    print("4. Pattern 4 (Pyramid palindrome numbers)")

    choice = int(input("Enter pattern number (1-4): "))
    height = int(input("Enter the height of pattern: "))

    print("\n===== PATTERN OUTPUT =====")
    if choice == 1:
        pattern1(height)
    elif choice == 2:
        pattern2(height)
    elif choice == 3:
        pattern3(height)
    elif choice == 4:
        pattern4(height)
    else:
        print("Invalid choice! Please select 1-4.")

# Run the program
print_patterns()
