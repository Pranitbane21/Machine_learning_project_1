from collections import namedtuple
import os,sys
from housing.config.configuration import Configuartion
from housing.exception import HousingException
from housing.component.data_ingestion import DataIngestion
from housing.entity.artifact_entity import  DataIngestionArtifact




class Pipeline():

    def __init__(self, config: Configuartion ) -> None:
        try:
            self.config = config
        except Exception as e:
            raise HousingException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def start_data_validation(self):
        pass

    def start_data_transformation(self):
        pass

    def start_model_trainer(self):
        pass

    def start_model_evaluation(self):
        pass

    def start_model_pusher(self):
        pass        

    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()

        except Exception as e:
            raise HousingException(e,sys) from e