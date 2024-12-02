from dataclasses import dataclass
import os
import numpy as np

from sklearn.ensemble import (
    RandomForestRegressor
)
from sklearn.metrics import r2_score
import joblib as jl
from src.logger import logger

from src.utils import get_important_features

from src.utils import evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.joblib")


class ModelTrainer:

    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, train_array, test_array):
        try:
            logger.info("splitting train and test input data")

            X_train,y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )
            
            model = RandomForestRegressor()
                
            model_report:dict=evaluate_model(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                             model=model)
            
            model_obj = jl.dump(model,self.model_trainer_config.trained_model_file_path)

            

            return model_report


        except Exception as e:
            raise e