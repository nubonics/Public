# LOCAL IMPORTS
from login import login


L = login()

def acquire_current_price(epic):
    base_url = "https://trade.nadex.com/iDeal/v2/markets/details/"

    response = L.get(base_url + epic)

    data = response.json()

    bid = data['marketSnapshotData']['bidFormatted']
    offer = data['marketSnapshotData']['offerFormatted']
    return bid, offer


if __name__ == "__main__":
    acquire_current_price(epic)
