import time
import requests
import jsonlines
from update_x_security_token import update_x_security_token
from current_price import acquire_current_price
from ttv import acquire_ttv


# EPIC = 'NB.D.AUD-JPY.OPT-29-11-19Jul19.IP'
EPIC = 'NB.D.EUR-USD.OPT-29-9-19Jul19.IP'
DIRECTION = '+'
#SECTOKEN = 'e46ef57fc9897d45df1b52d8b09168c3654451f350adbd2dfebb675690148699'
# SECTOKEN = 'e46ef57fc9897d45df1b52d8b09168c3654451f350adbd2dfebb675690148699'
SECTOKEN = '3e449d0676f5ee149a6e5dbdc0aeae65be7ea45cddf3c6fff2ae52d0f23e8e88'
USERNAME = 'SPARROWSWORD'
# TTV = 'af7c768e8bc62d20a87bb24646564bbd'
#TTV = acquire_ttv(epic=EPIC)
TTV = 'd378344d9262238e92639884b6354f97'


# THIS VALUE STAYS THE SAME UNTIL A GREATER THAN $1000 ACCOUNT BALANCE NO MATTER WHAT
RAW_HOW_MANY_CONTRACTS = 1
HOW_MANY_CONTRACTS = str(RAW_HOW_MANY_CONTRACTS)

# FOR TESTING PURPOSES WE WILL USE THE VALUE OF $1 SO THE ORDER IS EXTREMELY UNLIKELY TO BE FILLED

RAW_PRICE_PER_CONTRACT = 1.00
PRICE_PER_CONTRACT = str(RAW_PRICE_PER_CONTRACT)

CURRENT_PRICE = acquire_current_price(epic=EPIC)




headers = {
    'x-device-user-agent': 'vendor=IG Group | applicationType=ig | platform=Puredeal | version=4.13.0',
    'Origin': 'https://trade.nadex.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'referrer': f'/fe/module/ticket/ticket.html?mode=ticket&EPIC={EPIC}&SECTOKEN={SECTOKEN}&accountID={USERNAME}&mode=ticket&openedFrom=dealingRates&EPIC={EPIC}&SECTOKEN={SECTOKEN}&accountID={USERNAME}&ttv={TTV}',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Content-Type': 'application/json; charset=UTF-8',
    'X-SECURITY-TOKEN': f'{SECTOKEN}',
    'Accept': 'application/json; charset=UTF-8',
    'Referer': f'https://trade.nadex.com/fe/module/ticket/ticket.html?mode=ticket&EPIC={EPIC}&SECTOKEN={SECTOKEN}&accountID={USERNAME}&mode=ticket&openedFrom=dealingRates&EPIC={EPIC}&SECTOKEN={SECTOKEN}&accountID={USERNAME}',
    'Connection': 'keep-alive',
    'DNT': '1',
}

# timeStamp is required, however, a value of zero does work
data = '{' + '"epic":"{}"'.format(EPIC) + ',"direction":"' + DIRECTION + '","orderSize":"' + HOW_MANY_CONTRACTS + '","orderLevel":"' + PRICE_PER_CONTRACT +'","timeStamp":0,"lsServerName":"https://tra-upd.nadex.com","timeInForce":"GoodTillCancelled","orderType":"MarketLimit","pricePreference":null}'

response = requests.post('https://trade.nadex.com/iDeal/orders/workingorders/dma', headers=headers, data=data)

"""
if "error.unhandled-HttpSessionRequiredException" == response.json()['globalErrors'][0] or "token invalid" in response.json()['globalErrors'][0]:
        update_x_security_token()
        response = requests.post('https://trade.nadex.com/iDeal/orders/workingorders/dma', headers=headers, data=data)

"""
print(response.json())


"""
# print(f'response from placing_trade_v3: {response.text}')
text = response.json()['globalErrors'][0]

if 'token invalid' in text:
    print('x-security-token was not updated')
"""