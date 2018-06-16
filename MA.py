#FUNCION PARA EL SIMULADOR QUE NOSOTROS CREAMOS
import pandas as pd
import pandas_datareader as web
import pandas as pd
import pytz
from talib import SMA
import datetime as dt

start = dt.datetime(2015,1,1)
end = dt.datetime(2015,12,31)

asset = 'AAPL'  

data = web.DataReader(asset, 'morningstar', start= start, end=end)
data.index = data.index.droplevel()

data.columns = ['Open', 'High', 'Low','Close', 'Volume']

def SMAdecision(table, days):   
    decision = []
    dataSMA = SMA(table['Close'])

    for i in range(len(data['Close'])):
        if dataSMA.iloc[i] < table['Close'].iloc[i] :
            decision.append()
            #BUY


