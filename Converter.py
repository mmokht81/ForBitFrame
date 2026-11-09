def Temperature():
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Choose: ")
    value = float(input("Enter value: "))

    if choice == "1":
        result = (value * 9/5) + 32
    elif choice == "2":
        result = (value - 32) * 5/9
    elif choice == "3":
        result = value + 273.15
    elif choice == "4":
        result = value - 273.15
    else:
        print("Invalid choice!")
        return

    print("Result:", result)

def Weight():
    print("\n1. Kilogram to Gram")
    print("2. Gram to Kilogram")

    choice = input("Choose: ")
    value = float(input("Enter value: "))

    if choice == "1":
        result = value * 1000
    elif choice == "2":
        result = value / 1000
    else:
        print("Invalid choice!")
        return

    print("Result:", result)

def Length():
    print("\n1. Meter to Centimeter")
    print("2. Centimeter to Meter")
    print("3. Meter to Kilometer")
    print("4. Kilometer to Meter")

    choice = input("Choose: ")
    value = float(input("Enter value: "))

    if choice == "1":
        result = value * 100
    elif choice == "2":
        result = value / 100
    elif choice == "3":
        result = value / 1000
    elif choice == "4":
        result = value * 1000
    else:
        print("Invalid choice!")
        return
    
    print("Result:", result)

while True:

    print("\n===== UNIT CONVERTER =====")
    print("1. Temperature")
    print("2. Weight")
    print("3. Length")
    print("4. Exit")

    choice = input("Choose a converter: ")

    if choice == "1":
        Temperature()
    elif choice == "2":
        Weight()
    elif choice == "3":
        Length()
    elif choice == "4":
        print("bye bye!")
        break
    else:
        print("Invalid choice! Try again.")
