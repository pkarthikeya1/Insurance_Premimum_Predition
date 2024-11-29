from dataclasses import dataclass
import os
import joblib as jl
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from src.logger import logger
from src.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.constants import Numerical_Cols, Categorical_Cols, train_data, test_data, train_labels, test_labels, target_column_name


@dataclass
class DataColumns:
    Numerical_Columns = Numerical_Cols
    Categorical_Columns = Categorical_Cols
    train_df = train_data
    test_df = test_data
    train_target = train_labels
    test_target = test_labels
    target = target_column_name



@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", 'preprocessor.joblib')


class DataTransformation:
    def __init__(self):
        
        self.data_transformation_config = DataTransformationConfig()
        self.data_columns = DataColumns()

    def get_data_transformer_object(self):

        """
        This function is responisble for data transformation
    
        """
        try:

            

            num_pipeline = Pipeline(

                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())]
            )

            cat_pipeline = Pipeline(

                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("OneHotEncoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))]
            )
            logger.info("Numerical columns standard scaling completed")
            logger.info("Categorical columns encoding completed")
            
            preprocessor = ColumnTransformer(
                [
                    # ("Duplicate_Dropper", duplicate_pipeline, self.data_columns.Numerical_Columns+self.data_columns.Categorical_Columns),
                    ("Numerical_Pipeline", num_pipeline, self.data_columns.Numerical_Columns),
                    ("Categorical_Pipeline", cat_pipeline, self.data_columns.Categorical_Columns)
                     ]
            )


            preprocessor_obj = jl.dump(preprocessor,self.data_transformation_config.preprocessor_obj_file_path)
            
            logger.info(f"saved preprocessor as joblib file in the path {self.data_transformation_config.preprocessor_obj_file_path}")
            return preprocessor
        except Exception as e:
            raise e

    def initiate_data_transformation(self, train_path, test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logger.info("Reading train and test data completed")

            logger.info("Obtaining preprocessing object")

            prerprocessing_obj = self.get_data_transformer_object()

            logger.info("Applying preprocessor on train dataset and test dataset")
            
            input_feature_arr = prerprocessing_obj.fit_transform(train_df.drop(columns=self.data_columns.target, axis=1))

            transformed_columns = prerprocessing_obj.get_feature_names_out()

            input_test_arr = prerprocessing_obj.transform(test_df.drop(columns=self.data_columns.target, axis=1))

            train_arr = np.c_[
                input_feature_arr, np.array(train_df[self.data_columns.target].values)
            ]

            test_arr = np.c_[
                input_test_arr, np.array(test_df[self.data_columns.target].values)
            ]

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
                transformed_columns
                
            )
        except Exception as e:
            raise e
            
            
            
                        
            

if __name__=="__main__":
    obj= DataIngestion()
    raw_data, train_data, test_data=obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)