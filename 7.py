
# Temperature Converter - Menu Based Program


while True:
    print("\n===== TEMPERATURE CONVERTER =====")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print("Temperature in Fahrenheit:", round(f, 2))

    elif choice == 2:
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5/9
        print("Temperature in Celsius:", round(c, 2))

    elif choice == 3:
        c = float(input("Enter temperature in Celsius: "))
        k = c + 273.15
        print("Temperature in Kelvin:", round(k, 2))

    elif choice == 4:
        k = float(input("Enter temperature in Kelvin: "))
        c = k - 273.15
        print("Temperature in Celsius:", round(c, 2))

    elif choice == 5:
        f = float(input("Enter temperature in Fahrenheit: "))
        k = (f - 32) * 5/9 + 273.15
        print("Temperature in Kelvin:", round(k, 2))

    elif choice == 6:
        k = float(input("Enter temperature in Kelvin: "))
        f = (k - 273.15) * 9/5 + 32
        print("Temperature in Fahrenheit:", round(f, 2))

    elif choice == 7:
        print("Exiting program... Thank you!")
        break

    else:
        print("Invalid choice! Please select between 1 and 7.")
