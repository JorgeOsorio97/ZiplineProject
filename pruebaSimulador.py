from functions.EMA import EMAdecision
from functions.KAMA import KAMAdecision
from functions.SMA import SMAdecision
from functions.TEMA import TEMAdecision
from functions.TRIMA import TRIMAdecision
from functions.WMA import WMAdecision
from simulator.simulator import Simulator
import pandas_datareader as web
import pandas as pd
import datetime as dt

start = dt.datetime(2015,1,1)
end = dt.datetime(2017,12,31)

asset = 'AAPL'  
data = web.DataReader(asset, 'morningstar', start= start, end=end)
data.index = data.index.droplevel()

sim = Simulator(data, std_purchase= 10)
sim.add_indicator('EMA-20',EMAdecision(data,20))
sim.add_indicator('KAMA-20',KAMAdecision(data,20))
sim.add_indicator('SMA-20',SMAdecision(data,20))
sim.add_indicator('SMA-100',SMAdecision(data,10))
sim.add_indicator('TEMA-20',TEMAdecision(data,20))
sim.add_indicator('TRIMA-20',TRIMAdecision(data,20))
sim.add_indicator('WMA-20',WMAdecision(data,20))

#print(sim.security.head())
#print(sim.security.tail())

sim.calc_earning()
print('\n Resumen')
print('Capital final {}'.format(sim.final_capital))
print('Acciones finales {}'.format(sim.shares_own))
print('Valor por accion {}'.format(sim.security['Close'].iloc[-1]))
print('Capital en acciones {}'.format(sim.security['Close'].iloc[-1] * sim.shares_own))