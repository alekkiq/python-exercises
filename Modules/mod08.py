import mysql.connector
from geopy import distance

from db_helpers.populate_airports_db import populate_database
from db_helpers.mysql_helpers import db_connection
from db_helpers.db_config import db_config
from db_helpers.csv_helpers import get_file_path

# first put some data to the db
# building the db helpers was most likely a larger job than the exercise itself :D
# populate_database(get_file_path("airports.csv"), "airports")

# 1
def get_airport_by_icao():
    sql_query = "SELECT name, municipality FROM airport WHERE ident = '%s';"
    
    database_config = db_config()
    db = db_connection(database_config["connection_params"])
    cursor = db.cursor(dictionary=True)
    
    while (True):
        icao_ident = input("Search for an airport by ICAO-code: ")
        
        cursor.execute(sql_query % icao_ident.upper())
        
        result = cursor.fetchall()
        
        if not result:
            print(f"Airport with the ICAO {icao_ident} does not exist in our database")
        else:
            for row in result:
                print(f"Airport {icao_ident}:\nName: {row['name']}, municipality: {row['municipality']}")
            break

#   get_airport_by_icao()

# 2
def get_countries_by_iso_country():
    sql_query = "SELECT type, COUNT(*) AS typecount FROM airport WHERE iso_country = '%s' GROUP BY type ORDER BY typecount DESC;"
    
    database_config = db_config() # <-- Update your own proper values before running!
    db = db_connection(database_config["connection_params"])
    cursor = db.cursor(dictionary=True)
    
    while (True):
        iso_country = input("Search for an airport by ISO country code (eg. FI): ").upper()
        
        cursor.execute(sql_query % iso_country)
        
        result = cursor.fetchall()
        
        if not result:
            print(f"Airport with the ISO country code {iso_country} does not exist in our database")
        else:
            print(f"Airports in {iso_country}:\n")
            for row in result:
                print(f"{row['type'].replace('_', ' ').capitalize()}: {row['typecount']}")
            break
            
#   get_countries_by_iso_country()

# 3
def get_airport_gap():
    sql_query = "SELECT name, ident, latitude_deg, longitude_deg FROM airport WHERE ident = '%s';"
    
    database_config = db_config()
    db = db_connection(database_config["connection_params"])
    cursor = db.cursor(dictionary=True)

    inserted_airports = [
        input("Input an airports ICAO-code: ").upper(),
        input("Input another airports ICAO-code: ").upper()
    ]

    queried_airports = []

    for airport in inserted_airports:
        cursor.execute(sql_query % airport)
        found_rows = cursor.fetchone()
        
        if len(found_rows) == 0:
            print(f"Airport with the ICAO  '{airport}' was not found in our database")
            break

        queried_airports.append(found_rows)
    
    # this could maybe be done more cleanly, but it works in this case
    airport_one_coordinates = (queried_airports[0]["latitude_deg"], queried_airports[0]["longitude_deg"])
    airport_two_coordinates = (queried_airports[1]["latitude_deg"], queried_airports[1]["longitude_deg"])

    print(f"Distance between airports {queried_airports[0]["ident"]} - {queried_airports[1]["ident"]}:\nApproximately {int(distance.distance(airport_one_coordinates, airport_two_coordinates).km)} kilometers")
    
#    get_airport_gap()
