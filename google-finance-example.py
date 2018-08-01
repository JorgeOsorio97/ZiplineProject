from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data

# Dow Jones
param = {
    'q': "BIMBOA", # Stock symbol (ex: "AAPL")
    'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
    'x': "BMV", # Stock exchange symbol on which stock is traded (ex: "NASD")
    'p': "1Y" # Period (Ex: "1Y" = 1 year)
}
# get price data (return pandas dataframe)
df = get_price_data(param)
print(df)
#                          Open      High       Low     Close     Volume
# 2016-05-17 05:00:00  17531.76   17755.8  17531.76  17710.71   88436105
# 2016-05-18 05:00:00  17701.46  17701.46  17469.92  17529.98  103253947
# 2016-05-19 05:00:00  17501.28  17636.22  17418.21  17526.62   79038923
# 2016-05-20 05:00:00  17514.16  17514.16  17331.07   17435.4   95531058
# 2016-05-21 05:00:00  17437.32  17571.75  17437.32  17500.94  111992332
# ...                       ...       ...       ...       ...        ...
