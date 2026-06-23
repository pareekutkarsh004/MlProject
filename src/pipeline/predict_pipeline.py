import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features: pd.DataFrame):
        '''
        Loads the preprocessor and model artifacts, scales the features, and returns model predictions.
        '''
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            
            # Load preprocessor and model
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            
            # Apply transformation
            data_scaled = preprocessor.transform(features)
            
            # Make predictions
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    '''
    Helper class to convert front-end / user input variables into a structured Pandas DataFrame.
    '''
    def __init__(self, feature1: float, feature2: float, category1: str):
        self.feature1 = feature1
        self.feature2 = feature2
        self.category1 = category1

    def get_data_as_data_frame(self) -> pd.DataFrame:
        '''
        Converts the initialization parameters into a Pandas DataFrame.
        '''
        try:
            custom_data_input_dict = {
                "feature1": [self.feature1],
                "feature2": [self.feature2],
                "category1": [self.category1],
            }
            
            df = pd.DataFrame(custom_data_input_dict)
            return df
        except Exception as e:
            raise CustomException(e, sys)
