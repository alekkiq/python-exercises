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
def cars_main():
    print("\n")
    cars = [
        Electric("ABC-15", 180, 52.5),
        Combustion("ACD-123", 180, 32.3)
    ]
    
    for car in cars:
        car.accelerate(random.randint(100, 150))
        car.drive(3)
        print(f"Car {car.registration_number} distance driven after at {car.speed} km/h for 3 hours: {car.distance_driven}")
        
cars_main()