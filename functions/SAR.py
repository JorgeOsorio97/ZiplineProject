import pandas as pd
import numpy as np
from talib import SAR # pylint: disable=E0611

def SARdecision(table, aceleration = 0.02, max = 0.2):   
    decision = []
    high =table['High']
    low = table['Low']

    del table
    data = SAR(np.array(high), np.array(low), aceleration, max)
    

    for i in np.arange(len(high)):     
        if np.isnan(data[i]):
            decision.append(None)
        elif data[i] >= low[i]:
            decision.append('Buy') 
        elif data[i] <= high[i]:
            decision.append('Sell')
        else:
            decision.append(decision[-1])  

    
    return {'decision' :decision, 'data': data}
