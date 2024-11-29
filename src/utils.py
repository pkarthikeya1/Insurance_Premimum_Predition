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
        



###############################################################

from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

def evaluate_model(X_train, y_train, X_test, y_test, model):

    try:
        
        model.fit(X_train, y_train) 

        y_train_pred = model.predict(X_train)

        y_test_pred  = model.predict(X_test)

        train_model_r2_score = r2_score(y_train, y_train_pred)

        test_model_r2_score = r2_score(y_test, y_test_pred)
        
        train_RMSE = np.sqrt(mean_squared_error(y_train, y_train_pred))

        test_RMSE = np.sqrt(mean_squared_error(y_test, y_test_pred))

        report = {'train_R2_score':train_model_r2_score, 'test_R2_score':test_model_r2_score, 'train_RMSE': train_RMSE, 'test_RMSE': test_RMSE}

        return report

    except Exception as e:
        raise e

def get_important_features(model, features):
    importances = pd.DataFrame(model.feature_importances_)
    importances['features'] = features
    importances.columns = ['importance', 'features']
    importances.sort_values(by = 'importance', ascending= False,inplace=True)

    return importances