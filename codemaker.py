 # Program guesses user's code
 # codemaker.py
import random
from constants import COLORS, CODE_LENGTH, MAX_ATTEMPTS
from utils import calculate_feedback
from itertools import product

# Function to generate all possible codes
def get_all_possible_codes():
    # Generate a list of all possible codes using Cartesian product of COLORS repeated CODE_LENGTH times.
    # Each code is a tuple of length CODE_LENGTH with colors chosen from COLORS.
    return list(product(COLORS, repeat=CODE_LENGTH))

def codemaker_mode():
    print("\nThink of a secret code.")
    print(f"Available colors: {', '.join(COLORS)}")
    print(f"The code is {CODE_LENGTH} colors long.")

    # Initialize possible codes
    possible_codes = get_all_possible_codes()
    attempts = 0
    last_guess = None

    while attempts < MAX_ATTEMPTS and possible_codes:
        attempts += 1

        # Make the first guess randomly, or reuse the last filtered guess
        if not last_guess:
            guess = list(random.choice(possible_codes))
        else:
            guess = list(last_guess)

        print(f"Program's guess #{attempts}: {' '.join(guess)}")
        feedback_input = input("Enter feedback as 'Black White': ").strip().split()

        # Check if feedback input is valid
        if len(feedback_input) != 2:
            print("Invalid feedback format. Please enter two numbers separated by space.")
            attempts -= 1 # Invalid feedback does not count as an attempt
            continue
        try:
            black_pegs, white_pegs = map(int, feedback_input) # Convert feedback to integers
        except ValueError:
            print("Invalid numbers. Please enter integers for feedback.")
            attempts -= 1 # Invalid feedback does not count as an attempt
            continue

        if black_pegs == CODE_LENGTH:
            print(f"The program guessed your code in {attempts} attempts!")
            return

        # Filter possible codes based on feedback
        filtered_codes = []
        for code in possible_codes:
            # Calculate the feedback for the current code against the program's guess
            feedback_for_code = calculate_feedback(code, guess)

            if feedback_for_code == (black_pegs, white_pegs):
                filtered_codes.append(code)

        possible_codes = filtered_codes

        if not possible_codes:
            print("No possible codes match the feedback. Please check your feedback inputs.")
            return

        last_guess = possible_codes[0]

    print("The program couldn't guess your code within the maximum attempts.")
