#FUNCION PARA EL SIMULADOR QUE NOSOTROS CREAMOS
import pandas as pd
import numpy as np
from talib import TRIMA # pylint: disable=E0611

def TRIMAdecision(table, days = 20):   
    decision = []
    close =table['Close']
    del table
    data = TRIMA(np.array(close),days)

    for i in np.arange(len(close)):     
        if np.isnan(data[i]):
            decision.append(None)
        if data[i] > close[i]:
            decision.append('Sell') 
        if data[i] < close[i]:
            decision.append('Buy')  
    return decision
