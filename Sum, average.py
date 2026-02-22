# Program to calculate Sum, Average, Maximum and Minimum

count = int(input("How many numbers? "))

total = 0

for i in range(1, count + 1):
    num = float(input(f"Enter number {i}: "))
    
    total += num
    
    if i == 1:
        maximum = num
        minimum = num
    else:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

average = total / count

print("\n===== RESULTS =====")
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)

O/P
How many numbers? 4
Enter number 1: 12
Enter number 2: 7
Enter number 3: 25
Enter number 4: 9

===== RESULTS =====
Sum: 53.0
Average: 13.25
Maximum: 25.0
Minimum: 7.0
