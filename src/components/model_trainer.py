from dataclasses import dataclass

from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, median_absolute_error, mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
import joblib as jl
from src.logger import logger

from src.utils import evaluate_models

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

            models = {
                "RandomForest":RandomForestRegressor(),
                "DecisionTree": DecisionTreeRegressor(),
                "GradientBoosting" : GradientBoostingRegressor(),
                "LinearRegression" : LinearRegression(),
                "XGBRegressor" : XGBRegressor(),
                "AdaBoostRegressor": AdaBoostRegressor()

            }
            model_report:dict = evaluate_models(
                X_train=X_train,
                y_train=y_train,
                X_test= X_test,
                y_test =y_test,
                models= models)
            
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise Exception("No best model found")
            
            logger.info(f"Best found model on both training and testing dataset")

            model_obj = jl.dump(best_model,self.model_trainer_config.trained_model_file_path)

            predicted = best_model.predict(X_test)

            R2_score = r2_score(y_test, predicted)

            return R2_score


        except Exception as e:
            raise e