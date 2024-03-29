import os
import time
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException

logging.basicConfig(filename='dca.log', format='%(asctime)s %(message)s', encoding='utf-8', level=logging.INFO)

def safe_execute(action, *args, **kwargs):
    try:
        return action(*args, **kwargs)
    except BinanceAPIException as e:
        logging.error(f"Binance API Exception occurred: {e.status_code} - {e.message}")
    except BinanceOrderException as e:
        logging.error(f"Binance Order Exception occurred: {e.status_code} - {e.message}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    return None


if __name__ == '__main__':
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_SECRET')
    client = Client(api_key, api_secret)
    invest_amount = 500

    account_info = safe_execute(client.get_asset_balance, 'USDT')
    if account_info:
        account_usdt = float(account_info['free'])
        total_usdt = float(account_info['free']) + float(account_info['locked'])
    else:
        account_usdt = 0

    account_info = safe_execute(client.get_asset_balance, 'ADA')
    if account_info:
        account_ada = float(account_info['free'])
    else:
        account_ada = 0

    logging.info(f"Account Balance USDT = {account_usdt}, ADA = {account_ada}")


