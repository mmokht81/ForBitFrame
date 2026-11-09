import random

while True:
    a = random.randint(1, 10)
    b = 0

    while True:
        guess = int(input("Guess a number: "))
        b = b + 1

        if guess == a:
            print("Perfect dear !")
            print("You have been trying for: ", b)
            break

        elif guess < a:
            print("Bigger please: ")

        else:
            print("Lower please: ")

    again = input("Would you like to try again (y/n) ?")

    if again.lower() == "n":
        break

print("Bye Bye!")