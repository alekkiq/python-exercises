import random

# 1
def season_from_month():
    month = int(input("Enter a month number 1-12: "))

    seasons = (
        ("Winter", [12, 1, 2]),
        ("Spring", [3, 4, 5]),
        ("Summer", [6, 7, 8]),
        ("Autumn", [9, 10, 11])
    )

    for season, months in seasons:
        if month in months:
            print(season)

#   season_from_month()

# 2
def usernames():
    collected_usernames = set()

    while (True):
        username = input("Enter a username: ")

        if username == "":
            print("\nAll previously inputted names:\n")
            for name in collected_usernames:
                print(name)
            break

        if username in collected_usernames:
            print(f"Previously inputted username")
        else:
            collected_usernames.add(username)
            print("New username")

#   usernames()

# 3
def airport_search(preset_airports: dict = {"KJFK": "John F. Kennedy Airport", "EFHK": "Helsinki Vantaan lentokenttä"}):
    print("Welcome to our airport search centre.")
    
    collected_airports = preset_airports

    while (True):
        print("\n1) Add a new airport")
        print("2) Look for an existing airport")
        print("3) Quit\n")

        selected_action = int(input("Choose an action (1 - 3): "))

        match selected_action:
            case 1:
                airport_name = input("New airports name: ")
                airport_icao = input("New airports ICAO code: ")

                if airport_icao in collected_airports:
                    print(f"\nSearch found: ICAO-code {airport_icao} already exists. Try creating a new one")
                    continue

                collected_airports[airport_icao] = airport_name
                
                print(f"\nSuccesfully added airport {airport_icao}, {airport_name}")

                continue
            case 2:
                icao_code = input("\nInput an ICAO code: ")

                if icao_code not in collected_airports.keys():
                    print(f"\nAirport with ICAO-code {icao_code} was not found. Try adding it yourself?")
                    continue
                
                print(f"ICAO {icao_code}: {collected_airports[icao_code]}")

                continue
            case 3:
                print("Thanks for using our app!")
                break
            case _:
                print("\nInvalid number! Input a number 1 - 3")

#   airport_search()