# imports
import math
import random


# Each "part" exercise is created as their
# own function. Call a function to fire a
# single part-exercise.


def part_1():
    name = input("What's your name? ")
    print(f"Hello {name}!")

#   part_1()

def part_2():
    radius = input("What's the circles radius? ")
    area = math.pi * math.pow(int(radius), 2)
    print(f"The circles area is {area}")

#   part_2()

def part_3():
    base = int(input("What's the rectangles base? "))
    height = int(input("And what is the rectangles height? "))
    area = base * height
    circuit = base * 2 + height * 2
    print(f"The rectangles area is {area}, and it's circuit is {circuit}")

#   part_3()

def part_4():
    numbers = input("Input 3 numbers. Please separate the numbers by a space.\n")
    numbers_array = numbers.split(' ')

    # Define the end-cases
    sum = 0
    product = 1
    average = 0

    for i in numbers_array:
        i = int(i)

        sum = sum + i
        product = product * i
        average = sum / len(numbers_array)

    print(f"Sum of the numbers: {sum}\n")
    print(f"Product of numbers: {product}\n")
    print(f"Average of numbers: {round(average, 2)}")

#   part_4()

def part_5():
    breads = int(input("How many breads: "))
    nails = int(input("How many nails: "))
    bullets = float(input("How many bullets: "))

    bullets_in_kg = 0.0133
    nails_in_kg = 32 * bullets_in_kg
    breads_in_kg = 20 * nails_in_kg

    kg_outcome = breads * breads_in_kg + nails * nails_in_kg + bullets * bullets_in_kg

    print(f"Weight in modern units: {kg_outcome}kg")

#   part_5()

def part_6():
    three_num_pin = ''
    four_num_pin = ''

    for i in range(1, 4):
        three_num_pin += str(random.randint(0, 9))
    
    for i in range(1, 5):
        four_num_pin += str(random.randint(1, 6))

    print(f"Three number code: {three_num_pin}")
    print(f"Four number code: {four_num_pin}")

#   part_6()