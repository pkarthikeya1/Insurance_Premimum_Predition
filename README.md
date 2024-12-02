# **Insurance Premium Prediction Project**

This project aims to predict health insurance premiums using a dataset with 1 million records. The data includes various factors influencing medical costs, such as demographics and lifestyle attributes. The project involves comprehensive data preprocessing, exploratory analysis, machine learning model development, and deployment through a Streamlit interface. The modular code design ensures scalability and maintainability.

---

## 📂 **Project Structure**

```
Insurance_Premium_Prediction/
│
├── notebooks/
│   ├── 01_Data_Ingestion.ipynb          # Load data from Database.db and initial exploration
│   ├── 02_EDA.ipynb                     # In-depth exploratory data analysis with visualizations
│   ├── 03_Data_Transformation.ipynb     # Data cleaning, transformation, and feature engineering
│   ├── 04_Model_Experimentation.ipynb   # Model selection, hyperparameter tuning, and comparison
│   ├── 05_Model_Training.ipynb          # Final training and performance evaluation
│   └── frontend.ipynb                   # Prototyping the Streamlit frontend
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py            # Handles data loading and basic validation from Database.db
│   │   ├── data_transformation.py       # Feature scaling, encoding, and outlier handling
│   │   └── model_trainer.py             # Model training, validation, and saving to disk
│   │
│   ├── pipelines/
│   │   ├── prediction_pipeline.py       # Preprocessing and inference pipeline for real-time predictions
│   │   └── training_pipeline.py         # End-to-end pipeline for model training and evaluation
│   │
│   ├── constants.py                      # Configuration file for global constants (paths, hyperparameters)
│   ├── db_paths.py                       # Manages database connection paths and table definitions
│   ├── frontend.py                       # Streamlit code to interact with the model via a web interface
│   ├── logger.py                         # Logging setup for error handling, data tracking, and debugging
│   └── utils.py                          # Helper functions for data manipulation, evaluation, and visualization
│
├── requirements.txt                      # List of Python dependencies and their versions
└── README.md                             # Project documentation (this file)
```

---

## 🚀 **Objective**

Predict health insurance premiums based on key demographic and lifestyle attributes, including:
- Age
- Gender
- Body Mass Index (BMI)
- Number of children
- Smoking status
- Region
- Occupation
- Type of insurance plan

---

## 📊 **Dataset Overview**

- **Source:** `Insurance_Prediction` table from `Database.db`  
- **Total Records:** 1,000,000  
- **Data Splits:**
  - **Training Set:** 700,000 records  
  - **Validation Set:** 200,000 records  
  - **Live/Production Data:** 100,000 records for real-time evaluation  

---

## 🛠️ **Technical Implementation**

### 📌 **Key Steps:**

1. **Data Ingestion:**
   - Load data from a SQLite database.
   - Validate data integrity and handle missing values.

2. **Exploratory Data Analysis (EDA):**
   - Visualize feature distributions, correlations, and identify outliers.
   - Generate insights into feature impact on insurance premiums.

3. **Data Transformation:**
   - Encode categorical variables.
   - Scale numerical features.

4. **Model Development:**
   - **Selected Model:** Random Forest Regressor
   - **Why Gradient Boosting?** Performed best in terms of Feature importance, R² compared to Linear Regression and XGBoost.
   - **Metrics Used:** 
     - Mean Absolute Error (MAE)
     - Root Mean Squared Error (RMSE)
     - R² Score

5. **Model Training Pipeline:**
   - Modular code for training, validation, and saving the model.
   - Hyperparameter tuning and cross-validation to avoid overfitting.

6. **Prediction Pipeline:**
   - Ensures consistency in data preprocessing for real-time predictions.
   - Deploys a trained model for inference.

7. **Frontend (Streamlit Application):**
   - Interactive UI for inputting customer data.
   - Provides real-time premium predictions with a user-friendly interface.

---

## 💻 **How to Run the Project**

### 1. **Setup the Environment:**
   ```bash
   pip install -r requirements.txt
   ```

### 2. **Run the Streamlit Application:**
   ```bash
   streamlit run src/frontend.py
   ```

### 3. **Train the Model:**
   Execute the training pipeline to retrain the model:
   ```bash
   python src/pipelines/training_pipeline.py
   ```

---

## 📈 **Evaluation Metrics and Performance**

- **Testing Performance:** RMSE: `1416.15`, R²: `0.803`
- **Feature Importance (Top 4):**
  1. Coverage Level
  2. Smoker Status  No
  3. Family Medical History High blood pressure
  4. Smoker Status  Yes

---

## 🌐 **Streamlit Application Features**

- **Input Fields:** User-friendly form for entering customer data (age, BMI, etc.)
- **Real-time Prediction:** Calculate and display the predicted insurance premium.
- **Model Explainability:** Display top influencing factors for the prediction.

---

## 📜 **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 👩‍💻 **Author**
[Karthikeya Pervela]  
[pervela.karthikeya@gmail.com]
---
