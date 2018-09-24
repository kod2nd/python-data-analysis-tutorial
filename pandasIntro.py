import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2017, 1, 1)
end = datetime.datetime.now()

df = web.DataReader("XOM", "iex", start, end)

print(df.head())


df['high'].plot()
plt.legend()
plt.show()