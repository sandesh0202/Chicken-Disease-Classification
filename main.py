from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n x===========================x")
except Exception as e:
   logger.exception(e)
   raise e
     

STAGE_NAME = "Prepare base Model"
if __name__ == "__main__":
   try:
      logger.info(f"*********************************")
      logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<<<<")
      obj = PrepareBaseModelTrainingPipeline()
      obj.main()
      logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n x===========================x")
   except Exception as e:
      logger.exception(e)
      raise e
   
   

STAGE_NAME = "Training"
try: 
   logger.info(f"*********************************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n x===========================x")
except Exception as e:
   logger.exception(e)
   raise e
     
     
STAGE_NAME = "Evaluation Stage"
try: 
   logger.info(f"*********************************")
   logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
   obj = EvaluationPipeline()
   obj.main()
   logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n x===========================x")
    
except Exception as e:
   logger.exception(e)
   raise e