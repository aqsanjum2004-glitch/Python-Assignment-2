# Number System Functions Program

def factorial(n):
    if n < 0:
        return None
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n <= 0:
        return None
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return a

def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

def reverse_number(n):
    reversed_num = int(str(abs(n))[::-1])
    return reversed_num if n >= 0 else -reversed_num

def is_armstrong(n):
    num_str = str(abs(n))
    power = len(num_str)
    total = sum(int(digit)**power for digit in num_str)
    return total == abs(n)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def is_perfect_number(n):
    if n <= 0:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

# Menu function to call all functions
def math_menu():
    while True:
        print("\n===== NUMBER SYSTEM FUNCTIONS MENU =====")
        print("1. Factorial")
        print("2. Check Prime")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number")
        print("10. Exit")
        
        choice = int(input("Enter your choice (1-10): "))
        
        if choice == 1:
            n = int(input("Enter a number: "))
            print(f"{n}! =", factorial(n))
        elif choice == 2:
            n = int(input("Enter a number: "))
            print(n, "is Prime?" , is_prime(n))
        elif choice == 3:
            n = int(input("Enter n for Fibonacci: "))
            print(f"The {n}th Fibonacci number is", fibonacci(n))
        elif choice == 4:
            n = int(input("Enter a number: "))
            print("Sum of digits:", sum_of_digits(n))
        elif choice == 5:
            n = int(input("Enter a number: "))
            print("Reversed number:", reverse_number(n))
        elif choice == 6:
            n = int(input("Enter a number: "))
            print(n, "is Armstrong?", is_armstrong(n))
        elif choice == 7:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(f"GCD({a}, {b}) =", gcd(a, b))
        elif choice == 8:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(f"LCM({a}, {b}) =", lcm(a, b))
        elif choice == 9:
            n = int(input("Enter a number: "))
            print(n, "is Perfect?", is_perfect_number(n))
        elif choice == 10:
            print("Exiting menu...")
            break
        else:
            print("Invalid choice! Select 1-10.")

# Run the menu
math_menu()
