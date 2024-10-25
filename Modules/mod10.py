import random
import string

# needed in exercises 1 - 3
from Classes.Building import Building

# needed in exercise 4
from Classes.Car import Car
from Classes.Race import Race

def elevator_main():
    building = Building(10, 1, 5)

    # fire alarm will occur after 1-7 moves of an elevator
    moves_before_alarm = random.randint(1, 7)

    # loop for just moving around with elevators
    while moves_before_alarm >= 0:
        chosen_elevator_number = int(input(f"The house has {building.elevator_count} elevators. Which one to use: "))

        chosen_elevator = building.elevators[chosen_elevator_number - 1]

        print(f"Elevator {chosen_elevator.product_number}, current floor {chosen_elevator.current_floor}\n")

        destination = int(input(f"Which floor to go {building.lowest_floor} - {building.highest_floor}: "))

        building.move_elevator(chosen_elevator_number, destination)
        
        print(f"Elevator {chosen_elevator.product_number}, current floor {chosen_elevator.current_floor}")

        moves_before_alarm -= 1
    
    building.fire_alarm()

    for elevator in building.elevators:
        print(f"Elevator {elevator.product_number} moved to bottom floor {building.lowest_floor}")

    print("There was a fire alarm. All elevators moved to the bottom floor. Everyone must leave the building immediately!")

#   elevator_main()

# 4
def race_main():
    cars = []
    
    for i in range(1, 11): # create 10 cars 1-10
        speed = random.randint(100, 200)
        registration = f"{''.join(random.choice(string.ascii_letters).upper() for _ in range(3))}-{random.randint(1, 9)}"
        car = Car(registration, speed)
        car.accelerate(random.randint(-10, 15)) # set the cars initial speed
        cars.append(car)
            
    race = Race("The grand scrap race", 8000, cars)
    
    print("Starting statistics:\n")
    race.get_race_state()
    
    # track the hours driven
    hours_driven = 0

    while not race.race_over()["state"]:
        race.hour_passes()
        hours_driven += 1
        
        if hours_driven % 10 == 0:
            print(f"\nStatistics after {hours_driven} hours driven:\n")
            race.get_race_state()
        
    print(f"\nThe race is over after {hours_driven} hours driven. Car {race.race_over()["winning_car"]} has won!")
    print(f"\nThe final standings:\n")
    race.get_race_state(sort=True)
    
#   race_main()