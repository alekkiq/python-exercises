# 3
def gallons_to_liters(gallons : int | float):
    return gallons * 3.785

def main():
    while (True):
        gallons_to_convert = float(input("How many gallons to convert (insert a negative value to end): "))

        if gallons_to_convert <= 0:
            print("Thanks for using our converter!")
            break
        
        print(f"{gallons_to_convert} gallons is {round(gallons_to_liters(gallons_to_convert), 2)} liters.")

main()