import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

# Configuration class for data transformation paths
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self) -> ColumnTransformer:
        '''
        Creates and returns the data preprocessing pipeline object containing ColumnTransformers 
        for numerical and categorical columns.
        '''
        try:
            # TODO: Define your numeric and categorical feature names
            numerical_columns = []
            categorical_columns = []

            # Pipeline for handling numerical columns
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            # Pipeline for handling categorical columns
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder(handle_unknown='ignore')),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )

            logging.info(f"Numerical columns: {numerical_columns}")
            logging.info(f"Categorical columns: {categorical_columns}")

            # Combine numerical and categorical pipelines
            preprocessor = ColumnTransformer(
                transformers=[
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipeline", cat_pipeline, categorical_columns)
                ]
            )

            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path: str, test_path: str):
        '''
        Applies the preprocessor object on training and test datasets.
        '''
        try:
            # Example read
            # train_df = pd.read_csv(train_path)
            # test_df = pd.read_csv(test_path)
            
            logging.info("Read train and test data completed")
            
            logging.info("Obtaining preprocessing object")
            preprocessing_obj = self.get_data_transformer_object()
            
            # Example logic to apply transformation:
            # target_column_name = "target_column"
            # input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            # target_feature_train_df = train_df[target_column_name]
            
            # input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            # input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)
            
            # train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            # test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            
            # save_object(
            #     file_path=self.data_transformation_config.preprocessor_obj_file_path,
            #     obj=preprocessing_obj
            # )
            
            # return (train_arr, test_arr, self.data_transformation_config.preprocessor_obj_file_path)
            pass
        except Exception as e:
            raise CustomException(e, sys)
