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
    fifty_states = pd.read_html(
        'https://simple.wikipedia.org/wiki/List_of_U.S._states')
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

    pickle_out = open('fifty_states3.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()


def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=API_KEY)
    df.columns = ["United States"]
    df["United States"] = (
        df["United States"]-df["United States"][0]) / df["United States"][0] * 100.0
    df.rename(columns={'United States': 'US_HPI'}, inplace=True)
    return df


def mortgage_30y():
    df = quandl.get("FMAC/MORTG", trim_start="1975-01-01", authtoken=API_KEY)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    df = df.resample('M').mean()
    df.columns = ['M30']
    return df


def gdp_data():
    df = quandl.get("BCB/4385", trim_start="1975-01-01", authtoken=API_KEY)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    # df=df.resample('M').mean()
    df.rename(columns={'Value': 'GDP'}, inplace=True)
    df = df['GDP']
    return df


m30 = mortgage_30y()
HPI_data = pd.read_pickle('fifty_states3.pickle')
HPI_bench = HPI_Benchmark()
gdp = gdp_data()

newHPI = HPI_bench.join([m30, gdp])
newHPI.dropna(inplace=True)
newHPI.to_pickle('newHPI.pickle')

print(newHPI)

# print(state_HPI_M30.corr()['M30'].describe())
