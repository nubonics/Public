# LOCAL IMPORTS
from login import login


L = login()

def acquire_ttv(epic):
    base_url = "https://trade.nadex.com/iDeal/v2/markets/details/"

    response = L.get(base_url + epic)

    # print(response.text)

    ttv = response.json()['metaData']['ttv']

    bid = response.json()['marketSnapshotData']['bidFormatted']
    offer = response.json()['marketSnapshotData']['offerFormatted']
    print(bid, offer)

    print(ttv)
    return ttv

if __name__ == "__main__":
    acquire_ttv(epic)
