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
data[asset].index = data[asset].index.droplevel()

data[asset].columns = ['open', 'high', 'low','close', 'volume']
#print(data[asset].info())

panel = pd.Panel(data)
panel.minor_axis = ['Open','High','Low','Close','Volume']
panel.major_axis = panel.major_axis.tz_localize(pytz.utc)

def initialize(context):
    context.asset = symbol('AAPL')
    context.invest = False
    context.count = 0

def handle_data(context, data):
    long_period = 40
    short_period = 20
    context.count+=1
    if context.count < long_period:
        return
    price_history = data.history(context.asset, 'price', long_period, '1d')
    short_MA = MA(price_history.values, 20)
    long_MA = MA(price_history.values,40)
    if short_MA[-1] < long_MA[-1] and not context.invest:
        order(context.asset, 10)
        context.invest = True
    if short_MA[-1] > long_MA[-1] and context.invest:
        order(context.asset,-10)
        context.invest = False
    record(price = data.current(context.asset, 'price'), promedioMovilCorto = short_MA, promedioMovilLargo = long_MA) 
    lt

algo_obj = TradingAlgorithm(initialize = initialize, handle_data = handle_data)

perf_manual = algo_obj.run(panel)

print(perf_manual)