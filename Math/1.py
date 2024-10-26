import numpy as np

def degrees_to_radians():
    # 1. Degrees to radians

    # a)
    print(np.rad2deg(2493)) # 142838.4

    # b)
    print(np.rad2deg(0.911)) # 52.2

def radians_to_degrees():
    # 2. Radians to degrees

    # a)
    print(np.deg2rad(137.7)) # 2.4

    # b)
    print(np.deg2rad(62.3)) # 1.1 

def convertion_table():
    # 3. Degrees to radians convertion table

    values = np.array([
        30, 45, 60, 90, 120, 135, 150, 180, 270, 360
    ])

    print(f"{'Degrees':<10}{'Radians':<10}")

    for value in values:
        print(f"{value:<10}{np.deg2rad(value):<10}")

def calculate_hypotenuse():
    # 4. Calculate the hypotenuse

    a = 1.6
    b = 2.3

    print(f'{np.hypot(a, b)}m')

if __name__ == "__main__":
    print("Exercise 1")
    degrees_to_radians()
    print("\nExercise 2")
    radians_to_degrees()
    print("\nExercise 3")
    convertion_table()
    print("\nExercise 4")
    calculate_hypotenuse()