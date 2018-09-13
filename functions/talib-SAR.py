import talib

def initialize(context):
  schedule_function(record_SAR, date_rules.every_day()),time_rules.market_close(hours = 1))

def record_SAR(context, data):

    stk = symbol('NVDA')

    H = data.history(stk, 'high', 2, '1d').dropna()
    L = data.history(stk,'low', 2, '1d').dropna()
    CP = data.current(stk, 'price')

    ta_SAR = talib.SAR(H, L, 0.02, 0.2)
    SAR = ta_SAR[-1]
    record( SAR = SAR, Price = CP)
