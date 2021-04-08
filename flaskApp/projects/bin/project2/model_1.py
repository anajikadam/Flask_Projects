# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:37:22 2020

@author: Anaji
"""

# import pandas as pd
# import numpy as np
#
# from sklearn.linear_model import LinearRegression
import pickle
import yaml

# from preprocessor import PreprocessData
from flaskApp.projects.bin.project1.preprocessor import PreprocessData


class Prediction:
    """
    Module for Create Model and prediction logic 
    """
    def __init__(self):
        with open('flaskApp/projects/bin/project2/config.yml','r') as fl:
            self.config = yaml.load(fl, Loader=yaml.FullLoader)
        
    def loadCSV(self,filePath):
        """
        Loading CSV file
        Input:
            filepath
        Output:
            df = Dataframe
        """
        df= pd.read_csv(filePath)
        return df
    
    def preprocess(self,data):
        """
        Preprocess data by PreprocessData()
        Input:
            data = dataframe
        Output:
            preprocess_data = cleaned dataframe
        """
        preprocessObj = PreprocessData()
        preprocess_data = preprocessObj.preprocess1(data)
        return preprocess_data
    
    def dataSplit(self,df):
        """
        Dataframe split Independent and dependent features
        Input:
            df = dataframe
        Output:
            X = Independent feature as message
            y = Dependent feature as label
        """
        X = df.iloc[:, :3]
        y = df.iloc[:, -1]
        return X, y
        
    def linearReg(self, X, y, filename1):
        #Since we have a very small dataset, 
        #we will train our models with all availabe data.
        regressor = LinearRegression()
        #Fitting models with trainig data
        regressor.fit(X, y)
        # Saving models to disk
        pickle.dump(regressor, open(filename1, 'wb'))
        
    def model(self):
        """
        Process from prepocess to models creation
        """
        filePath1 = self.config['model_data1']['train_data']
        data = self.loadCSV(filePath1)
        cleandata = self.preprocess(data)
        X, y = self.dataSplit(cleandata)
        filepath2 = self.config['model_pkl_1']['model_path']
        self.linearReg(X, y, filepath2)
        
    def loadpklfile(self, filename1,filename2):
        """
        Loading pkl file
        Input:
            filePath1 : filePath pkl file
        Output:
            regmodel : regressor models
        """
        # load the model from disk
        model = pickle.load(open(filename1, 'rb'))
        pipe = pickle.load(open(filename2, 'rb'))
        return model, pipe


    def predict(self, data):
        """
        Predict predictSalary
        Input:
            data : list of data value 
        Output:
            my_pred : prediction in numerical format
        """
        model,pipe = self.loadpklfile(self.config['model_pkl_1']['model_path']
                                 ,self.config['model_pkl_2']['model_path'])
        trans_data = pipe.transform(data)
        output = model.predict(trans_data)
        return output
        
# Create models by using train data and save pkl file
# PredictSalaryObj = PredictSalary()
# PredictSalaryObj.models()
# data = [[2, 9, 6]]
# result = PredictSalaryObj.predictsal(data)
# print(result)
