# Prime Number Program

# -------- PART 1: Check Single Number --------

num = int(input("Enter a number: "))

if num < 0:
    print(num, "is NOT a prime number (negative numbers are not prime).")

elif num == 0 or num == 1:
    print(num, "is NOT a prime number.")

elif num == 2:
    print("2 is a PRIME number.")

else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a PRIME number.")
    else:
        print(num, "is NOT a prime number.")


# -------- PART 2: Prime Numbers in Range --------

start = int(input("\nEnter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers in the given range:")

for n in range(start, end + 1):
    if n > 1:
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        if prime:
            print(n, end=" ")


  output 
Enter a number: 10
10 is NOT a prime number.

Enter start range: 5
Enter end range: 20
Prime numbers in the given range:
5 7 11 13 17 19
