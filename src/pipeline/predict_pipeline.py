import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            
            loaded_model = model["model"]
            loaded_params = model["params"]

            # Create a new instance of the model with the loaded hyperparameters
            model_with_loaded_params = loaded_model.set_params(**loaded_params)            
            
            preds=model_with_loaded_params.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        age: int,
        gender: str,
        income: int,
        credit_score: int,
        credit_history_length: int,
        no_of_existing_loans: int,
        loan_amount: int,
        loan_tenure: int,
        existing_customer: str,
        state: str,
        city: str,
        employment_type: str,
        occupation: str,
        bike_price: int,
    ):

        self.age = age
        self.gender = gender
        self.income = income
        self.credit_score = credit_score
        self.credit_history_length = credit_history_length
        self.no_of_existing_loans = no_of_existing_loans
        self.loan_amount = loan_amount
        self.loan_tenure = loan_tenure
        self.existing_customer = existing_customer
        self.state = state
        self.city = city
        self.employment_type = employment_type
        self.occupation = occupation
        self.bike_price = bike_price


    def get_data_as_data_frame(self):
        try:
        
            custom_data_input_dict = {
                "Gender": [self.gender],
                "Age": [self.age],
                "Income": [self.income],
                "Credit Score": [self.credit_score],
                "Credit History Length": [self.credit_history_length],
                "Number of Existing Loans": [self.no_of_existing_loans],
                "Loan Amount": [self.loan_amount],
                "Loan Tenure": [self.loan_tenure],
                "Existing Customer": [self.existing_customer],
                "State": [self.state],
                "City": [self.city],
                "Employment Profile": [self.employment_type],
                "Occupation": [self.occupation],
                "LTV Ratio": [self.loan_amount/self.bike_price]
            }

            df = pd.DataFrame(custom_data_input_dict)
            df['Credit History Length'] = df['Credit History Length']*12
            df['Loan Tenure'] = df['Loan Tenure']*12
            
            return df

        except Exception as e:
            raise CustomException(e, sys)

