import os
import unittest

# Get the two below from futures-demo.kraken.com
api_key = os.getenv('API_KEY', None)
api_secret = os.getenv('API_SECRET', None)
dev = False 

from ccxt_monkey_patch import KrakenFutures, get_kf_patch

kf = None

class TestCCXT(unittest.TestCase):
    kf = get_kf_patch(KrakenFutures)
    kf.set_sandbox_mode(True)
    kf.verbose = True
    kf.apiKey = api_key
    kf.secret = api_secret

    def test_connection(self):
        # Set API_KEY and SECRET
        self.assertNotEqual(api_key, None)
        self.assertNotEqual(api_secret, None)

    def test_can_fetch_balance(self):
        balance = self.__class__.kf.fetch_balance()
        print("fetching balance...")

    def test_can_fetch_markets(self):
        self.__class__.kf.fetch_markets()
        print("fetching markets...")

    def test_can_get_order_status(self):
        # Create an Order
        self.__class__.kf.create_order(
            'ETH/USD:ETH-231229',
            'limit',
            'sell',
            1,
            float(2000)
        )
        # get open orders
        self.__class__.kf.fetch_open_orders(
            'ETH/USD:ETH-231229',
        )
        order_id = orders[0]['info']['order_id']
        # get order status
        self.__class__.kf.fetch_order(order_id)
        

if __name__ == '__main__':
    unittest.main()
