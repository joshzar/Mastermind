import os

def get_high_score(file_path):
    """
    Reads the high score from a file.
    Returns None if the file does not exist or is empty.
    """
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as file:
        try:
            return int(file.read().strip())
        except ValueError:
            return None


def save_high_score(file_path, score):
    """
    Saves the high score to a file.
    """
    with open(file_path, 'w') as file:
        file.write(str(score))

'''
Parameters
guess: A list of colors guessed by the player.
colors: A list of valid colors the player is allowed to choose from. Should be the COLOR constant from utils.
code_length: The expected number of colors in the guess.

Output:
A tuple
First Value (True or False): Indicates whether the guess is valid.
Second Value (Message): An error message if the guess is invalid; otherwise, an empty string.

'''
def validate_guess(guess, colors, code_length):
    if len(guess) != code_length:
        return False, f"Guess must be {code_length} colors."
    for color in guess:
        if color not in colors:
            return False, f"Invalid color: {color}. Choose from {', '.join(colors)}."
    return True, ""

'''
Parameters:
    secret: A sequence (e.g., list or string) representing the secret code.
    guess: A sequence of the same length as secret, representing the player's guess.

Output:
    A tuple (black_pegs (correct color and position), white_pegs(correct color but wrong position)).
'''
def calculate_feedback(secret, guess):
    black_pegs = 0
    for s, g in zip(secret, guess):
        if s == g:
            black_pegs += 1

    '''
    creates a dict for secret and guess to see the count of each color

    example
    secret = ['Red', 'Green', 'Blue', 'Yellow']
    guess = ['Red', 'Blue', 'Green', 'Green']

    Colors in secret (ignoring matched positions): 'Green': 1, 'Blue': 1, 'Yellow': 1
    Colors in guess (ignoring matched positions): 'Blue': 1, 'Green': 2

    '''
    secret_color_counts = {}
    guess_color_counts = {}
    

    for s, g in zip(secret, guess):
        if s != g:
            if s in secret_color_counts:
                secret_color_counts[s] += 1
            else:
                secret_color_counts[s] = 1
            
            if g in guess_color_counts:
                guess_color_counts[g] += 1
            else:
                guess_color_counts[g] = 1

    # Calculate white pegs (correct colors in wrong positions)
    white_pegs = 0
    for color in guess_color_counts:
        # Compare counts of each color in secret and guess
        
        '''
        example from above
        'Blue': min(secret['Blue'] = 1, guess['Blue'] = 1) = 1
        'Green': min(secret['Green'] = 1, guess['Green'] = 2) = 1
        '''

        if color in secret_color_counts:
            white_pegs += min(secret_color_counts[color], guess_color_counts[color])

    return black_pegs, white_pegs
