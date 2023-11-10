from ccxt.base.types import Entry
import ccxt

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

def create_order_status_request()
    pass

def get_kf_patch():
    kf = ccxt.krakenfutures()

    # Patch ImplicitAPI entries
    kf = patch_entry(kf)

    # Make fetchOrder available
    kf.has['fetchOrder'] = True 
    
    # add api
    kf.api['private']['post'].append('orders/status')

    return kf 

get_kf_patch(ccxt)
