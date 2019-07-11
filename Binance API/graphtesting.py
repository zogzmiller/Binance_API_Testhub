import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np
import requests
import time
import urllib
import pymongo
import datetime as dt
import celluloid
from celluloid import Camera

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
interval_3min = '&interval=3m'
interval_5min = '&interval=5m'
interval_15min = '&interval=15m'


    
# go = True

# while go is True:
for key, symbol in crypto_symbols.items():
    coin = key
    recent_klines_url = binance_klines_url + symbol + interval_1min
    avg_price_url = binance_avgPrice_url + symbol
    current_time_request = requests.get(binance_time_url).json()    
    recent_trade_response = requests.get(recent_klines_url).json()
    avg_price_response = requests.get(avg_price_url).json()
    realtime = dt.datetime.now()
    kot = []
    kop = []
    kct = []
    kcp = []
    vol = []
    tbvol = []
    trades = []
    for key in recent_trade_response:
        klineopentime = int(key[0])
        klineopenprice = float(key[1])
        klinecloseprice = float(key[4])
        klinevolume = float(key[5])
        klineclosetime = int(key[6])
        numberoftrades = int(key[8])
        klinetbvolume = float(key[9])
        kot.append(klineopentime)
        kop.append(klineopenprice)
        kct.append(klineclosetime)
        kcp.append(klinecloseprice)
        vol.append(klinevolume)
        tbvol.append(klinetbvolume)
        trades.append(numberoftrades)
    fig, axes = plt.subplots(2)
    camera = Camera(fig)
    axes[0].plot(kot, kop, color = 'green')
    axes[0].plot(kct, kcp, color = 'red')
    axes[1].plot(kct, vol, color = 'blue')
    axes[1].plot(kct, tbvol, color = 'purple')
    plt.xlabel(f'{current_time_request, realtime}')
    plt.ylabel(f'{avg_price_response}')
    plt.title(f'{coin} Kline Open/Close Price Data')
    plt.xlabel(f'{current_time_request, realtime}')
    plt.ylabel(f'{avg_price_response}')
    plt.title(f'{coin} Kline Volume/Taker Buyer Volume Data')
    camera.snap()		    
    animation = camera.animate()
    plt.tight_layout()
    plt.show()