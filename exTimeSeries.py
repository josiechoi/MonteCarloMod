import pandas as pd
2012d = pd.read_csv("IEXE0101-sd-2012-ed-2012-12-31.csv", parse_dates=True, index_col='Date')
2013d = pd.read_csv("IEXE0101-sd-2013-ed-2013-12-31.csv", parse_dates=True, index_col='Date')
2014d = pd.read_csv("IEXE0101-sd-2014-ed-2014-12-31.csv", parse_dates=True, index_col='Date')
2015d = pd.read_csv("IEXE0101-sd-2015-ed-2015-12-31.csv", parse_dates=True, index_col='Date')
2016d = pd.read_csv("IEXE0101-sd-2016-ed-2016-12-31.csv", parse_dates=True, index_col='Date')

# Initialize empty list: data
exTimeSeries = []

# Build the list of Series
for date, IEXE0101 in [2012d, 2013d, 2014d, 2015d, 2016d]:
    exTimeSeries.append([exTimeSeries["day"],exTimeSeries["IEXE0101"]])

# Concatenate the list: exList
exList = pd.concat(exTimeSeries,axis="rows")

# Print slices from exList
print(exList.loc['jan 27, 2015':'feb 2, 2015'])
print(exList.loc['feb 26, 2015':'mar 7, 2015'])
