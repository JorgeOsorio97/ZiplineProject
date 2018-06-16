from functions.EMA import EMAdecision
import pandas_datareader as web
import pandas as pd
import datetime as dt


start = dt.datetime(2015,1,1)
end = dt.datetime(2015,12,31)

asset = 'AAPL'  
data = web.DataReader(asset, 'morningstar', start= start, end=end)
data.index = data.index.droplevel()

print(EMAdecision(data, days=10))