import random
print("Let's play rock, paper, scissors!")

#player chooses option
player_choice = input("rock, paper, or scissors?: ")

#list with computer choices, computer chooses randomly
c_choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(c_choices)

#draw scenario
if computer_choice == player_choice:
    print("Computer chose", computer_choice, "It's a draw.")

#computer chooses rock scenario
elif computer_choice == "rock":
    if player_choice == "scissors":
        print("Computer chose rock. You win!")
    else:
        print("Computer chose rock. You lose... better luck next time!")

#computer chooses paper scenario
elif computer_choice == "paper":
    if player_choice == "scissors":
        print("Computer chose paper. You win!")
    else:
        print("Computer chose paper. You lose... better luck next time!")
         
#computer chooses scissors scenario
elif computer_choice == "scissors":
    if player_choice == "rock":
        print("Computer chose scissors. You win!")
    else:
        print("Computer chose scissors. You lose... better luck next time!")