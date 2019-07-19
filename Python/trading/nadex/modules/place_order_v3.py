import time
import requests
import jsonlines
from update_x_security_token import update_x_security_token


def place_order_v3(EPIC,DIRECTION,SECTOKEN,USERNAME,TTV,HOW_MANY_CONTRACTS,PRICE_PER_CONTRACT,CURRENT_PRICE):
    """
    EPIC = 'NB.D.AUD-USD.OPT-23-12-18Jul19.IP'
    DIRECTION = '+'
    SECTOKEN = '89e88d573b53d965e386deb981c9331c0fc893fe31c807546700f6c2ec5c037c'
    USERNAME = 'SPARROWSWORD'
    TTV = '37e908d5885d27cdad047802a241eb10'

    # THIS VALUE STAYS THE SAME UNTIL A GREATER THAN $1000 ACCOUNT BALANCE NO MATTER WHAT
    RAW_HOW_MANY_CONTRACTS = 1
    HOW_MANY_CONTRACTS = str(RAW_HOW_MANY_CONTRACTS)

    # FOR TESTING PURPOSES WE WILL USE THE VALUE OF $1 SO THE ORDER IS EXTREMELY UNLIKELY TO BE FILLED

    RAW_PRICE_PER_CONTRACT = 1.00
    PRICE_PER_CONTRACT = str(RAW_PRICE_PER_CONTRACT)
    """



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
        'Referer': f'https://trade.nadex.com/fe/module/ticket/ticket.html?mode=ticket&EPIC={EPIC}&secToken={SECTOKEN}&accountID=SPARROWSWORD&mode=ticket&openedFrom=dealingRates&EPIC={EPIC}&secToken={SECTOKEN}&accountID=SPARROWSWORD',
        'Connection': 'keep-alive',
        'DNT': '1',
    }

    # timeStamp is required, however, a value of zero does work
    data = '{' + '"epic":"' + EPIC +'"' + ',"direction":"' + DIRECTION + '","orderSize":"' + HOW_MANY_CONTRACTS + '","orderLevel":"' + PRICE_PER_CONTRACT +'","timeStamp":0,"lsServerName":"https://tra-upd.nadex.com","timeInForce":"GoodTillCancelled","orderType":"MarketLimit","pricePreference":null}'

    response = requests.post('https://trade.nadex.com/iDeal/orders/workingorders/dma', headers=headers, data=data)


    try:
        # If the X-SECURITY-TOKEN has expired, obtain a new one...
        if "error.unhandled-HttpSessionRequiredException" == response.json()['globalErrors'][0] or "token invalid" in response.json()['globalErrors'][0]:
            update_x_security_token()
            response = requests.post('https://trade.nadex.com/iDeal/orders/workingorders/dma', headers=headers, data=data)
    except:
        pass


    print(response.json())

    # print(f'response from placing_trade_v3: {response.text}')

    with jsonlines.open('last_order_placed.json','w') as writer:
        writer.write(response.json())

    with jsonlines.open('orders_placed.json', 'a') as writer:
        writer.write(response.json())

    if 'tokenVO' in response.text:
        print('Order has been placed.')


if __name__ == "__main__":
    place_order_v3(EPIC,DIRECTION,SECTOKEN,USERNAME,TTV,HOW_MANY_CONTRACTS,PRICE_PER_CONTRACT,CURRENT_PRICE)
