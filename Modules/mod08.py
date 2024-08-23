import mysql.connector
from db_helpers.airport_db_populator import *

# first put some data to the db
fill_database(read_json("airports.json"), "airports_db")

# 1
def get_airport_by_icao():
    icao = input("Input a valid Airport ICAO-code: ")

    db = db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("USE airports_db;")
    
    query = f"SELECT name, municipality FROM airports WHERE icao = '{icao.upper()}';"

    cursor.execute(query)

    for item in cursor.fetchall():
        print(f"\nAirport {icao}:\n")
        print(f"Name: {item["name"]}")
        print(f"Municipality: {item["municipality"]}\n")


# test with these ICAOs: KLAX, RJTT, EGLL
#   get_airport_by_icao()

# 2 TODO
# this part requires a ready database with more data than my one...



