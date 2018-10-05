import os
import quandl
from dotenv import load_dotenv
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

bridge_height = {'meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}

df = pd.DataFrame(bridge_height)
df['Standard Deviation'] = df['meters'].rolling(2).std()
df['MovingAverage'] = df['meters'].rolling(2).mean()


print(df)
print(df.describe()['meters']['std'])
df_std = df.describe()['meters']['std']
df = df[(df['Standard Deviation'] < df_std)]
print('after',df)

df['meters'].plot()
plt.show()