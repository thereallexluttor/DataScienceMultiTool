#Here I pretend to test the datascience multi tool class to 
#be sure about the quality of my code and my methods to provide
#a good code with a basic scence of quality.

#import the libs
import unittest
import pandas as pd
from dcpe import DataFrameHandler as dfh
import sys

sys.path.append("..")

#class to start testing the dcpe class and his inner methods
class TestDataCleaner(unittest.TestCase):
    
    #setup method
    def setUp(self):
        #create a dataframe to make the test
        self.df = pd.DataFrame({'A': ['cat', 'dog', 'cat', 'dog'],
                                'B': ['small', 'large', 'medium', 'small'],
                                'C': [1, 2, 3, 4]})
        
        #instantiate the datacleaner class with the example dataframe
        self.cleaner = dfh(self.df)

    #methods to test the missing values
    def test_clean_missing_values_1(self):
        #verify the non existense of missing values
        cleaned_df = self.cleaner.process_data_num()
        self.assertTrue(cleaned_df.isnull().sum().sum() == 0)
    
    def test_clean_missing_values_2(self):
        #verify the non existense of missing values
        cleaned_df = self.cleaner.process_data_cat()
        self.assertTrue(cleaned_df.isnull().sum().sum() == 0)

    #methods to test the one hot enconding for categorical and non-categorical dataframes
    def test_one_hot_encode_categorical(self):
        #verify the correct one-hot codification
        encoded_df = self.cleaner.process_data_num()
        self.assertEqual(encoded_df.shape[1], self.df.shape[1] + 3) #verify if new columns where created
    
    def test_one_hot_encode_categorical_no_categorical(self):
        #verify if not exist a codification is not exist categorical data
        df_no_categorical = pd.DataFrame({'A': [1, 2, 3],
                                          'B': [4, 5, 6]})
        cleaner_no_categorical = dfh(df_no_categorical)
        encoded_df = cleaner_no_categorical.process_data_num()
        self.assertEqual(encoded_df.shape, df_no_categorical.shape) #the forms must be equals
    
if __name__ == '__main__':
    unittest.main()    