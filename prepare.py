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
    log = log.merge(courses, how='left', left_on='program_id', right_on='id')

        # Dropping duplicate columns:
    log = log.drop(columns=['Unnamed: 0', 'id_y', 'id_x', 'deleted_at'])

    return log


# Function that will prep the data prior to exploration:

def prep_logs():
    '''This function has scripts that clean the log data from Codeups curriculum'''

        # Getting the log files with course names included:
    log = add_course_names()

        # Filling the start, end, created, and update null dates with the log entry date:
    log.start_date = log.start_date.fillna(log['date'])
    log.end_date = log.end_date.fillna(log['date'])
    log.created_at = log.created_at.fillna(log['date'])
    log.updated_at = log.updated_at.fillna(log['date'])

        # Combining date and time, converting to datetime, and making it the index:
    log['timestamp'] = log.date + " " + log.time
    log.timestamp = pd.to_datetime(log.timestamp)
    log = log.set_index('timestamp')

        # Converting all dates and time columns to datetime format:
    log.start_date = pd.to_datetime(log.start_date)
    log.end_date = pd.to_datetime(log.end_date)
    log.created_at = pd.to_datetime(log.created_at)
    log.updated_at = pd.to_datetime(log.updated_at)

        # Creating an hour and weekday columns:
    log['hour'] = log.index.hour
    log['weekday'] = log.index.day_name()

        # Dropping the original date and time columns:
    log = log.drop(columns=['date', 'time'])

        # Filling NAs with 0 for numeric columns:
    log.cohort_id = log.cohort_id.fillna(0)
    log.program_id = log.program_id.fillna(0)
    log.cohort_id = log.cohort_id.astype('int64')
    log.program_id = log.program_id.astype('int64')

        # Filling NAs with 'none' for string columns:
    column_list = ['name', 'slack', 'course_name', 'course_subdomain']
    for col in column_list:
        log[col] = log[col].fillna('none')

    return log