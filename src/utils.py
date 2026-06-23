import os
import sys
import dill
from src.exception import CustomException
from src.logger import logging

def save_object(file_path: str, obj) -> None:
    '''
    Saves an object (like a trained model or a transformer pipeline) as a serialized file.
    '''
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info(f"Successfully saved object to {file_path}")
    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path: str):
    '''
    Loads a serialized object from the given file path.
    '''
    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)
        logging.info(f"Successfully loaded object from {file_path}")
        return obj
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train, y_train, X_test, y_test, models: dict, params: dict) -> dict:
    '''
    A skeleton function for evaluating dictionary of models.
    Can be expanded to perform hyperparameter tuning and score evaluation.
    '''
    try:
        report = {}
        # Implement model training and evaluation logic here
        return report
    except Exception as e:
        raise CustomException(e, sys)
