import random

# 2
def roll_custom_dice(dice_sides : int):
    while (True):
        rolled_value = random.randint(1, dice_sides)
        
        print(f"Rolled {rolled_value}")
        
        if rolled_value == dice_sides:
            break

def main():
    dice_sides = int(input("How many sides does the dice have: "))

    roll_custom_dice(dice_sides)

main()