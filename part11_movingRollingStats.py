import os
import quandl
from dotenv import load_dotenv
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

load_dotenv('./.env')
API_KEY = os.getenv("API_KEY")

def state_list():
    fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fifty_states[0][0][1:]
    

def grab_initial_state_data():
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=API_KEY)
        print(query)
        df[abbv] = (df[abbv]-df[abbv][0]) / df[abbv][0] * 100.0
        print(df.head())
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
            
    pickle_out = open('fifty_states3.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=API_KEY)
    df["United States"] = (df["United States"]-df["United States"][0]) / df["United States"][0] * 100.0
    return df

fig = plt.figure()
ax1 = plt.subplot2grid((2,1), (0,0))
ax2 = plt.subplot2grid((2,1), (1,0), sharex=ax1)
HPI_data = pd.read_pickle('fifty_states3.pickle')

# HPI_State_Correlation = HPI_data.corr()

# To get resampling quantum --- https://pythonprogramming.net/resample-data-analysis-python-pandas-tutorial/?completed=/percent-change-correlation-data-analysis-python-pandas-tutorial/
# HPI_data['TX12MA'] = HPI_data['TX'].rolling(24).mean()
# HPI_data['TX12STD'] = HPI_data['TX'].rolling(12).std()

# HPI_data.dropna(inplace=True)
# print(HPI_data[['TX', 'TX12MA']])

# HPI_data['TX'].plot(ax=ax1, label='Monthly TX HPI')
# HPI_data['TX12MA'].plot(color='k', ax=ax1, label='Moving Average')
# HPI_data['TX12STD'].plot(ax=ax2, label= 'standard deviation')

# CORRELATION
TX_CA_corr= HPI_data['TX'].rolling(12).corr(HPI_data['WA'])

HPI_data['TX'].plot(ax=ax1)
HPI_data['WA'].plot(ax=ax1)
TX_CA_corr.plot(ax=ax2, label='Correlation')



plt.legend(loc=4)
ax1.legend(loc=4)
plt.show()