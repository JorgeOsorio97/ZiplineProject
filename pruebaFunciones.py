from functions.SAR import SARdecision
from simulator.simulator import Simulator
import pandas_datareader as web
import pandas as pd
import datetime as dt

start = dt.datetime(2015,1,1)
end = dt.datetime(2017,12,31)

asset = 'AAPL'  
data = web.DataReader(asset, 'morningstar', start= start, end=end)
data.index = data.index.droplevel()

print(len(SARdecision(data)['decision']))