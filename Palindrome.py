user_input = input("Enter word/number: ")

# Step 1: Store original input
original = user_input

# Step 2: Normalize for comparison (ignore case for words)
normalized = str(user_input).lower()

# Step 3: Reverse the input
reversed_input = normalized[::-1]

# Step 4: Display step-by-step
print("\nOriginal:", original)
print("Reversed:", user_input[::-1])

# Step 5: Check palindrome
if normalized == reversed_input:
    print("Result: PALINDROME ")
else:
    print("Result: NOT a palindrome ")


Enter word/number: Madam
Original: Madam
Reversed: madaM
Result: PALINDROME ✅

Enter word/number: 12321
Original: 12321
Reversed: 12321
Result: PALINDROME ✅
