import sqlite3
import pandas as pd
from dataclasses import dataclass


from src.db_paths import db_path, table_name, query
from src.logger import logger

@dataclass
class DatabaseConfig:
    database_path: str = db_path
    table_name: str = table_name
    sql_query: str = query



class DatabaseHandler:
    def __init__(self):
        """
        Initialize the database handler with the DatabaseConfig to the SQLite database.
        """
        self.db_config = DatabaseConfig()

    def initating_data_extraction_from_database(self) ->pd.DataFrame:
        try:
            self.connection = sqlite3.connect(self.db_config.database_path)
            self.cursor = self.connection.cursor()
            logger.info("Successfully connected to the SQLite database.")
        except sqlite3.Error as e:
            logger.info(f"Error connecting to database: {e}")

        try:
            df= pd.read_sql_query(self.db_config.sql_query, self.connection)
            return df
        
        except Exception as e:
            logger.info(f"Error reading SQLite to DataFrame: {e}")

    def disconnect(self) -> None:
        """
        Disconnect from the SQLite database.
        """
        try:
            if self.connection:
                self.connection.close()
                logger.info("Disconnected from the SQLite database.")

        except Exception as e:
            logger.info(f"Error closing SQLite database connection: {e}")
            raise e