# In this file the exercises 1 - 3 in Module 10 are
# blended together, since they all revolve around
# the Elevator class. So the "exercise" in this file
# is essentially just exercise 3.

import random

# needed in exercise 4
from mod09 import Car

class Elevator:
    def __init__(self, current_floor: int = 1, highest_floor: int = 1, lowest_floor: int = 0, product_number: str = ""):
        self.product_number = product_number
        self.highest_floor = highest_floor
        self.lowest_floor = lowest_floor
        self.current_floor = current_floor

    def floor_up(self, current_floor: int):
        return current_floor + 1
    
    def floor_down(self, current_floor: int):
        return current_floor - 1
    
    def change_floor(self, destination: int):
        '''
        Changes the Elevators floor to a given *destination*.
        '''

        if destination > self.highest_floor or destination < self.lowest_floor or destination < 0:
            return print("Invalid floor number.")
       
        for floor in range(self.current_floor, destination, (-1 if self.current_floor > destination else 1)):
            if self.current_floor > destination:
                self.current_floor = self.floor_down(floor)
            elif self.current_floor < destination:
                self.current_floor = self.floor_up(floor)

class Building:
    def __init__(self, highest_floor: int = 1, lowest_floor: int = 0, elevator_count: int = 1):
        self.highest_floor = highest_floor
        self.lowest_floor = lowest_floor
        self.elevator_count = elevator_count
        self.elevators = []

        if elevator_count > 0:
            for i in range(1, self.elevator_count + 1):
                elevator = Elevator(self.lowest_floor, self.highest_floor, self.lowest_floor, f"EL{i}")
                self.elevators.append(elevator)     

    def move_elevator(self, elevator_number: int, destination: int = 0):
        if elevator_number > len(self.elevators) or elevator_number <= 0:
            return print(f"Elevator {elevator_number} not found. Try a different value")
        
        target_elevator = self.elevators[elevator_number - 1]
        target_elevator.change_floor(destination)
    
    def fire_alarm(self):
        '''
        Sets off a fire alarm in the building, making all the elevators to fall to the bottom floor.
        '''
        for elevator in self.elevators:
            elevator.change_floor(self.lowest_floor)
        

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
class Race:
    def __init__(self, name: str = "Race", length: float = 10, cars: list = [...]):
        self.name = name
        self.length = length
        self.cars = cars

    def hour_passes():
        print()
    
    def get_race_state():
        print()

    def race_over(self) -> bool:
        for car in self.cars:
            if car.distance_driven >= self.length:
                return True
        return False
    
def race_main():
    cars = []

    for i in range(1, 11): # create 10 cars 1-10
        speed = random.randint(100, 200)
        car = Car(f"ABC-{i}", speed)
        car.accelerate(random.randint(-10, 15))
        cars.append(car)

    race = Race("The grand scrap race", 8000, cars)

    while not race.race_over():
        # TODO

#race_main()