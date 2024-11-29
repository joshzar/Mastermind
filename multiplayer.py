from codebreaker import codebreaker_mode
from codemaker import codemaker_mode
from constants import HIGH_SCORE_FILE, CODE_LENGTH, MAX_ATTEMPTS, COLORS
from utils import get_high_score, save_high_score, validate_guess, calculate_feedback

def multiplayer_mode():
    print("\nWelcome to Local Multiplayer Mastermind!")
    print("In this mode, players take turns as Codemaker and Codebreaker.")
    print(f"Available colors: {', '.join(COLORS)}")
    print(f"The code must be {CODE_LENGTH} colors long.")

    player_scores = {"Player 1": 0, "Player 2": 0}
    rounds_played = 0

    while True:
        # Decide roles
        codemaker = "Player 1" if rounds_played % 2 == 0 else "Player 2"
        codebreaker = "Player 2" if codemaker == "Player 1" else "Player 1"
        
        print(f"\nRound {rounds_played + 1}: {codemaker} is the Codemaker, {codebreaker} is the Codebreaker.")
        
        # Codemaker sets the code
        while True:
            secret_code_input = input(f"{codemaker}, enter your secret code ({CODE_LENGTH} colors, space-separated): ").strip().title().split()
            is_valid, message = validate_guess(secret_code_input, COLORS, CODE_LENGTH)
            if is_valid:
                break
            print(message)
        secret_code = secret_code_input
        print("\n" * 50)  # Clear screen for privacy
        
        # Codebreaker tries to guess
        attempts = 1
        while attempts <= MAX_ATTEMPTS:
            guess_input = input(f"{codebreaker}, Attempt {attempts}: ").strip().title().split()
            is_valid, message = validate_guess(guess_input, COLORS, CODE_LENGTH)
            if not is_valid:
                print(message)
                continue

            black_pegs, white_pegs = calculate_feedback(secret_code, guess_input)
            print(f"Feedback: {black_pegs} Black Peg{'s' if black_pegs != 1 else ''}, {white_pegs} White Peg{'s' if white_pegs != 1 else ''}")

            if black_pegs == CODE_LENGTH:
                print(f"{codebreaker} guessed the code in {attempts} attempts!")
                # Award score based on remaining attempts
                points = (MAX_ATTEMPTS - attempts + 1) * 10
                player_scores[codebreaker] += points
                print(f"{codebreaker} earns {points} points!")
                break

            attempts += 1

        if attempts > MAX_ATTEMPTS:
            print(f"{codebreaker} couldn't guess the code. The secret code was: {' '.join(secret_code)}")
            print(f"{codemaker} earns 50 points for a successful defense!")
            player_scores[codemaker] += 50

        # Display current scores
        print("\nCurrent Scores:")
        for player, score in player_scores.items():
            print(f"{player}: {score} points")

        # Ask if they want another round
        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nFinal Scores:")
            for player, score in player_scores.items():
                print(f"{player}: {score} points")


            # Determine the winner
            if player_scores["Player 1"] > player_scores["Player 2"]:
                print("Player 1 is the winner! 🎉")
            elif player_scores["Player 1"] < player_scores["Player 2"]:
                print("Player 2 is the winner! 🎉")
            else:
                print("It's a tie! 🤝")
            
            print("Thank you for playing Multiplayer Mastermind!")
            break

        rounds_played += 1