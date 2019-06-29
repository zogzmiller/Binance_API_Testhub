import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import urllib
import datetime
###################################################################
#BINANCE API REQUEST TYPES WITH PARAMS/LIMITS/WEIGHTS ???????
#Params with an asterik are required*
#/api/v1/time weight 1 no params

#/api/v1/exchangeInfo weight 1 no params

#/api/v1/exchangeInfo weight 1 no params

#/api/v1/depth Params = symbol*, limit
# Limit	    Weight
# 5-100	     1
# 500	     5
# 1000	     10

#/api/v1/trades weight 1 Default 500; max 1000; Params = symbol*, limit

#/api/v1/historicalTrades weight 5  Default 500; max 1000; Params = symbol*, limit, fromld

#/api/v1/aggTrades weight 1 Default 500; max 1000; Params = symbol*, fromld, startTime, endTime, limit

#/api/v1/klines weight 1 Params = symbol*, interval*, startTime, endTime, limit

#/api/v3/avgPrice weight 1 Params = symbol*

#/api/v1/ticker/24hr weight 1 Params = symbol(40 weight when omitted)

#/api/v3/ticker/price weight 1 Params = symbol(2 weight when omitted)

#/api/v3/ticker/bookTicker weight 1 Params = symbol(2 weight when omitted)
###################################################################
binance_url = 'https://api.binance.com/api/v1/trades?symbol=LTCBTC'
binance_time_url = 'https://api.binance.com/api/v1/time'
binance_trade_url = 'https://api.binance.com/api/v1/trades?'
binance_historicaltrades_url = 'https://api.binance.com/api/v1/historicalTrades?'
binance_aggTrades_url = 'https://api.binance.com/api/v1/aggTrades?'
binance_klines_url = 'https://api.binance.com/api/v1/klines?'
binance_avgPrice_url = 'https://api.binance.com/api/v3/avgPrice?'
binance_24hrticker_url = 'https://api.binance.com/api/v1/ticker/24hr?'
binance_tickerprice_url = 'https://api.binance.com/api/v3/ticker/price?'
binance_bookTicker_url = 'https://api.binance.com/api/v3/ticker/bookTicker?'

crypto_symbols = {
    'LTCBTC' : 'symbol=LTCBTC',
    'ETHUSDT' : 'symbol=ETHUSDT',
    'BTCUSDT' : 'symbol=BTCUSDT',
    'ETHBTC' : 'symbol=ETHBTC',
    'BCCBTC' : 'symbol=BCCBTC',
    'XRPBTC' : 'symbol=XRPBTC'}


for key, symbol in crypto_symbols.items():
    print(key)
    url = binance_trade_url + symbol + '&limit=1000'

    current_time_request = requests.get(binance_time_url).json()    
    response = requests.get(url).json()
    print(response)
    print(current_time_request)
    print(datetime.datetime.now())


# dict_keys = list(response[0].keys())
# test_df = pd.DataFrame(response)

# print(test_df)
# with open('test.txt', mode='x') as textfile:
# for x in response:
#     print(f'{current_time_request}')
#     for key in dict_keys:
#         print(f'{key}: {x[key]}')
