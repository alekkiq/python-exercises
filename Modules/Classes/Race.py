import random
from tabulate import tabulate

class Race:
    def __init__(self, name: str, length: int, cars: list):
        self.name = name
        self.length = length
        self.cars = cars

    def get_race_state(self, sort: bool = False):
        headers = ["Registration", "Speed", "Distance driven (km)"]
        data = []
        
        for car in self.cars:
            data.append([car.registration_number, f"{car.speed} km/h", car.distance_driven])
        
        if sort == True: # sorting on
            data = sorted(data, key=lambda x: x[2], reverse=True)
            
        return print(tabulate(data, headers=headers, tablefmt="grid"))
    
    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1) # 1 -> 1 hour

    def race_over(self):
        sorted_cars = sorted(list(self.cars), key=lambda car: car.distance_driven, reverse=True)
        
        for car in sorted_cars:
            if car.distance_driven >= self.length:
                return car.registration_number
        return False