import requests


def deal_reference(deal_id, SECTOKEN, username):

    url = f'https://trade.nadex.com/iDeal/v2/markets/details/workingorders/{deal_id}'

    headers = {
        'x-device-user-agent': 'vendor=IG Group | applicationType=ig | platform=Puredeal | version=4.13.0',
        'DNT': '1',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Content-Type': 'application/json; charset=UTF-8',
        'X-SECURITY-TOKEN': SECTOKEN,
        'Accept': 'application/json; charset=UTF-8',
        'Referer': f'https://trade.nadex.com/fe/module/ticket/ticket.html?mode=workingOrder&EPIC=&dealId=ticket.html?mode=workingOrder&openedFrom=entryOrders&EPIC={deal_id}&dealId={deal_id}&secToken={SECTOKEN}&accountID={username}&secToken={SECTOKEN}&accountID={username}',
        'Connection': 'keep-alive',
    }

    response = requests.get(url, headers=headers)

    reference = response.json()['workingOrderData']['dealReference']

    return reference

if __name__ == "__main__":
    deal_reference(deal_id, SECTOKEN, username)
