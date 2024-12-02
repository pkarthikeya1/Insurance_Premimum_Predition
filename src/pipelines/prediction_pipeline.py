import pandas as pd
import joblib
import os
from src.logger import logging

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):

        try:
            model_path=os.path.join("artifacts","model.joblib")
            preprocessor_path=os.path.join('artifacts','preprocessor.joblib')

            logging.info("Loading model...")
            model=joblib.load(model_path)
            logging.info("Model loaded successfully.")

            logging.info("Loading preprocessor...")
            preprocessor=joblib.load(preprocessor_path)

            logging.info("Preprocessor loaded successfully.")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
    
        except Exception as e:
            logging.error(f"Error loading artifacts: {e}")
            raise e



class CustomData:
    
    def __init__(  self,
        age:int,
        gender: str,
        bmi: float,
        children:int,
        smoker:str,
        medical_history: str,
        family_medical_history: str,
        exercise_frequency: str,
        region: str,
        occupation: str,
        coverage_level: str):
        
        self.age = age

        self.gender = gender

        self.bmi = bmi

        self.children = children

        self.smoker = smoker

        self.medical_history = medical_history

        self.family_medical_history = family_medical_history

        self.exercise_frequency = exercise_frequency
        
        self.region =region

        self.occupation = occupation

        self.coverage_level = coverage_level


    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "age": [self.age],
                "gender": [self.gender],
                "bmi": [self.bmi],
                "children": [self.children],  # Corrected typo from 'childern'
                "smoker": [self.smoker],
                "medical_history": [self.medical_history],
                "family_medical_history": [self.family_medical_history],
                "exercise_frequency": [self.exercise_frequency],
                "region": [self.region],
                "occupation": [self.occupation],
                "coverage_level": [self.coverage_level]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise e