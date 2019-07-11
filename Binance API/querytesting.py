import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import urllib
import datetime
import pymongo
from pprint import pprint as pprint

crypto_symbols = {
    'LTCBTC' : 'symbol=LTCBTC',
    'ETHUSDT' : 'symbol=ETHUSDT',
    'BTCUSDT' : 'symbol=BTCUSDT',
    'ETHBTC' : 'symbol=ETHBTC',
    'BCCBTC' : 'symbol=BCCBTC',
    'XRPBTC' : 'symbol=XRPBTC'}

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

for key, symbol in crypto_symbols.items():
    db = client[f'{key}']
    coll = db[f'Binance API']

    f = coll.find({'Binance Time' : 1562378372531})
    for x in f:
        print(x)