# User guesses program's code

import random
from constants import COLORS, CODE_LENGTH, MAX_ATTEMPTS, HIGH_SCORE_FILE
from utils import validate_guess, calculate_feedback, get_high_score, save_high_score

def generate_secret_code():
    secret_code = []  
    for _ in range(CODE_LENGTH): 
        #random.choice(COLORS): Selects a random color from the COLORS list.
        random_color = random.choice(COLORS)  
        secret_code.append(random_color)  
    return secret_code 


def codebreaker_mode():
    secret_code = generate_secret_code()
    print("\nTry to guess the secret code.")
    print(f"the available colors to use are: {', '.join(COLORS)}")
    print(f"Enter your guess as {CODE_LENGTH} colors separated by spaces.")

    high_score = get_high_score(HIGH_SCORE_FILE)
    print(f"Current High Score: {high_score if high_score is not None else 'None'}")

    score = 0  # Initialize score
    attempt = 1

    while attempt <= MAX_ATTEMPTS:

        '''
        strip()-Removes leading and trailing spaces.
        title()-Capitalizes the first letter of each word (lowercases others).
        split()Splits the string into a list of words.
        '''
        guess_input = input(f"Attempt {attempt}: ").strip().title().split()


        is_valid, message = validate_guess(guess_input, COLORS, CODE_LENGTH)
        if not is_valid:
            print(message)
            continue

        black_pegs, white_pegs = calculate_feedback(secret_code, guess_input)
        
        black_pegs_label = f"Black Peg{'s' if black_pegs != 1 else ''}"

        white_pegs_label = f"White Peg{'s' if white_pegs != 1 else ''}"

        # Print the feedback with proper pluralization
        print(f"Feedback: {black_pegs} {black_pegs_label}, {white_pegs} {white_pegs_label}")

        if black_pegs == CODE_LENGTH:
            score += (MAX_ATTEMPTS - attempt + 1) * 10

            # Bonus for quick win
            if attempt == 1:
                score += 50  # First-try bonus
                print("Amazing! You guessed the code on the first try! Bonus: 50 points!")


            print(f"Congratulations! You guessed the code in {attempt} attempts.")
            print(f"Your score: {score}")

            # Check for new high score
            if high_score is None or score > high_score:
                save_high_score(HIGH_SCORE_FILE, score)
                print("New High Score!")
            return

        attempt += 1

    print(f"Sorry, you've used all {MAX_ATTEMPTS} attempts. The secret code was: {' '.join(secret_code)}")
    print(f"Your score: {score}")