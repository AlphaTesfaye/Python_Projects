import random

# Function to roll a dice
def roll_dice():
    return random.randint(1, 6)

# Function to prompt the number of players
def get_num_players():
    while True:
        num_players = input("Enter the number of players (1-4): ")
        if num_players.isdigit():
            num_players = int(num_players)
            if 1 <= num_players <= 4:
                return num_players
            else:
                print("Number of players must be between 1 and 4.")
        else:
            print("Invalid input. Please enter a number.")

# Main function to play the game
def play_game():
    num_players = get_num_players()
    max_score = 50
    players_scores = [0] * num_players

    while max(players_scores) < max_score:
        for player_idx in range(num_players):
            print("\nPlayer", player_idx + 1, "'s turn:\n")
            current_score = 0

            while True:
                roll_choice = input("Roll the dice? (y/n): ").lower()
                if roll_choice != "y":
                    break
                dice_roll = roll_dice()
                print("You rolled:", dice_roll)

                if dice_roll == 1:
                    print("You rolled a 1! Turn over.")
                    current_score = 0
                    break
                else:
                    current_score += dice_roll

            print("Turn score:", current_score)
            players_scores[player_idx] += current_score
            print("Total score:", players_scores[player_idx])

            # Check for winner
            if players_scores[player_idx] >= max_score:
                print("Player", player_idx + 1, "wins!")

            # Prompt for a rematch
            if input("Continue to the next player's turn? (y/n): ").lower() != "y":
                return

# Run the game
if __name__ == "__main__":
    print("Welcome to the Dice Game!")
    play_game()
