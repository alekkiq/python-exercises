from Classes.Car import Car

class Electric(Car):
    def __init__(self, registration_number: str = "", speed: int = 0, distance_driven: int = 0, battery_capacity: float = 0):
        self.battery_capacity = battery_capacity
        super().__init__(registration_number, speed, distance_driven)
        
    def accelerate(self, change: int = 0) -> int:
        return super().accelerate(change)
    
    def drive(self, time: float = 0) -> int:
        return super().drive(time)