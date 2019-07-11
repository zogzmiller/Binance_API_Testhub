import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np
import requests
import time
import urllib
import pymongo
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
    'LTCUSDT' : 'symbol=LTCUSDT',
    'BTCUSDT' : 'symbol=BTCUSDT',
    'XRPUSDT' : 'symbol=XRPUSDT',
    'XRPBTC' : 'symbol=XRPBTC'}

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
interval_1min = '&interval=1m'

for key, symbol in crypto_symbols.items():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    xs = []
    ys = []
    coin = key
    recent_klines_url = binance_klines_url + symbol + interval_1min
    avg_price_url = binance_avgPrice_url + symbol
    current_time_request = requests.get(binance_time_url).json()    
    recent_trade_response = requests.get(recent_klines_url).json()
    avg_price_response = requests.get(avg_price_url).json()

    # print(recent_trade_response)    
    # print(avg_price_response)
    # print(current_time_request)
    # print(datetime.datetime.now())


    # Initialize communication with TMP102

    # This function is called periodically from FuncAnimation
    def animate(i, xs, ys):

        # Read temperature (Celsius) from TMP102
        for key in recent_trade_response:
            bt = key[0]
            # time.append(float(key[6]))
            pt = key[1]
            # price.append(float(key[4]))
            xs.append(bt)
            ys.append(pt)

        # Limit x and y lists to 20 items

        # Draw x and y lists
        ax.clear()
        ax.plot(xs, ys)

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title(f'{coin} Recent Klines')
        plt.ylabel('Price of Trade')

    # Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
    plt.show()
# dict_keys = list(response[0].keys())
# test_df = pd.DataFrame(response)

# print(test_df)
# with open('test.txt', mode='x') as textfile:
# for x in response:
#     print(f'{current_time_request}')
#     for key in dict_keys:
#         print(f'{key}: {x[key]}')
