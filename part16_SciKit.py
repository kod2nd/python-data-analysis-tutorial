import os
import quandl
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from statistics import mean
from sklearn import svm, preprocessing
from sklearn.model_selection import train_test_split
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

# print(housing_data_percentage_change.tail())

# Features
X = np.array(housing_data_percentage_change.drop(['label', 'US_HPI_future'], 1))
# Labels
y = np.array(housing_data_percentage_change['label'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

print(clf.score(X_test,y_test))
