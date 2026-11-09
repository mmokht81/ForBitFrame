while True:
    a = input("Enter number one OR q for exit...")

    if a.lower() == "q":
        print("Bye !")
        break

    b = input("Enter number two: ")
    operator = input("Enter operator: ")

    a = float(a)
    b = float(b)

    if operator == "+":
        print(a + b)

    elif operator == "-":
        print(a - b)

    elif operator == "*":
        print(a * b)

    elif operator == "/":
        if b == 0:
            print("Invalid input")
        else:
            print(a / b)