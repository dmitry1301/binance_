from binance.client import Client
from config import api_key, api_secret, ASSET

client = Client(api_key, api_secret)


# Баланс
def balance(symbol):
    balance = client.get_asset_balance(asset=symbol)
    balance = {'free': balance['free'], 'locked': balance['locked']}
    return balance


# История
def history(symbol):
    history = client.get_my_trades(symbol=symbol)
    return history


# Курс
def price(symbol):
    price = client.get_avg_price(symbol=symbol)['price']
    return float(price)


# Ордер на покупку
def order_market_buy(quantity):
    order = client.order_market_buy(symbol=ASSET, quantity=quantity)


# Ордер на продажу
def order_market_sell(quantity):
    order = client.order_market_sell(symbol=ASSET, quantity=quantity)
    