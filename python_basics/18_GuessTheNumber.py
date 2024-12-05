import random

EASY = 10
HARD = 5


def game_difficulty(level):
    """Returns the number of attempts based on difficulty level."""
    if level == "hard":
        return HARD
    else:
        return EASY


def check_guess(guess, number):
    """Checks the player's guess against the target number."""
    if guess == number:
        print(f"Your guess was right! The number was {number}.")
        return True
    elif guess > number:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    return False


def game():
    """Main game function."""
    print("GuessTheNumber")
    print("Let me think of a number between 1 to 50...")

    # Get difficulty level
    level = input(
        "Choose a level of difficulty (hard or easy): ").strip().lower()
    if level not in ["hard", "easy"]:
        print("Invalid input. Please choose 'hard' or 'easy'.")
        return game()  # Restart the game for invalid input

    # Set attempts and generate the target number
    attempts = game_difficulty(level)
    number = random.randint(1, 50)

    # Game loop
    while attempts > 0:
        try:
            guess = int(
                input(f"Make a guess (remaining attempts: {attempts}): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Check the guess
        if check_guess(guess, number):
            return  # End the game if guessed correctly

        # Decrement attempts
        attempts -= 1

    # If out of attempts
    print(f"You've run out of attempts! The correct number was {number}.")


game()
