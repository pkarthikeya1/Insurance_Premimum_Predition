import streamlit as st
import pandas as pd
import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline


def predict_datapoint():
    st.title('Insurance Premium Prediction')

    # Columns for layout
    col = st.columns(2)

    # Input fields matching CustomData attributes
    gender = col[1].selectbox('Gender', ["female", "male"])
    age = col[0].number_input('Enter age in years', step=1, min_value=18, max_value=70)
    bmi = col[0].number_input('BMI of customer', min_value=14.1, max_value=54.0, value=25.0, step=0.1)
    children = col[1].number_input("Number of children", step=1, min_value=0, max_value=20)
    smoker = col[0].selectbox('Smoker', ['yes', 'no'])
    medical_history = col[1].selectbox('Medical History', ['Heart disease', 'Diabetes', 'High blood pressure'])
    family_medical_history = col[0].selectbox('Family Medical History', ['Heart disease', 'Diabetes', 'High blood pressure'])
    exercise_frequency = col[1].selectbox('Exercise Frequency', ['Never', 'Frequently', 'Occasionally', 'Rarely'])
    region = col[0].selectbox('Region', ['northwest', 'southeast', 'northeast', 'southwest'])
    occupation = col[1].selectbox('Occupation', ['Student', 'Unemployed', 'White collar', 'Blue collar'])
    coverage_level = col[0].selectbox('Coverage Level', ['Basic', 'Standard', 'Premium'])

    # Prediction button
    if st.button('Predict'):
        # Create CustomData instance
        data = CustomData(
            gender=gender,
            age=age,
            bmi=bmi,
            children=children,
            smoker=smoker,
            medical_history=medical_history,
            family_medical_history=family_medical_history,
            exercise_frequency=exercise_frequency,
            region=region,
            occupation=occupation,
            coverage_level=coverage_level
        )
        
        # Get DataFrame and predict
        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        
        st.success(f'Predicted Premium: ${results[0]:.2f}')

# Run the app
predict_datapoint()