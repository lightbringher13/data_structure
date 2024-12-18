import os
import platform
import coffee_machine_resources as cmr


def clear_console():
    command = "cls" if platform.system() == "Windows" else "clear"
    os.system(command)


def report():
    print("Current Coffee Machine Resources:")
    for key, value in cmr.coffee_machine_resources.items():
        print(f"{key}: {value}")
    print()


def exchange(menu, customer_pay):
    change = customer_pay - cmr.MENU[menu]["cost"]
    if cmr.coffee_machine_resources["money"] >= change:
        print(f"Here is your change: {change}Rs")
        cmr.coffee_machine_resources["money"] -= change
    else:
        print(
            "Coffee machine doesn't have enough money for change. Please try again later.")


def make_coffee(menu):
    # Check if resources are sufficient
    if cmr.MENU[menu]["ingredients"]["water"] > cmr.coffee_machine_resources["water"]:
        print("Not enough water.")
        return False
    if cmr.MENU[menu]["ingredients"]["coffee"] > cmr.coffee_machine_resources["coffee"]:
        print("Not enough coffee.")
        return False
    if "milk" in cmr.MENU[menu]["ingredients"]:
        if cmr.MENU[menu]["ingredients"]["milk"] > cmr.coffee_machine_resources["milk"]:
            print("Not enough milk.")
            return False

    # Deduct resources
    cmr.coffee_machine_resources["water"] -= cmr.MENU[menu]["ingredients"]["water"]
    cmr.coffee_machine_resources["coffee"] -= cmr.MENU[menu]["ingredients"]["coffee"]
    if "milk" in cmr.MENU[menu]["ingredients"]:
        cmr.coffee_machine_resources["milk"] -= cmr.MENU[menu]["ingredients"]["milk"]

    print(f"Here is your {menu}. Enjoy!")
    return True


def coffee_machine():
    flag = True
    while flag:
        menu = input(
            "What would you like to have? (latte/espresso/cappuccino/report/off): ").lower()

        if menu == "report":
            report()
            continue
        if menu == "off":
            flag = False
            print("Turning off the coffee machine.")
            break

        if menu not in cmr.MENU:
            print("Invalid selection. Please choose from the menu.")
            continue

        print("Please insert coins: ")
        coin5 = int(input("How many 5Rs coins? "))
        coin10 = int(input("How many 10Rs coins? "))
        coin20 = int(input("How many 20Rs coins? "))
        customer_pay = 5 * coin5 + 10 * coin10 + 20 * coin20

        # Update machine's money
        cmr.coffee_machine_resources["money"] += customer_pay

        if customer_pay >= cmr.MENU[menu]["cost"]:
            exchange(menu, customer_pay)
            if make_coffee(menu):
                continue
        else:
            additional = cmr.MENU[menu]["cost"] - customer_pay
            print(f"Not enough money. You need an additional {additional}Rs.")

        print()


coffee_machine()
