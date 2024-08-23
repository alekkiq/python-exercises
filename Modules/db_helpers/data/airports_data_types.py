# define the data types (mysql) for each
# column in airports.csv.

# if new columns are added to airports.csv,
# this file needs to be updated with the new
# column's data type, in order to fill the
# database properly

def airports_data_types_sql() -> dict:
    return {
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
    }