import requests

apiKey = 'e6cd91fd5766f09b6627773d8d83dfa6'

def getHistory(symbol, startDate):
    res = requests.post('https://marketdata.websol.barchart.com/getHistory.json', data={'apikey':apiKey, 'symbol':symbol,'type':'daily','startDate':startDate})
    print(res.json())

def getQuote(symbol):
    res = requests.post('https://marketdata.websol.barchart.com/getQuote.json', data={'apikey':apiKey, 'symbols':symbol})
    #print(res)
    print(res.json())

getHistory('AAPL','20180627')