import os
import quandl
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from statistics import mean
import numpy as np
style.use('fivethirtyeight')

load_dotenv('./.env')
API_KEY = os.getenv("API_KEY")

def moving_average(values):
    return mean(values)

def create_labels(currentValue, futureHPI):
    if futureHPI > currentValue:
        return 1
    else:
        return 0

housing_data = pd.read_pickle('newHPI.pickle')
housing_data_percentage_change = housing_data.pct_change()
housing_data_percentage_change.replace([np.inf, -np.inf], np.nan, inplace=True)
housing_data_percentage_change.dropna(inplace=True)
housing_data_percentage_change['US_HPI_future']= housing_data_percentage_change['US_HPI'].shift(-1)

housing_data_percentage_change['label'] = list(map(create_labels, housing_data_percentage_change['US_HPI'], housing_data_percentage_change['US_HPI_future']))


# print(housing_data)
# print(housing_data_percentage_change.head())

housing_data_percentage_change['ma_apply_example'] = housing_data_percentage_change['M30'].rolling(10).apply(moving_average)

print(housing_data_percentage_change.tail())
