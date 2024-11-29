# Mastermind Game - README

## Overview
This is a Python implementation of the classic **Mastermind** game, where players take turns being the "Codemaker" and the "Codebreaker." The game features multiple modes, including single-player and multiplayer, with a scoring system and feedback mechanism to enhance the gaming experience.

### Features
1. **Single-Player Mode**:
   - Play as the Codebreaker and try to guess a randomly generated secret code.
   - The program provides feedback on your guesses using "Black Pegs" and "White Pegs."

2. **Program Guesses Mode**:
   - Think of a secret code, and the program will try to guess it.
   - Provide feedback to the program as it guesses.

3. **Multiplayer Mode**:
   - Two players alternate roles as Codemaker and Codebreaker.
   - Scoring is based on the number of attempts and successful defense of the code.

4. **Scoring System**:
   - Earn points based on attempts and bonuses for quick solutions or successful code defense.
   - High scores are saved and displayed.

5. **Configurable Constants**:
   - Customize game settings such as colors, code length, and maximum attempts.

---

## File Structure
### Core Components
1. **`mastermind.py`**:
   - The main game script.
   - Handles mode selection and game flow.

2. **`codebreaker.py`**:
   - Implements the logic for the "You guess the code" mode.
   - Randomly generates a secret code and evaluates user guesses.

3. **`codemaker.py`**:
   - Implements the logic for the "Program guesses your code" mode.
   - The program filters possible codes based on feedback until it guesses the correct one.

4. **`multiplayer.py`**:
   - Implements the multiplayer mode where two players take turns guessing each other's codes.

5. **`constants.py`**:
   - Contains configurable settings:
     - Colors: `['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple']`
     - Code Length: `4`
     - Maximum Attempts: `10`

6. **`utils.py`**:
   - Utility functions for:
     - Validating guesses.
     - Calculating feedback (Black and White Pegs).
     - Reading and saving high scores.

6. **`highscore.txt`**:
   - Stores the highest score gotten in the game

---

## How to Play

### Setup
1. Ensure you have Python 3 installed.
2. Place all files in the same directory.
3. Run the game using:
   ```bash
   python mastermind.py
   ```

### Game Modes
1. **Mode 1: You guess the code**:
   - Enter guesses as space-separated colors (e.g., `Red Blue Green Yellow`).
   - The program provides feedback after each guess:
     - **Black Pegs**: Correct color in the correct position.
     - **White Pegs**: Correct color but in the wrong position.

2. **Mode 2: Program guesses your code**:
   - Think of a secret code and provide feedback as:
     - `Black White` (e.g., `2 1` for 2 Black Pegs and 1 White Peg).

3. **Mode 3: Multiplayer**:
   - One player sets the code while the other guesses.
   - Roles alternate after each round.
   - Feedback and scoring are handled interactively.

---

## Code Structure

### Key Functions
#### Codebreaker Mode (`codebreaker.py`)
- `generate_secret_code()`: Randomly generates the secret code.
- `codebreaker_mode()`: Main game loop for guessing the code.

#### Codemaker Mode (`codemaker.py`)
- `get_all_possible_codes()`: Generates all possible combinations of the code.
- `codemaker_mode()`: Program guesses the code based on feedback.

#### Multiplayer Mode (`multiplayer.py`)
- `multiplayer_mode()`: Handles rounds, role switching, and scoring.

#### Utility Functions (`utils.py`)
- `validate_guess()`: Validates user input against game rules.
- `calculate_feedback()`: Computes Black and White Pegs for a guess.
- `get_high_score()` / `save_high_score()`: Reads/writes high scores.

---

## Customization
- Edit `constants.py` to modify game settings:
  - Add more colors.
  - Change the code length.
  - Adjust the maximum attempts.

---

## Sample Output
### Single-Player Mode
```
Welcome to Mastermind!
Current High Score: 100

Choose a mode:
1. You guess the code
2. Program guesses your code
3. Multiplayer Mode
4. Exit
Enter 1, 2, 3, or 4: 1

Try to guess the secret code.
Available colors: Red, Blue, Green, Yellow, Orange, Purple
Enter your guess as 4 colors separated by spaces.
Attempt 1: Red Blue Green Yellow
Feedback: 2 Black Pegs, 1 White Peg
...
Congratulations! You guessed the code in 5 attempts.
Your score: 60
```

### Multiplayer Mode
```
Welcome to Local Multiplayer Mastermind!
Available colors: Red, Blue, Green, Yellow, Orange, Purple
The code must be 4 colors long.

Round 1: Player 1 is the Codemaker, Player 2 is the Codebreaker.

Player 1, enter your secret code: Red Blue Green Yellow
...
Player 2, Attempt 1: Red Blue Yellow Green
Feedback: 2 Black Pegs, 2 White Pegs
...
Player 2 guessed the code in 3 attempts!
Player 2 earns 70 points!
...
Final Scores:
Player 1: 50 points
Player 2: 70 points
Player 2 is the winner! 🎉
```

---

## Future Enhancements
1. Add graphical user interface (GUI) for better user experience.
2. Allow online multiplayer mode.
3. Include difficulty levels with varying code lengths and color sets.

---

## License
This project is open-source and can be modified and distributed under the [MIT License](https://opensource.org/licenses/MIT).
