import os
from src.logger import logger
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.utils import DatabaseHandler


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train_data.csv")
    test_data_path: str = os.path.join("artifacts", "test_data.csv")
    raw_data_path: str = os.path.join("artifacts","raw_data.csv")


class DataIngestion:

    def __init__(self) -> None:
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logger.info("Entered the data ingestion method")
    
        try :
            logger.info("Establishing Connection with SQLite databse")
            db_handler = DatabaseHandler()
            raw_data = db_handler.initating_data_extraction_from_database()
            logger.info("Successfuly read the raw data as dataframe")

            db_handler.disconnect()
            logger.info("Disconnected from SQLite database")

            
            logger.info("Train Test Split Initiated")

            train_set,test_set = train_test_split(raw_data, test_size=0.3, random_state=42)

            raw_data.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logger.info("Data ingestion is complete")

            return(
                self.ingestion_config.raw_data_path,
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logger.error("Probelm initating the data ingestion method {e}")
            raise e