import math

# 6
def price_per_square_meter(diameter: float, price: float | int):
    area = round(math.pi * (diameter / 2) ** 2, 2) / 10000 # calculate the "pizza" area in cm2 and divide by 10000 to get m2
    return price / area

# helper
def get_pizza_value_input(pizza_number: int):
    diameter = float(input(f"\nPizza {pizza_number} diameter (cm): "))
    price = float(input(f"Pizza {pizza_number} price (EUR): "))
    return round(price_per_square_meter(diameter, price), 6)

def main():
    pizza_1_price_per_sqm = get_pizza_value_input(1)
    pizza_2_price_per_sqm = get_pizza_value_input(2)

    if pizza_1_price_per_sqm == pizza_2_price_per_sqm:
        print("The pizzas are the same value!")
    elif pizza_1_price_per_sqm < pizza_2_price_per_sqm:
        print("Pizza 1 is cheaper per square meter.")
    else:
        print("Pizza 2 is cheaper per square meter.")

main()