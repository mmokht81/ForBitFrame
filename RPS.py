import random

while True:
    
    user_choice = input("Enter your choice (rock, paper, scissors) OR enter exit: ")
    actions = ["rock", "paper", "scissors", "exit"]
    pc_respond = random.choice(actions)

    if user_choice == "exit":
        break
    
    print(f"\nYou chose {user_choice}, Computer chose is {pc_respond}. \n")

    if user_choice == pc_respond:
        print(f"Both players selected {user_choice}. It's a tie!\n")
        
    elif user_choice == "rock":
        if pc_respond == "scissors":
            print("Rock smashes scissors! You win!\n")
        else:
            print("Paper covers rock! You lose.\n")

    elif user_choice == "paper":
        if pc_respond == "rock":
            print("Paper covers rock! You win!\n")
        else:
            print("Scissors cuts paper! You lose.\n")

    elif user_choice == "scissors":
        if pc_respond == "paper":
            print("Scissors cuts paper! You win!\n")
        else:
            print("Rock smashes scissors! You lose.\n")
            
print("Bye Bye!")