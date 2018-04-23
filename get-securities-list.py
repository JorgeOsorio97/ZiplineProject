from requests import request
import pandas as pd

api_username = '8993a7d350ddc80795097189caecf28b'
api_password = '7f74a16a497c5f27204b15eebd3eeeae'
base_url = "https://api.intrinio.com"

bmv = '^XMEX'
for x in list(range(11,20)):
    request_url = base_url + '/securities'
    q_params = {
        'exch_symbol':bmv,
        'page_number':x,
    }

    response = request('get',request_url, params = q_params, auth=(api_username, api_password))


    data = response.json()['data']

    df = []

    for row in data:
        ticker = row['ticker']
        security_name = ['security_name']
        figi_ticker = row['figi_ticker']
        figi = row['figi']
        df.append([ticker,security_name,figi_ticker,figi])
        #print(ticker + ' : ' + security_name + ' : ' + figi_ticker)

    cols = ['TICKER','SECURITY','FIGI-TICKER','FIGI']
    df = pd.DataFrame(df,columns = cols)
    print(df.head)
    df.to_csv('securities-list-{}.csv'.format(x)  )     