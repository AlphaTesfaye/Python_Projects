# Computer Quiz

This Python script is a simple computer quiz game that tests your knowledge of computer-related terms and acronyms. It presents a series of questions and evaluates the user's answers to calculate their score.

## Instructions

1. **Welcome Message:** The game starts with a welcome message inviting the user to play.
2. **Prompt to Play:** The user is asked whether they want to play the quiz. If they decline, the game quits.
3. **Quiz Start:** If the user chooses to play, the quiz begins.
4. **Questions and Answers:** The quiz consists of several multiple-choice questions about computer terms and acronyms. The user inputs their answer for each question.
5. **Scoring:** For each correct answer, the user earns a point. The final score is displayed at the end of the quiz.

## Quiz Questions

The quiz questions cover various topics related to computer terminology and acronyms. Here are some examples:

1. What does APU stand for?
2. What does ILS stand for?
3. What does VOR stand for in aviation?
4. What does MFD stand for?
5. What does ATC stand for?
6. What does TCAS stand for?

## How to Run

To play the quiz:
1. Ensure you have Python installed on your computer.
2. Download the Python script (`quiz_game.py`) from this repository.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script by executing the command `python quiz_game.py`.
5. Follow the on-screen instructions to play the quiz.

## Contributing

Contributions to this project are welcome! If you have ideas for improving the quiz or adding more questions, feel free to fork the repository and submit a pull request.





# Number Guessing Game

This Python script is a simple number guessing game where the player tries to guess a randomly generated number within a specified range.

## How the Game Works

1. **User Input:** The game prompts the user to input the upper limit of the range for the random number.
2. **Input Validation:** The script validates the user's input to ensure it is a positive integer.
3. **Random Number Generation:** Using the `random.randint()` function, a random number within the specified range is generated.
4. **Guessing Loop:** The game enters a loop where the player makes guesses.
5. **Guess Evaluation:** After each guess, the script compares the player's guess to the randomly generated number and provides feedback (higher, lower, or correct).
6. **Game Termination:** The loop continues until the player correctly guesses the number. The game then terminates, displaying the number of guesses made.

## How to Run

To play the game:
1. Ensure you have Python installed on your computer.
2. Download the Python script (`Number_Guessing_Game.py`) from this repository.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script by executing the command `python Number_Guessing_Game.py`.
5. Follow the on-screen instructions to play the game.

## Features
- **Input Validation:** The script validates user input to ensure it is a positive integer.
- **Random Number Generation:** The game generates a random number within the specified range using the `random.randint()` function.
- **Feedback Mechanism:** After each guess, the player receives feedback on whether their guess was higher, lower, or correct.
- **Guess Counter:** The script keeps track of the number of guesses made by the player and displays it at the end of the game.

## Contributing

Contributions to this project are welcome! If you have ideas for improving the game or adding new features, feel free to fork the repository and submit a pull request.




# Rock-Paper-Scissors Game

This Python script is a simple rock-paper-scissors game where the player competes against the computer. The game continues until the player decides to quit by entering "Q".

## How the Game Works

1. **User Input:** The game prompts the user to input their choice of "rock," "paper," or "scissors," or to quit by entering "Q."
2. **Input Validation:** The script validates the user's input to ensure it is one of the specified options or "Q" to quit.
3. **Computer Selection:** The script randomly selects one of the three options ("rock," "paper," or "scissors") for the computer.
4. **Comparison and Outcome:** The user's choice is compared to the computer's selection to determine the winner. The outcome is displayed to the user, indicating whether they won or lost.
5. **Score Tracking:** The script keeps track of the number of wins for both the user and the computer.
6. **Game Termination:** The game continues until the user decides to quit by entering "Q." After quitting, the final scores are displayed, and the game ends.

## How to Run

To play the game:
1. Ensure you have Python installed on your computer.
2. Download the Python script (`Rock_Paper_Scissors.py`) from this repository.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script by executing the command `Rock_Paper_Scissors.py`.
5. Follow the on-screen instructions to play the game.

