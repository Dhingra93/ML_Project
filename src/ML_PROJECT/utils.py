import os
import sys
from src.ML_PROJECT.exception import CustomException
from src.ML_PROJECT.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
import pymysql.cursors

load_dotenv()

host=os.getenv('host')
user=os.getenv('user')
passw=os.getenv('pass')
db=os.getenv('db')

def read_sql_data():
    logging.info('Reading SQL database started')
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=passw,
            database=db,
            #cursorclass=pymysql.cursors.DictCursor
        )
        logging.info('Connection established ',mydb)
        df=pd.read_sql_query('Select * from students',mydb)
        print(df.head())
        return df
    except Exception as e:
        raise CustomException(e,sys)
