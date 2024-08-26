# In this file the exercises 1 - 3 in Module 10 are
# blended together, since they all revolve around
# the Elevator class. So the "exercise" in this file
# is essentially just exercise 3.

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
        print(f"change_floor, current floor: {self.current_floor}. Changing to {destination}")
        '''
        Changes the Elevators floor to a given *destination*.
        '''

        if destination == self.lowest_floor:
            self.current_floor = destination

        if destination > self.highest_floor or destination < self.lowest_floor or destination < 0:
            return print("Invalid floor number.")
        
        for floor in range(self.current_floor, destination):
            if self.current_floor > destination:
                self.current_floor = self.floor_down(floor)
            elif self.current_floor < destination:
                self.current_floor = self.floor_up(floor)
                
        print(f"change_floor floor after changing; {self.current_floor}")        

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
        

def main():
    building = Building(10, 1, 5)

    # loop for just moving around with elevators
    while (True):
        chosen_elevator_number = int(input(f"The house has {building.elevator_count} elevators. Which one to use: "))

        chosen_elevator = building.elevators[chosen_elevator_number - 1]

        print(f"Elevator {chosen_elevator.product_number}, current floor {chosen_elevator.current_floor}\n")

        destination = int(input(f"Which floor to go {building.lowest_floor} - {building.highest_floor}: "))

        building.move_elevator(chosen_elevator_number, destination)
        
        print(f"Elevator {chosen_elevator.product_number}, current floor {chosen_elevator.current_floor}")

main()
