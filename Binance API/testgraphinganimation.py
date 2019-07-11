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
binance_time_url = 'https://api.binance.com/api/v1/time?'
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


interval_1min = '&interval=1m'
symbol = 'symbol=XRPUSDT'
# def klinedata():
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client['XRPUSDT']
coll = db['1minklinedata']
current_time_request = requests.get(binance_time_url).json() 
recent_klines_url = binance_klines_url + symbol + interval_1min
avg_price_url = binance_avgPrice_url + symbol
recent_trade_response = requests.get(recent_klines_url).json()
avg_price_response = requests.get(avg_price_url).json()
realtime = dt.datetime.now()
print(realtime)
print(current_time_request['serverTime'])
for trade in recent_trade_response:
    tradedump = {}
    tradedump = {
        'open_time' : int(trade[0]),
        'open_price' : float(trade[1]),
        'high_price' : float(trade[2]),
        'low_price' : float(trade[3]),
        'close_price' : float(trade[4]),
        'volume' : float(trade[5]),
        'close_time' : int(trade[6]),
        'quote_asset_volume' : float(trade[7]),
        'number_of_trades' : float(trade[8]),
        'taker_buy_base_asset_volume' : float(trade[9]),
        'taker_buy_quote_asset_volume' : float(trade[10]),
        'ignore' : float(trade[11])
    }
    coll.insert_one(tradedump)
    # return current_time_request, recent_trade_response, avg_price_response, realtime
query = coll.find({"close_time": {"$gt": current_time_request['serverTime']}})
for x in query:
    print(x)
# fig, ax = plt.subplots()

# x = np.arange(0, 2*np.pi, 0.01)
# line, = ax.plot(x, np.sin(x))


# def init():  # only required for blitting to give a clean slate.
#     line.set_ydata([np.nan] * len(x))
#     return line,


# def animate(i):
#     line.set_ydata(np.sin(x + i / 100))  # update the data.
#     return line,


# ani = animation.FuncAnimation(
#     fig, animate, init_func=init, interval=5, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()