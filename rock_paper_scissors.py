import random

# Define the options
choices = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def play_game():
    player_score = 0
    computer_score = 0
    rounds = 0

    while True:
        print("\nRock, Paper, Scissors - Round", rounds + 1)
        print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit the game.")
        player_choice = input("Your choice: ").lower()

        if player_choice == "quit":
            break

        if player_choice not in choices:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        # Update score
        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        rounds += 1
        print(f"Score: You {player_score} - {computer_score} Computer")

    print("\nFinal score:")
    print(f"You: {player_score}")
    print(f"Computer: {computer_score}")
    print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    play_game()