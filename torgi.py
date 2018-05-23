import ccxt
import time

symbol = 'BTC/USD'
amount = 10

bitmex = ccxt.bitmex({'apiKey': 'AbLgPxd4X-c0ucT3W6Db-RWB',
                      'secret': 'n6Y4tk45PAa5cO0KTvAn68ebRulu0qoMRlw0Sd8jUtsGibsZ',
                      'rateLimit': True})

if 'test' in bitmex.urls:
     bitmex.urls['api'] = bitmex.urls['test']  # ←----- switch the base URL to testnet
print(bitmex.fetch_balance())

price = bitmex.fetch_ticker('BTC/USD') #---get ticker
print(price)
result=bitmex.createLimitBuyOrder (symbol, amount, price['bid'])  #TODO внести правки сюда
time.sleep(3)

bitmex.edit_order(result['id'],'BTC/USD','limit',result['side'],price=8000,amount=50)

