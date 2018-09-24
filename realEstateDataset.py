import os
from dotenv import load_dotenv
import pandas as pd
import pickle
import quandl

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

        # NOTE: Quandl has since changed the returns of datasets, to where if the return has one column (or so it seems to me), then the title of that column is just "value." Well, that's irritating, but we can work around it. In our for loop, rename the dataframe's column to what our abbv value is.
        df.rename(columns={'Value': abbriviation}, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    # print(main_df.head())
    
    pickleFileOut = open('./fifty_states.pickle', 'wb')
    pickle.dump(main_df, pickleFileOut)
    pickleFileOut.close()

# grabInitialStatesData()

pickleFileIn = open('./fifty_states.pickle', 'rb')
HPI_data = pickle.load(pickleFileIn)
# print(HPI_data)

# to_pickle and pd.read_pickle, makes the code shorter. Dont have to open and close
HPI_data.to_pickle('pickle.pickle')
HPI_data2 = pd.read_pickle('pickle.pickle')
print(HPI_data2)