import mysql.connector
import json
import os


# get predefined data from a json file
def read_json(filename: str) -> list:
    directory = os.path.dirname(__file__)
    file_path = os.path.join(directory, filename)

    json_file = open(file_path, 'r')

    try:
        data = json.load(json_file) # chatgpt generated json data <3
    finally:
        json_file.close() 

    return data 

# fill the db with data
def fill_database(data: list):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password", # top tier, hiring applications accepted
        collation="utf8mb4_unicode_ci", # fixes some weeeird issues with mysql connector
        autocommit=True
    )

    cursor = db.cursor()

    # create the db
    cursor.execute("DROP DATABASE IF EXISTS airports_db;")
    cursor.execute("CREATE DATABASE airports_db;")
    cursor.execute("USE airports_db;")

    # create a simple table
    cursor.execute("CREATE TABLE airports (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), icao VARCHAR(4), municipality VARCHAR(100));")

    # fill it with some preset data
    insert_sql = "INSERT INTO airports (name, icao, municipality) VALUES (%s, %s, %s)"

    try:
        for item in data:
            airport = (item["name"], item["icao"], item["municipality"])
            cursor.execute(insert_sql, airport)
    except:
        print("An error occurred while trying to fill database. Try again")
    finally:
        print(f"Successfully inserted data to the DB. Added {len(data)} items.")
