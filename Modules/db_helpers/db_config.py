# this could also be done in a json file etc.
# but in this context it's easiest in a straight
# python file

def db_config() -> dict:
    return {
        # connection_params to be used in establishing a mysql connection
        "connection_params": {
            "host": "localhost",
            "username": "root",
            "password": "password",
            "collation": "utf8mb4_unicode_ci"
        },
        # database_keys for database-specific params
        "database_keys": {
            "name": "airports_db",
            "tables": [
                "airports"
            ]
        }
    }