## Features
- **Input Validation:** The script validates user input to ensure it is one of the specified options or "Q" to quit.
- **Random Selection:** The computer's choice is randomly selected from the available options using the `random.randint()` function.
- **Outcome Determination:** The script compares the user's choice to the computer's selection to determine the winner.
- **Score Tracking:** The script keeps track of the number of wins for both the user and the computer.
- **Game Termination:** The game continues until the user decides to quit by entering "Q." Upon quitting, the final scores are displayed.

## Contributing

Contributions to this project are welcome! If you have ideas for improving the game or adding new features, feel free to fork the repository and submit a pull request.





# Adventure Game

This Python script is an adventure game where the player embarks on a journey through a dense forest, facing various choices and challenges along the way.

## How the Game Works

1. **Introduction:** The game starts with a welcome message and an introduction to the setting: a crossroads in the middle of a dense forest.
2. **First Choice:** The player must choose between two paths: entering a dark cave or exploring a mysterious forest.
3. **Cave Exploration:** If the player chooses to enter the cave, they encounter a hidden chamber with a treasure chest. They must decide whether to open the chest or leave the cave.
4. **Forest Exploration:** If the player chooses to explore the forest, they encounter a fork in the path. They must choose between taking an uphill path or a downhill path.
5. **Glade Encounter:** If the player chooses the downhill path, they stumble upon a hidden glade where a mystical creature offers them a choice between a magical boon or a dangerous curse.
6. **Outcome Determination:** The game evaluates the player's choices and provides different outcomes based on their decisions.
7. **Game Over:** The game ends if the player makes an invalid choice or fails to make a decision, resulting in their adventure coming to an unfortunate end.

## Features
- **Multiple Endings:** The game offers multiple endings based on the player's choices, encouraging replayability.
- **Interactive Storytelling:** Players make decisions that influence the outcome of their adventure, adding an element of storytelling and immersion.
- **Simple Gameplay:** The game mechanics are straightforward, making it accessible to players of all ages and skill levels.

## How to Run

To play the game:
1. Ensure you have Python installed on your computer.
2. Download the Python script (`Choose_your_own_adventure book.py`) from this repository.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script by executing the command `python Choose_your_own_adventure book.py`.
5. Follow the on-screen instructions to play the game.

## Contributing

Contributions to this project are welcome! If you have ideas for expanding the game, adding new story branches, or improving the user experience, feel free to fork the repository and submit a pull request.

# Password Manager

This Python script is a simple password manager that allows users to store and retrieve passwords securely using encryption.

## Features

- **Secure Encryption:** Passwords are encrypted using the Fernet symmetric encryption scheme from the `cryptography` library, ensuring data security.
- **User-Friendly Interface:** The script provides a menu-based interface for users to view stored passwords, add new passwords, and quit the application.
- **Automatic Key Generation:** If the encryption key (`key.key`) does not exist, the script generates a new key to ensure data integrity.
- **Clear Error Handling:** The script includes error handling to handle file not found errors and invalid user input, providing clear error messages to the user.
- **Persistent Storage:** Passwords are stored in a text file (`password.txt`) for persistent storage between sessions.

## How to Use

1. **Clone the Repository:** Clone this repository to your local machine.
2. **Install Dependencies:** Make sure you have Python installed on your computer. Install the required dependencies using `pip install -r requirements.txt`.
3. **Run the Script:** Execute the script by running `python Password_Manager.py` in your terminal or command prompt.
4. **Menu Options:**
   - **View Stored Passwords (1):** View all stored usernames and decrypted passwords.
   - **Add a New Password (2):** Add a new username and password to the storage.
   - **Quit (3):** Exit the password manager application.

## File Structure

- `Password_Manager.py`: The main Python script containing the password manager functionality.
- `key.key`: The encryption key file. If not present, the script generates a new key.
- `password.txt`: The file where encrypted passwords are stored.

## Contributing

Contributions to this project are welcome! If you have ideas for improving the password manager or adding new features, feel free to fork the repository and submit a pull request.


