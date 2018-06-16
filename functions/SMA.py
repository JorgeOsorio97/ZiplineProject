#FUNCION PARA EL SIMULADOR QUE NOSOTROS CREAMOS
import pandas as pd
import numpy as np
from talib import SMA # pylint: disable=E0611

def SMAdecision(table, days = 20):   
    decision = []
    close =table['Close']
    del table
    dataSMA = SMA(np.array(close),days)

    for i in np.arange(len(close)):     
        if np.isnan(dataSMA[i]):
            decision.append(None)
        if dataSMA[i] > close[i]:
            decision.append('Sell') 
        if dataSMA[i] < close[i]:
            decision.append('Buy')  
    return decision


