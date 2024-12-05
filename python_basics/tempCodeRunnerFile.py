import random

EASY = 10
HARD = 5


def game_difficulty(level):
    if level == "hard":
        return HARD
    else:
        return EASY


def check_guess(guess, number, attempts):
    print(f"you have remaining {attempts} attempts to guess the number")
    if guess == number:
        print(f"your guess was right. the number was {number}")
        return True
    elif guess > number:
        print("your guess is too high")
        return attempts - 1
    else:
        print("your guess is too low")
        return attempts - 1


def game():
    print("GuessTheNumber")
    print("let me think of a number between 1 to 50.")
    level = input("choose level of difficulty hard or easy: ")
    if level not in ["hard", "easy"]:
        print("invalid input.")
        game()
    attempts = game_difficulty(level)
    number = random.randint(1, 50)
    print(number)
    flag = True
    while flag:
        try:
            guess = int(input("make a guess: "))
        except ValueError:
            print("invalid input. try again")
            continue
        attempts = check_guess(guess, number, attempts)
        if attempts == 0:
            print("you lose.")
        elif attempts == True:
            print("your answer was right")


game()
