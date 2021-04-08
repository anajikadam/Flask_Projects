# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:37:23 2020

@author: Anaji
"""

import pandas as pd

class PreprocessData:
    """
    Module for preprocessing data
    """
    def preprocess1(self,dataset):
        """
        Preprocess dataframe for model_1
        Input:
            dataset = dataframe
        Output:
            dataset = cleaned dataframe
        """
        # Experience column missing value fill by 0
        dataset['experience'].fillna(0, inplace=True)
        # test_score column missing  value fill by mean value of that column
        dataset['test_score(out of 10)'].fillna(
                                    dataset['test_score(out of 10)'].mean(),
                                    inplace=True)
        # function for Converting words to integer values
        def convert_to_int(word):
            """
            function convert word to number
            Input:
                word = word for number
            Output:
                number = number for inputed word
            """
            word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5,
                         'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10,
                         'eleven':11, 'twelve':12, 'zero':0, 0: 0}
            return word_dict[word]
        dataset['experience'] = dataset['experience'].apply(
                                    lambda x : convert_to_int(x))
        return dataset
