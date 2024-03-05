import os
from binance.client import Client


class BinanceClientSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BinanceClientSingleton, cls).__new__(cls)
            api_key = os.getenv("BINANCE_API_KEY")
            api_secret = os.getenv("BINANCE_SECRET_KEY")
            cls._instance.client = Client(api_key, api_secret)
        return cls._instance

    @classmethod
    def get_client(cls):
        return cls()._instance.client