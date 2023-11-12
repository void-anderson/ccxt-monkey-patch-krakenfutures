from typing import Optional
from ccxt import krakenfutures as KrakenFuturesCCXT
from ccxt.base.types import Entry

def patch_entry(kf):
    entry = Entry(
        'orders/status', 
        'private', 
        'POST', 
        {},
    )
    kf.private_post_orders_status = entry
    kf.privatePostOrdersStatus = entry
    return kf


def get_kf_patch(krakenfutures):
    kf = krakenfutures({ 
        'has': { 'fetchOrder': True } 
    })

    # add api
    kf.api['private']['post'].append('orders/status')

    # Patch ImplicitAPI entries
    kf = patch_entry(kf)

    return kf 

class KrakenFutures(KrakenFuturesCCXT):

    def fetch_order(
        self, 
        id: str, 
        symbol: Optional[str] = None, 
        params={}
    ):
        self.load_markets()
        orderIds = [id,]
        request = self.extend({'orderIds': orderIds}, params)
        response = self.privatePostOrdersStatus(request)
        data = self.safe_value(response, 'orders', [])
        return self.parse_orders(data)