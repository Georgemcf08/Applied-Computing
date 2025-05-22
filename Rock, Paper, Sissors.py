#Import the random function
import random

# Step 1: Ask for the user name
user_name = input("What's your name? ")

# Step 2: Greet the user
print(f"Hello, {user_name}! Let's play Rock, Paper, Scissors!")

# Step 3: Ask how many rounds the user wants (between 3 and 10)
while True:
    try:
        total_rounds = int(input("How many rounds do you want to play? (3 to 10): "))
        if 3 <= total_rounds <= 10:
            break
        else:
            print("Please enter a number between 3 and 10.")
    except ValueError:
        print("That's not a valid number. Please enter a whole number between 3 and 10.")

# Step 4: Define the possible choices
choices = ["rock", "paper", "scissors"]

# Step 5: Initialize scores
user_score = 0
computer_score = 0

# Step 6: Play the chosen number of rounds
for round_number in range(1, total_rounds + 1):
    print(f"\n--- Round {round_number} ---")
    
    # Get users choice
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Validate user's choice
    while user_choice not in choices:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()

    # pyhton randomly selects a choice
    computer_choice = random.choice(choices)
    print(f"The computer chose: {computer_choice}")

    # Determine round outcome
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print(f"{user_name}, you win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

# Step 7: Show final scores
print("\n--- Game Over ---")
print(f"{user_name}'s score: {user_score}")
print(f"Computer's score: {computer_score}")

# Step 8: prints the overall winner
if user_score > computer_score:
    print(f"Congratulations, {user_name}! You are the overall winner!")
elif computer_score > user_score:
    print("The computer wins the game! Better luck next time.")
else:
    print("It's a tie game!")
