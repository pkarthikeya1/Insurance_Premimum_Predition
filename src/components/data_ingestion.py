import sys
import os

# Add the root directory (Insurance_Premium_Prediction) to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Now you can import from src
import src.utils

from dataclasses import dataclass

from sklearn.model_selection import train_test_split

from src.utils import DatabaseHandler

from src.logger import logger



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

            os.makedirs(os.path.join("artifacts",'self.ingestion.config.raw_data_path'), exist_ok=True)

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
            logger.info("Probelm initating the data ingestion method {e}")
            raise e
        


if __name__=="__main__":
    obj=DataIngestion()
    raw_data, train_data, test_data=obj.initiate_data_ingestion()

