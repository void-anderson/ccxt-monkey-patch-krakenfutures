from typing import Optional
from ccxt import krakenfutures as KrakenFuturesCCXT
from ccxt.base.types import Entry
import types

def get_kf_patch(krakenfutures):
    kf = krakenfutures({ 
        'has': { 'fetchOrder': True } 
    })

    # add api
    kf.api['private']['post'].append('orders/status')
    return kf 

class KrakenFutures(KrakenFuturesCCXT):

    private_post_orders_status = privatePostOrdersStatus = Entry(
        'orders/status', 
        'private', 
        'POST', 
        {},
    ) 

    def fetch_order(
        self, 
        id: str, 
        symbol: Optional[str] = None, 
        params={}
    ):
        self.load_markets()
        request = self.extend({'orderIds': id}, params)
        response = self.privatePostOrdersStatus(request)
        data = self.safe_value(response, 'orders', [])
        return self.parse_orders(data)