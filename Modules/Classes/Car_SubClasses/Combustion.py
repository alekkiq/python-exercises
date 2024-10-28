from Classes.Car import Car

class Combustion(Car):
    def __init__(self, registration_number: str, top_speed: int, gas_capacity: float = 0):
        self.gas_capacity = gas_capacity
        super().__init__(registration_number, top_speed)
        
    def accelerate(self, change: int) -> int:
        return super().accelerate(change)
    
    def drive(self, time: float) -> int:
        return super().drive(time)