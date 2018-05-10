import ccxt
from variable import *
import logging
logging.basicConfig(level=logging.DEBUG)
import aroon
import time

#start_time = time.time() - 24 * 60 * 60
bitmex = ccxt.bitmex({'rateLimit': True})

while True:
    data = bitmex.fetch_ohlcv('BTC/USD', tf, period, params={'reverse': 'true', 'partial': 'false'})
    result = aroon.aroon(data)
    print('-'*20)
    print(result)
    time.sleep(20)  # in seconds

# # yourdate = dateutil.parser.parse(k)
# # print(yourdate)
