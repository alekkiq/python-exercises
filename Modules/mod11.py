import random

# 1
from Classes.Release_SubClasses.Paper import Paper
from Classes.Release_SubClasses.Book import Book

# 2
from Classes.Car_SubClasses.Electric import Electric
from Classes.Car_SubClasses.Combustion import Combustion

# 1
def releases_main():
    releases = [
        Paper("Aku Ankka", "Aki Hyyppä"),
        Book("Hytti n:o 6", "Rosa Liksom", 200)
    ]
    
    for release in releases:
        release.get_information()
        
#   releases_main()


# 2
def cars_main(randomized_speeds: bool = False):
    print("\n")
    cars = [
        Electric("ABC-15", 180, 0, 52.5),
        Combustion("ACD-123", 180, 0, 32.3)
    ]
    
    for car in cars:
        if randomized_speeds:
            car.accelerate(random.randint(-30, 30)) # for some variety
        car.drive(3)
        print(f"Car {car.registration_number} distance driven after at {car.speed} km/h for 1 hour: {car.distance_driven}")
        
#   cars_main(False)
#   cars_main(True)