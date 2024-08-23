# import all helper functions
from db_helpers.data.airports_data_types import *
from db_helpers.csv_helpers import *
from db_helpers.mysql_helpers import *

def populate_database(data_file: str, db_name: str = "my_database"):
    '''
    Fills the given database name with data in the *data_file* CSV file.
    '''
    # initialize the connection and create the database
    db = db_connection("localhost", "root", "password", "utf8mb4_unicode_ci")
    cursor = db.cursor()
    create_database(cursor, db_name)
    
    # get the necessary things from the csv
    column_names = get_csv_headers(data_file)
    column_data_types = airports_data_types_sql()
    
    # create the table with the correct column names / data types
    create_table(cursor, "airports", column_names, column_data_types)
    
    # continue to inserting the data itself.
    data_chunksize = 500
    data = get_csv_data(data_file, data_chunksize)
    insert_data_to_table(cursor, "airports", data, column_names, data_chunksize)
    db.commit()
    
    # close the cursor & the database when ready
    cursor.close()
    db.close()

# populate_database(get_file_path("airports.csv"), "airports")