import pandas as pd
from src.components.data_ingestion import DataIngestionConfig

train_df_path = DataIngestionConfig().train_data_path
test_df_path = DataIngestionConfig().test_data_path

train_df = pd.read_csv(train_df_path)
test_df = pd.read_csv(test_df_path)

train_data = train_df.iloc[:, :-1]
train_data.drop_duplicates(inplace=True)
train_data.reset_index(drop=True, inplace=True)
test_data = test_df.iloc[:, :-1]
test_data.drop_duplicates(inplace=True)
test_data.reset_index(drop=True,inplace=True)

train_labels = train_data.iloc[:,-1]
test_labels = pd.DataFrame(test_df.iloc[:, -1])

target_column_name = "charges"

Numerical_Cols = train_data.select_dtypes(exclude="object").columns.to_list()
Categorical_Cols= train_data.select_dtypes(exclude="float64").columns.to_list()