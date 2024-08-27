import pandas as pd
import os

def get_file_path(filename: str) -> str:
    '''
    Returns the path of *filename* based on the directory of the file that called this function
    '''
    
    directory = os.path.dirname(__file__)
    return os.path.join(f"{directory}/data/", filename)

def get_csv_headers(csv_file: str) -> list:
    '''
    Reads the header row of a csv file and returns the values as a list
    '''
    
    return list(pd.read_csv(csv_file).columns)
    
def get_csv_data(csv_file: str, chunksize: int = 500) -> list:
    '''
    Returns csv data without the header row as a list of chunks
    '''
    
    df = pd.read_csv(csv_file, delimiter=',', header=1, encoding="utf-8")
    parsed_data = df.fillna(0) # replaces nan values with 0
    list_of_rows = [list(row) for row in parsed_data.values]
    
    # split the rows into reasonable chunks
    # this will be necessary since sql does not allow
    # queries of over 70000 lines
    
    # source: geeksforgeeks <3
    chunked_outcome = [list_of_rows[i * chunksize:(i + 1) * chunksize] for i in range((len(list_of_rows) + chunksize - 1) // chunksize)]
    
    return chunked_outcome