import os
from dotenv import load_dotenv
import pandas as pd
import pickle
import quandl
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

load_dotenv('./.env')
API_KEY = os.getenv("API_KEY")

# df = quandl.get('FMAC/HPI_AK', authtoken=API_KEY)
# print(df.head())

def stateList():
    fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    abbriviations = fifty_states[0][1][1:]
    return abbriviations

# Before joining the whole list of dataframes, need to create a main dataframe to join to

def grabInitialStatesData():
    states = stateList()
    main_df = pd.DataFrame()

    for abbriviation in states:
        query = 'FMAC/HPI_{}'.format(abbriviation)
        df = quandl.get(query, authtoken=API_KEY)

        # get percentage change against the first value

        # NOTE: Quandl has since changed the returns of datasets, to where if the return has one column (or so it seems to me), then the title of that column is just "value." Well, that's irritating, but we can work around it. In our for loop, rename the dataframe's column to what our abbv value is.
        df.rename(columns={'Value': abbriviation}, inplace=True)
        df[abbriviation] = (df[abbriviation]-df[abbriviation][0]) / df[abbriviation][0] * 100.0

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    # print(main_df.head())
    
    pickleFileOut = open('./fifty_states3.pickle', 'wb')
    pickle.dump(main_df, pickleFileOut)
    pickleFileOut.close()

# grabInitialStatesData()

# Get benchmark
def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=API_KEY)
    df.rename(columns={'Value': "United States"}, inplace=True)
    df["United States"] = (df["United States"]-df["United States"][0]) / df["United States"][0] * 100.0
    return df

# pickleFileIn = open('./fifty_states.pickle', 'rb')
# HPI_data = pickle.load(pickleFileIn)
# print(HPI_data)

# to_pickle and pd.read_pickle, makes the code shorter. Dont have to open and close
# HPI_data.to_pickle('pickle.pickle')
# HPI_data2 = pd.read_pickle('pickle.pickle')
# print(HPI_data2)

# config subplot
# fig = plt.figure()
# ax1 = plt.subplot2grid((1,1), (0,0))

# HPI_data = pd.read_pickle('pickle.pickle')
HPI_data_change = pd.read_pickle('fifty_states3.pickle')
# benchmark = HPI_Benchmark()

# print(HPI_data.head())

# Manupilating Data
# HPI_data['TX2'] = HPI_data['TX'] * 2
# print(HPI_data[['TX','TX2']])

# Plotting data
# HPI_data.plot()
# remove legend (optional)
# plt.legend().remove() 
# plt.show()

# HPI_data_change.plot(ax=ax1)
# benchmark.plot(color='k', ax=ax1, linewidth=10)

# plt.legend().remove()
# plt.show()

# CORRELATION
HPI_State_Correlation = HPI_data_change.corr()
print(HPI_State_Correlation)
print(HPI_State_Correlation.describe())