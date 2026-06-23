import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException
from src.logger import logging

class TrainPipeline:
    def __init__(self):
        pass

    def run_pipeline(self) -> float:
        '''
        Coordinates and runs the complete training lifecycle: ingestion, transformation, and training.
        '''
        try:
            logging.info("Starting training pipeline...")
            
            # 1. Data Ingestion
            # ingestion = DataIngestion()
            # train_data_path, test_data_path = ingestion.initiate_data_ingestion()
            
            # 2. Data Transformation
            # transformation = DataTransformation()
            # train_arr, test_arr, preprocessor_path = transformation.initiate_data_transformation(
            #     train_data_path, test_data_path
            # )
            
            # 3. Model Training
            # trainer = ModelTrainer()
            # r2_score = trainer.initiate_model_trainer(train_arr, test_arr)
            # logging.info(f"Model training pipeline completed with R2 Score: {r2_score}")
            # return r2_score
            
            return 0.0
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    pipeline = TrainPipeline()
    pipeline.run_pipeline()
