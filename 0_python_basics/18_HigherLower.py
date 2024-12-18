import random
import HigherLowerData as hld
import os
import platform


def clear_console():
    # Check the platform and execute the proper command
    command = "cls" if platform.system() == "Windows" else "clear"
    os.system(command)


def compare_celeb(a, b):
    """
    Compares the follower counts of two celebrities.
    Returns 1 if 'a' is greater or equal to 'b', else 2.
    """
    if a >= b:
        return 1
    else:
        return 2


def game():
    print(hld.game_logo)
    flag = True
    score = 0
    while flag:
        # Randomly select two celebrities from the data
        compare_list = random.sample(hld.data, 2)

        # Print details of the two celebrities
        print(f"Compare 1: {compare_list[0]['name']}, {
              compare_list[0]['description']}, {compare_list[0]['country']}")
        print(hld.vs)
        print(f"Compare 2: {compare_list[1]['name']}, {
              compare_list[1]['description']}, {compare_list[1]['country']}")

        # Retrieve their follower counts
        compare1 = compare_list[0]["follower_count"]
        compare2 = compare_list[1]["follower_count"]

        # Determine the correct answer
        res = compare_celeb(compare1, compare2)

        # Get the user's guess
        try:
            guess = int(input("Who has more followers? Type '1' or '2': "))
            if guess != 1 and guess != 2:
                raise ValueError
        except ValueError:
            print("Invalid input! Please type '1' or '2'.")
            continue

        # Check if the guess is correct
        if guess == res:
            score += 1
            clear_console()
            print(f"You're right! Current score: {score}")
        else:
            clear_console()
            print(f"You're wrong... Final score: {score}")
            flag = False


game()
