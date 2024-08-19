# imports
import math
import random


# Each "part" exercise is created as their
# own function. Call a function to fire a
# single part-exercise.


def part_1():
    zander_length = int(input("How long is the zander (cm)? "))
    allowed_length = 37 # centimeters

    if (zander_length < allowed_length):
        print(f"The zander is too small. \nYou must release it immediately. \nIt was short of the allowed length by {allowed_length - zander_length} cm.")

    else:
        print("The fish is allowed size! You are allowed to keep it.")

#   part_1()

def part_2():
    allowed_classes = ["LUX", "A", "B", "C"]

    cabin_class = str(input("What is your cabins class?\n").upper())

    if cabin_class in allowed_classes:
        match cabin_class:
            case "LUX":
                print("LUX is a cabin with a balcony in the upper deck.")
            case "A":
                print("A is a windowed cabin above the car deck.")
            case "B":
                print("B is a windowless cabin above the car deck.")
            case "C":
                print("C is a windowless cabin below the car deck.")
            # No need for a default case since we cant have a "wrong" value.
    else:
        print("Error! Cabin class not found. Try with another class.")

#   part_2()

def part_3():
    print()
    # this is an annoying one, skip

#   part_3()

def part_4():
    year = int(input("Input a year: "))

    is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    if is_leap_year:
        print(f"The year {year} is a leap year.")
    else:
        print(f"The year {year} is not a leap year.")

#   part_4()