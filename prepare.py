# This is a file that will keep all of my Data Prepare Scripts

# Imports ----------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import env
import os

# Functions --------------------------------------------------------------------------------

# Function to get the Codeup curriculum logs:

def get_logs():
    '''This is a function that will return all of the Codeup 
    curriculum logs and cohort information'''
    
        # Returns the csv version if it exists
    if os.path.isfile('curriculum.csv'):                        
        df = pd.read_csv('curriculum.csv')
        
        # Else, pulls from the sql server
    else:                                                       
        sql = '''SELECT *
                 FROM logs
                 LEFT JOIN cohorts 
                 ON cohorts.id = logs.cohort_id;'''

        url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/curriculum_logs'
        df = pd.read_sql(sql, url)

        # Creates the csv version
        df.to_csv('curriculum.csv')                             

    return df


# Function that adds the course names to the log files:

def add_course_names():
    '''This function creates a dictionary with the Codeup course 
    information and concatenates it with the log dataframe'''

        # Creating a dataframe with the course names:
    courses = pd.DataFrame({'id': [1, 2, 3, 4], 
                       'course_name': ['PHP Full Stack Web Dev', 'Java Full Stack Web Dev', 'Data Science', 'Front End Web Dev'],
                       'course_subdomain': ['php', 'java', 'ds', 'fe']})

        # Getting the log files:
    log = get_logs()

        # Adding the course names to the log files:
    log = log.merge(course, how='left', left_on='program_id', right_on='id')

        # Dropping duplicate columns:
    log = log.drop(columns=['Unnamed: 0', 'id_y', 'id_x', 'deleted_at'])

    return log