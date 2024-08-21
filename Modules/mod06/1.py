import random

def roll_dice():
    return random.randint(1, 6)

def main():
    while (True):
        rolled_number = roll_dice()

        print(f"Rolled {rolled_number}")

        if rolled_number == 6:
            break

main()