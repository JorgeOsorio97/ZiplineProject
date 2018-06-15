import pandas_datareader as web
from zipline.api import order,record,symbol
from zipline.algorithm import TradingAlgorithm
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from collections import OrderedDict
import pytz
from talib import MA

data = OrderedDict()
start = dt.datetime(2015,1,1)
end = dt.datetime(2015,12,31)

asset = 'AAPL'  
data[asset] = web.DataReader(asset, 'morningstar', start= start, end=end)
print(data[asset].head())
data[asset].index = data[asset].index.droplevel()
print(data[asset].head())
data[asset].columns = ['open', 'high', 'low','close', 'volume']
