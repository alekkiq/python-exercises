class Elevator:
    def __init__(self, highest_floor: int = 1, lowest_floor: int = 0, product_number: str = ""):
        self.product_number = product_number
        self.highest_floor = highest_floor
        self.lowest_floor = lowest_floor
        
        self.current_floor = lowest_floor

    def floor_up(self, current_floor: int):
        return current_floor + 1
    
    def floor_down(self, current_floor: int):
        return current_floor - 1
    
    def change_floor(self, destination: int):
        if destination > self.highest_floor or destination < self.lowest_floor or destination < 0:
            return print("Invalid floor number.")
       
        for floor in range(self.current_floor, destination, -1 if self.current_floor > destination else 1):
            if self.current_floor > destination:
                self.current_floor = self.floor_down(floor)
            elif self.current_floor < destination:
                self.current_floor = self.floor_up(floor)