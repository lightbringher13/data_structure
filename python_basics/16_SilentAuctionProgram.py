import os
import platform


def clear_console():
    """Clears the console based on the operating system."""
    command = "cls" if platform.system() == "Windows" else "clear"
    os.system(command)


def find_winner(bid):
    """Finds and prints the winner of the auction."""
    max_bid = 0
    winner = ""
    for name, price in bid.items():
        if price > max_bid:
            winner = name
            max_bid = price
    clear_console()
    print("Auction Results:")
    print(bid)
    print(f"The Winner is {winner} with a bid of ${max_bid}")


# Main Program
flag = True
bids = {}

while flag:
    # Input for name
    name = input("What is your name? ").strip()
    if not name.isalpha():
        print("Invalid input. Names should contain only letters. Try again.")
        continue

    # Input for bid
    try:
        price = int(input("What is your bid? ").strip())
        if price <= 0:
            print("Invalid input. Bid must be greater than 0. Try again.")
            continue
    except ValueError:
        print("Invalid input. Please enter a valid number for the bid.")
        continue

    # Store the bid
    bids[name] = price
    print(f"Thank you, {name}. Your bid of ${price} has been recorded.")

    # Check for more bidders
    con = input("Are there any other bidders? Type yes/no: ").strip().lower()
    if con == "no":
        find_winner(bids)
        flag = False
    elif con == "yes":
        clear_console()
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        clear_console()
