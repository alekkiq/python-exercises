import random

from Classes.Car import Car

# 1 - 3    
def exercises():
    # 1
    car = Car("ABC-123", 142)
    print(f"Car {car.registration_number}:\n")
    print(f"Speed: {car.speed}km/h")
    print(f"Total distance driven: {car.distance_driven}km\n\n")

    # 2
    print(f"The car accelerated by 30km/h, it's speed is now {car.accelerate(30)}")
    print(f"The car is accelerating even more, now by 70km/h. The current speed is {car.accelerate(70)}")
    print(f"It's still accelerating! By 50km/h! Now it's at {car.accelerate(50)}\n")
    print(f"There's a car slowing down in front! The car is slowing down rapidly. It's speed is now {car.accelerate(-200)}\n\n")

    # 3
    car.speed = 102
    print(f"The car's distance-meter started working! The driver has driven for 1,5 hours at {car.speed}km/h. The distance driven is now {car.drive(1.5)}km")

#   exercises()


# 4
def car_race(cars_amount: int = 10, race_time: float = 1):
    # create the cars
    cars = []

    for i in range(1, cars_amount + 1):
        registration_number = f"ABC-{i}"
        speed = random.randint(100, 200)
        car = Car(registration_number, speed)
        car.accelerate(random.randint(-10, 15)) # counterintuitively setting the acceleration here already
        cars.append(car)

    # the "race" loop
    race_ended = False

    while race_ended is not True:
        for car in cars:
            car.drive(race_time)

            if car.distance_driven >= 10000: # check for winner
                print(f"The race is over. Car {car.registration_number} has won!\n")
                race_ended = True
                break

    # get the car stats
    print("Car statistics:\n")
    for car in cars:
        print(f"Car {car.registration_number}, Speed: {car.speed}km/h, Distance driven: {car.distance_driven}km")

car_race()