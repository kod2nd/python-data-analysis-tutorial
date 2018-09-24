import pandas as pd

# Reading csv
df = pd.read_csv('./ZILLOW-Z77006_ZRISFRR.csv')
print(df.head())

df.set_index('Date', inplace=True )
# Writing to a new csv
df.to_csv('./newcsv2.csv')

# Setting an index when reading
df = pd.read_csv('./newcsv2.csv', index_col=0)
print(df.head())

# Renaming columns, note INDEX is not a COLUMN
df.columns = ['AUSTIN_HPI']
print(df.head())

# Saving the file with he new header
df.to_csv('./newcsv3.csv')
print(df.head())

# Saving without the header
df.to_csv('./newcsv4.csv', header=False)
print(df.head())

# Reading a file with no headers, How to set headers, and then set the index col
df = pd.read_csv('./newcsv4.csv', names=['Date', 'AustinHPI'], index_col=0)
print(df.head())

# Converting to different dataformats, HTML, JSON etc
df.to_html('example.html')
df.to_json('example.json')

# Renaming specific column names
df = pd.read_csv('./newcsv4.csv', names=['Date', 'AustinHPI'])

df.rename(columns={'AustinHPI': 'Austin_Housing_Prices'}, inplace=True)

print(df.head())