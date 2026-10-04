import random

choices = ["rock", "paper", "scissors"]

user = input("Choose rock, paper, or scissors: ").lower()
computer = random.choice(choices)

print("You chose:", user)
print("Computer chose:", computer)

if user not in choices:
    print("Invalid choice.")

elif user == computer:
    print("It's a tie!")

elif (user == "rock" and computer == "scissors") or \
     (user == "scissors" and computer == "paper") or \
     (user == "paper" and computer == "rock"):
    print("You win!")

else:
    print("Computer wins!")