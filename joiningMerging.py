import pandas as pd

df1 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index=[2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index=[2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Unemployment': [7, 8, 9, 6],
                    'Low_tier_HPI': [50, 52, 50, 53]},
                   index=[2001, 2002, 2003, 2004])

# MERGE, does not care about index
df4 = pd.merge(df1, df3, on='HPI')
df4.set_index('HPI', inplace=True)
print(df4)

df5 = pd.DataFrame({
    'Int_rate': [2, 3, 2, 2],
    'US_GDP_Thousands': [50, 55, 65, 55],
    'Year': [2001, 2002, 2003, 2004],
})

df6 = pd.DataFrame({
    'Unemployment': [7, 8, 9, 6],
    'Low_tier_HPI': [50, 52, 50, 53],
    'Year': [2001, 2003, 2004, 2005]},
    )

# MERGE option 'how' can take values like left, right, inner and outer like SQL, default value is inner
df7 = pd.merge(df5, df6, on='Year', how='outer')
df7.set_index('Year', inplace=True)
print(df7)

# JOIN, must set an index first, Also takes in the SQL LEFT,RIGHT, INNER, OUTER. Default value is outer
df5.set_index('Year', inplace=True)
df6.set_index('Year', inplace=True)
df7 = df5.join(df6, how='outer')
# df7.set_index('Year', inplace=True)
print(df7)
