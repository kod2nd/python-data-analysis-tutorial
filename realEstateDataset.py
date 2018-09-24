import os
from dotenv import load_dotenv
import pandas as pd
import quandl

load_dotenv('./.env')
API_KEY = os.getenv("API_KEY")

# df = quandl.get('FMAC/HPI_AK', authtoken=API_KEY)
# print(df.head())

fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

abbriviations = fifty_states[0][1][1:]

for abbriviation in abbriviations:
    print('FMAC/HPI_{}'.format(abbriviation))