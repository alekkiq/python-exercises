class Car:
    def __init__(self, registration_number: str | int = 0, top_speed: int = 0, speed: int = 0, distance_driven: int = 0):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.speed = speed
        self.distance_driven = distance_driven
    
    def accelerate(self, change: int = 0) -> int:
        if self.speed + change <= 0:
            return 0 # avoid negative speeds
        
        self.speed += change

        if self.speed >= self.top_speed:
            self.speed = self.top_speed

        return self.speed
    
    def drive(self, time: float = 0) -> int:
        if time <= 0:
            return
        self.distance_driven += self.speed * time
        return int(self.distance_driven)