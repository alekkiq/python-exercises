# imports
import math
import random


# 1
def print_divisible_by_three():
    i = 1
    while i < 1000:
        if i % 3 == 0:
            print(i)
        i = i + 1
        
#   print_divisible_by_three()

# 2
def inches_to_cm():
    while (True):
        inch = float(input("Convert inches to centimeters (Input a negative value to end):\n"))

        if inch <= 0:
            print("Thanks for using our app!")
            break

        print(f"{inch} inch is {round(inch * 2.54, 3)} centimeters")

#   inches_to_cm()

# 3
def print_largest_and_smallest():
    inputted_numbers = []

    while (True):
        number = input("Input a number (Input nothing to end): ")

        if number == "":
            print(f"Smallest number inputted: {min(inputted_numbers)}")
            print(f"Largest number inputted: {max(inputted_numbers)}")
            break

        inputted_numbers.append(int(number))

#   print_largest_and_smallest()

# 4
def guessing_game():
    rolled_number = random.randint(1, 10)

    while (True):
        guess = int(input("Guess a number between 1 and 10: "))

        if guess is rolled_number:
            print("Correct!")
            break
        elif guess > rolled_number:
            print("Too high guess.")
            continue
        elif guess < rolled_number:
            print("Too low guess")
            continue
        else:
            print("Invalid guess! The value has to be between 1 and 10")
            continue


#   guessing_game()

# 5
def login_guess():
    correct_username = "python"
    correct_password = "rules"

    tries = 3

    while (True):
        if tries == 0:
            print("You used all your tries. Try again later")
            break

        username = str(input("Username: "))
        password = str(input("Password: "))

        if username == correct_username and password == correct_password:
            print("Welcome!")
            break
        else:
            tries = tries - 1
            print(f"Access denied. {tries} tries left.")

#   login_guess()

# 6
def pi_floating_point():
    print("Mitä vittua?")
    # TODO