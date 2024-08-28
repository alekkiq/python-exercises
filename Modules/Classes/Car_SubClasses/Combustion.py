from Classes.Car import Car

class Combustion(Car):
    def __init__(self, registration_number: str = "", speed: int = 0, distance_driven: int = 0, gas_capacity: float = 0):
        self.gas_capacity = gas_capacity
        super().__init__(registration_number, speed, distance_driven)
        
    def accelerate(self, change: int = 0) -> int:
        return super().accelerate(change)
    
    def drive(self, time: float = 0) -> int:
        return super().drive(time)