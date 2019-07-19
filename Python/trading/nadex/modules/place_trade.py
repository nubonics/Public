import time
import jsonlines

# LOCAL IMPORTS
from login import login
from ttv import acquire_ttv
from epic import acquire_epic


L = login()


def load_credentials():
    with jsonlines.open(r'C:\Users\Nubonix\pyscripts3\trading\nadex\modules\nadex_credentials.json', 'r') as reader:
        for obj in reader:
            return obj['username'], obj['x-security-token']

LC = load_credentials()
username = LC[0]
token = LC[1]

def place_trade(epic, direction, size, price, ttv, asset, timeframe):
    url = "https://trade.nadex.com/iDeal/orders/workingorders/dma"

    data = {"direction": str(direction),
                "epic": str(epic),
                "lsServerName":"https://tra-upd.nadex.com",
                # how much to pay for a contract
                "orderLevel":str(price),
                # how many contracts
                "orderSize":str(size),
                "orderType":"MarketLimit",
                "pricePreference": None, #"null",
                "timeInForce":"GoodTillCancelled",
                "timeStamp": int(time.time()),
                "Cookie": {"X-SECURITY-TOKEN": token},
    }

    headers = {
        "Accept": "application/json; charset=UTF-8",
        "Content-Type": "application/json; charset=UTF-8",
        "Origin": "https://trade.nadex.com",
        "Referer": f'https://trade.nadex.com/fe/module/ticket/ticket.html?mode=ticket&EPIC={epic}&secToken={token}&accountID={username}&mode=ticket&openedFrom=dealingRates&EPIC={epic}&secToken={token}&accountID={username}&wow=2368.69250674835531000&wow=1562787101304 \
                    referrer: /fe/module/ticket/ticket.html?mode=ticket&EPIC={epic}&secToken={token}&accountID={username}&mode=ticket&openedFrom=dealingRates&EPIC={epic}&secToken={token}&accountID={username}&wow=2368.69250674835531000&wow=1562787101304&ttv={ttv}',
        "referer": f"/fe/module/ticket/ticket.html?mode=ticket&EPIC={epic}&secToken={token}&accountID={username}&mode=ticket&openedFrom=dealingRates&EPIC={epic}&secToken={token}&accountID={username}&wow=2368.69250674835531000&wow=1562787101304&ttv={ttv}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "x-device-user-agent": "vendor=IG Group | applicationType=ig | platform=Puredeal | version=4.13.0",
    }

    r = L.post(url, json = data, headers = headers)

    print(r.text)
    print(r.cookie)


if __name__ == "__main__":
    place_trade(epic, direction, size, price, ttv, asset, timeframe)
