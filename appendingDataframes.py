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
                    'Int_rate': [2, 3, 2, 2],
                    'Low_tier_HPI': [50, 52, 50, 53]},
                   index=[2001, 2002, 2003, 2004])

# CONCATENATION, of d1 and d2 just continues the rows of index
concat = pd.concat([df1,df2])
print(concat)

# What if conat all 3
concat = pd.concat([df1,df2,df3])
print(concat)

# APPEND
df4 = df1.append(df2)
print(df4)

# Series, just adds values the columns specified after index
s = pd.Series(["one", "two", "three"], index=["HPI","Int_rate","US_GDP_Thousands"])

df5 = df1.append(s, ignore_index = True)
print(df5)

