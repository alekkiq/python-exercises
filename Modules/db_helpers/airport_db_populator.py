import mysql.connector
import csv
import pandas as pd
import os


# get predefined data from a json file
def read_csv(filename: str) -> list:
    directory = os.path.dirname(__file__)
    file_path = os.path.join(directory, filename)

    data = dict()

    with open(file_path, newline='', mode="r") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=' ', quotechar="|")
        csv_header = next(csv_reader)

        # add the header columns as their own 
        data.update({"header": csv_header})
        data.update({"header_data_types": {
            "id": "INT PRIMARY KEY",
            "ident": "VARCHAR(50)",
            "type": "VARCHAR(50)",
            "name": "VARCHAR(100)",
            "latitude_deg": "FLOAT",
            "longitude_deg": "FLOAT",
            "elevation_ft": "INT",
            "continent": "VARCHAR(10)",
            "iso_country": "VARCHAR(10)",
            "iso_region": "VARCHAR(20)",
            "municipality": "VARCHAR(100)",
            "scheduled_service": "VARCHAR(10)",
            "gps_code": "VARCHAR(10)",
            "iata_code": "VARCHAR(10)",
            "local_code": "VARCHAR(10)",
            "home_link": "TEXT",
            "wikipedia_link": "TEXT",
            "keywords": "TEXT"
        }})

    #print(data)
    return data

def db_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password", # top tier, hiring applications accepted
        collation="utf8mb4_unicode_ci", # fixes some weeeird issues with mysql connector
        # autocommit=True
    )

    return db

# fill the db with data
def fill_database(data: list, db_name: str = "database"):
    db = db_connection()
    cursor = db.cursor()

    # create the db
    cursor.execute(f"DROP DATABASE IF EXISTS {db_name};")
    cursor.execute(f"CREATE DATABASE {db_name};")
    cursor.execute(f"USE {db_name};")
    
    # start with creating the table & the columns
    create_table_statement = f"CREATE TABLE airports (\n"

    for header in data["header"]:
        column_definition = f"{header} {data["header_data_types"].get(header, 'VARCHAR(255)')},\n"
        create_table_statement += column_definition

    create_table_statement = create_table_statement.rstrip(",\n") + "\n);"

    cursor.execute(create_table_statement)

fill_database(read_csv("airports.csv"), "airports_db")
