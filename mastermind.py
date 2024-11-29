# Main game logic
from codebreaker import codebreaker_mode
from codemaker import codemaker_mode
from multiplayer import multiplayer_mode
from constants import HIGH_SCORE_FILE
from utils import get_high_score


def main():
    print("Welcome to Mastermind!")
    
    high_score = get_high_score(HIGH_SCORE_FILE)
    if high_score is not None:
        print(f"Current High Score: {high_score}")
    else:
        print("No high score yet. Be the first to set one!")

    while True:
        print("\nChoose a mode:")
        print("1. You guess the code")
        print("2. Program guesses your code")
        print("3. Multiplayer Mode")
        print("4. Exit")
        choice = input("Enter 1, 2, 3, or 4: ").strip()

        if choice == '1':
            codebreaker_mode()
        elif choice == '2':
            codemaker_mode()
        elif choice == '3':
            multiplayer_mode()
        elif choice == '4':
            print("Thank you for playing Mastermind! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing Mastermind! Goodbye!")
            break

if __name__ == "__main__":
    main()

