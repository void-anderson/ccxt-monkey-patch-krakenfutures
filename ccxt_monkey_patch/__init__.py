from types import ModuleType
import ccxt

def patch(ccxt: ModuleType) -> ModuleType:
    return ccxt

patch(ccxt)
