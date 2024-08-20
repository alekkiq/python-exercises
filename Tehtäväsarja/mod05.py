# imports
import math
import random


# 1
def roll_dices():
    dices_amount = int(input("How many dices to roll?\n"))
    dices_list = list(range(1, dices_amount + 1))

    sum = 0

    for dice in dices_list:
        rolled_value = random.randint(1, 6)
        sum += rolled_value
        print(f"Dice {dice} rolled {rolled_value}. The current sum is {sum}")

    print(f"Rolled {dices_amount} dices, the sum of the values is {sum}")

#   roll_dices()

# 2
def print_five_largest():
    inputted_numbers = []

    while (True):
        number = input("Input a number (input empty to end): ")
        
        if number == '':
            sorted_numbers = sorted(inputted_numbers, reverse=True)

            five_largest = []

            for index, num in enumerate(sorted_numbers):
                if index < 5:
                    five_largest.append(str(num))

            print(f"The five largest numbers are {", ".join(five_largest)}")

            break
        else:
            inputted_numbers.append(int(number))

#   print_five_largest()

# 3
def prime_number():
    number = int(input("Input a number: "))
    numbers_to_test = list(range(1, number + 1))

    can_divide = []

    for num in numbers_to_test:
        if number % num == 0:
            can_divide.append(str(num))
    
    if len(can_divide) == 2:
        print(f"The number {number} is a prime number.")
    else:
        print(f"The number {number} is not a prime number.\nIt is divisible by {", ".join(can_divide)}")

#   prime_number()

# 4
def print_cities():
    cities = []

    for i in range(5):
        city = input("Input a city: ")
        cities.append(city)

    for city in cities:
        print(city)

#   print_cities()