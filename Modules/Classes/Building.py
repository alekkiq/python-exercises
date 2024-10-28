from .Elevator import Elevator

class Building:
    def __init__(self, highest_floor: int = 1, lowest_floor: int = 0, elevator_count: int = 1):
        self.highest_floor = highest_floor
        self.lowest_floor = lowest_floor
        self.elevator_count = elevator_count
        self.elevators = self.create_elevators(elevator_count)

    def create_elevators(self, count):
        elevators = []
        for i in range(1, count + 1):
            elevator = Elevator(self.highest_floor, self.lowest_floor, f"EL{i}")
            elevators.append(elevator)
        
        return elevators

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