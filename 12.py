# Multiplication Table Program

number = int(input("Enter number: "))
end = int(input("Enter range (end): "))

print("\nMultiplication Table of", number)

for i in range(1, end + 1):
    print(number, "x", i, "=", number * i)
  output:
Enter number: 5
Enter range (end): 8

Multiplication Table of 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
