class Car:
    def __init__(self, registration_number: str, top_speed: int):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.speed = 0
        self.distance_driven = 0
    
    def accelerate(self, change: int) -> int:
        if self.speed + change <= 0:
            return 0 # avoid negative speeds
        
        self.speed += change

        if self.speed >= self.top_speed:
            self.speed = self.top_speed

        return self.speed
    
    def drive(self, time: float) -> int:
        if time <= 0:
            return
        self.distance_driven += self.speed * time
        return int(self.distance_driven)