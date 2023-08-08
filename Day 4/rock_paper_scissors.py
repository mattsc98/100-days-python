import random

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

r_p_c = ["rock", "paper", "scissors"]

human_choice = r_p_c[int(choice)]
computer_choice = r_p_c[random.randint(0, 2)]

print(f"Computer chooses.....{computer_choice}!")

if(human_choice == "rock" and computer_choice == "paper"):
    print("You lose")
elif(human_choice == "rock" and computer_choice == "scissors"):
    print("You win")
elif(human_choice == "paper" and computer_choice == "rock"):
    print("You win")
elif(human_choice == "paper" and computer_choice == "scissors"):
    print("You lose")
elif(human_choice == "scissors" and computer_choice == "rock"):
    print("You lose")
elif(human_choice == "scissors" and computer_choice == "paper"):
    print("You win")
else:
    print("Draw")