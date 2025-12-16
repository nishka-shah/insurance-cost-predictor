import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_obj
import numpy as np

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path='artifact/model.pkl'
            preprocessor_path='artifact/preprocessor.pkl'
            model=load_obj(file_path=model_path)
            preprocessor=load_obj(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            pred=np.exp(model.predict(data_scaled))
            return pred
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    '''
    Maps user inputs to the backend
    '''
    def __init__(self, age: int, sex: str, bmi: float, children: int, smoker: str, region: str):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                'age': [self.age],
                'sex': [self.sex],
                'bmi': [self.bmi],
                'children': [self.children],
                'smoker': [self.smoker],
                'region': [self.region],
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)

        