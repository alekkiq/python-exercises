import mysql.connector
import geopy

from db_helpers.populate_airports_db import populate_database
from db_helpers.mysql_helpers import db_connection
from db_helpers.db_config import db_config
from db_helpers.csv_helpers import get_file_path

# first put some data to the db
# building the db helpers was most likely a larger job than the exercise itself :D

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
    
    database_config = db_config()
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
    sql_query = "SELECT type, COUNT(*) AS typecount FROM airport WHERE iso_country = '%s' GROUP BY type ORDER BY typecount DESC;"
    
    database_config = db_config()
    db = db_connection(database_config["connection_params"])
    cursor = db.cursor(dictionary=True)