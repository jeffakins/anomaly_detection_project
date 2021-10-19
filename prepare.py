# This is a file that will keep all of my Data Prepare Scripts

# Imports
import numpy as np
import pandas as pd
import env
import os

# Functions

def get_logs():
    '''This is a function that will return all of the Codeup 
    curriculum logs and cohort information'''
   
    if os.path.isfile('curriculum.csv'):                        # Returns the csv version if it exists
        df = pd.read_csv('curriculum.csv')
    else:                                                       # Else, pulls from the sql server
        sql = '''SELECT *
                 FROM logs
                 LEFT JOIN cohorts 
                 ON cohorts.id = logs.cohort_id;'''

        url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/curriculum_logs'
        df = pd.read_sql(sql, url)
        df.to_csv('curriculum.csv')                             # Creates the csv version

    return df


