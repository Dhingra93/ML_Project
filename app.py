from src.ML_PROJECT.logger import logging
from src.ML_PROJECT.exception import CustomException
from src.ML_PROJECT.components.data_ingestion import DataIngestion
import sys

if __name__=="__main__":
    logging.info("The execution has started")
    

    try:
        data_ingestion=DataIngestion()
        
        data_ingestion.initate_data_ingestion()


        
    except Exception as e:
        logging.info("CustomException")
        raise CustomException(e,sys)
