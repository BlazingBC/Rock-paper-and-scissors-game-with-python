import random

user_wins = 0
computer_wins = 0

print("Quit your game after finishing the play to view your score")
options = ["ROCK", "PAPER", "SCISSORS"]

while (True):
    user_choice = input("Type ROCK/PAPER/SCISSORS or Q to quit: ").upper()
    if (user_choice) == "Q":
        break

    if (user_choice not in options):
        continue

    random_number = random.randint(0, 2)
    
    computer_choice = options[random_number]
    print("Computer picked", computer_choice + ".")

    if (user_choice == "ROCK" and computer_choice == "SCISSORS"):
        print("You won!")
        user_wins = user_wins+1

    elif (user_choice == "PAPER" and computer_choice == "ROCK"):
        print("You won!")
        user_wins = user_wins+1

    elif (user_choice == "SCISSORS" and computer_choice == "PAPER"):
        print("You won!")
        user_wins = user_wins+1
    
    elif (user_choice == computer_choice):
        print("Neutralized!")

    else:
        print("You lost!")
        computer_wins = computer_wins+1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")

difference = user_wins - computer_wins
differ = computer_wins - user_wins

if (user_wins > computer_wins):
    print("you have woon with a differnce of ", difference)
    
elif (user_wins < computer_wins):
    print("you loss with a difference of ", differ)
    print("Better luck next time")

else:
    print("Neutralized result")
    