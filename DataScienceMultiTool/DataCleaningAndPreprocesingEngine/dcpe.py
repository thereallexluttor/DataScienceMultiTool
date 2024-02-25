#DCPE is a custom class for manage and handle a diverse types of datasets.

#import libraries to start working
 import pandas as pd
 import numpy as np

#a simply class to unify all the cleaning stuff
 class DataFrameHandler:

    #instance method 
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    #preprocessing method (numerical transformation)
    def process_data_num(self):

        """Here is important to denote a a few points when we think in data procesation.
        when you work whith litle datasets or you don't have enought information it's not
        a good idea drop the null or Nan values. why? because that can impact in some important
        metrics like the distribution of your data and only this will have big repercutions
        in your insights. wathever, this first version only works for hugue datasets.
        but i will make a more robust version of this.
        """

        #a simple way to clean the data of Nan or null values.
        cleaned_data = self.dataframe.dropna()

        #if the dataset have categorical data here that data will turn to numeric by doing a
        #one hot enconding

        #find categorcial cols if exists.
        categorical_cols = [col for col in cleaned_data.columns if cleaned_data[col].dtype == "object" and len(cleaned_data[col].unique()) < 5]

        #check it there are any categorical columns.
        if caregocial_cols:

            #return an encoded dataframe
            encoded_data = pd.get_dummies(cleaned_data, columns = categorical_cols)
            return encoded_data
        #if not exists categorical variables return only the cleaned dataframe
        else:
            return cleaned_data


    #preprocessing method (categorical transformation)
    def process_data_cat(self):

        """Here is important to denote a a few points when we think in data procesation.
        when you work whith litle datasets or you don't have enought information it's not
        a good idea drop the null or Nan values. why? because that can impact in some important
        metrics like the distribution of your data and only this will have big repercutions
        in your insights. wathever, this first version only works for hugue datasets.
        but i will make a more robust version of this.
        """

        #a simple way to clean the data of Nan or null values.
        cleaned_data = self.dataframe.dropna()

        return cleaned_data
