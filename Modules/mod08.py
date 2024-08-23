import mysql.connector

from db_helpers.populate_airports_db import populate_database
from db_helpers.csv_helpers import get_file_path

# first put some data to the db
# building the db helpers was most likely a larger job than the exercise itself :D
populate_database(get_file_path("airports.csv"), "airports")

# 1
def get_airport_by_icao():
    print("")


# test with these ICAOs: KLAX, RJTT, EGLL
#   get_airport_by_icao()

# 2 TODO
# this part requires a ready database with more data than my one...



