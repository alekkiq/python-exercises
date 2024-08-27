# import all helper functions
from db_helpers.data.airports_data_types import *
from db_helpers.csv_helpers import *
from db_helpers.mysql_helpers import *
from db_helpers.db_config import db_config

def populate_database(data_file: str, db_name: str = "my_database"):
    '''
    Fills the given database name with data in the *data_file* CSV file.
    '''
    # get the database configuration from a config file
    config = db_config()
    connection_params = config["connection_params"]
    
    # initialize the connection and create the database
    db = db_connection(connection_params)
    cursor = db.cursor()
    create_database(cursor, db_name)
    
    # get the necessary things from the csv
    column_names = get_csv_headers(data_file)
    column_data_types = airports_data_types_sql()
    
    # create the table with the correct column names / data types
    table_name = "airport"
    create_table(cursor, table_name, column_names, column_data_types)
    
    # continue to inserting the data itself.
    data_chunksize = 500
    data = get_csv_data(data_file, data_chunksize)
    insert_data_to_table(cursor, table_name, data, column_names)
    db.commit()
    
    # close the cursor & the database when ready
    cursor.close()
    db.close()