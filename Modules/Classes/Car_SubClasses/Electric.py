from Classes.Car import Car

class Electric(Car):
    def __init__(self, registration_number: str, top_speed, battery_capacity: float = 0):
        self.battery_capacity = battery_capacity
        super().__init__(registration_number, top_speed)
        
    def accelerate(self, change: int) -> int:
        return super().accelerate(change)
    
    def drive(self, time: float) -> int:
        return super().drive(time)