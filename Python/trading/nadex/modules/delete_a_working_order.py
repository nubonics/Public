import time
import requests


def delete_a_working_order(deal_id, deal_reference, SECTOKEN, DIRECTION, TP_PRICE, username):
    
    the_time = str(int(time.time()))

    url = 'https://trade.nadex.com/iDeal/orders/workingorders/dma/' + deal_id

    headers = {
        'x-device-user-agent': 'vendor=IG Group | applicationType=ig | platform=Puredeal | version=4.13.0',
        'Origin': 'https://trade.nadex.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Content-Type': 'application/json; charset=UTF-8',
        'X-SECURITY-TOKEN': SECTOKEN,
        'Accept': 'application/json; charset=UTF-8',
        'Referer': f'https://trade.nadex.com/fe/module/ticket/ticket.html?mode=workingOrder&EPIC=&dealId=ticket.html?mode=workingOrder&openedFrom=entryOrders&EPIC={deal_id}&dealId={deal_id}&secToken={SECTOKEN}&accountID={USERNAME}&secToken={SECTOKEN}&accountID={USERNAME}',
        'Connection': 'keep-alive',
        'DNT': '1',
    }

    data = '{"dealId":"' + deal_id + '","guaranteedStop":false,"dealReference":"' + deal_reference + '","direction":"'+ DIRECTION +'","exchangeId":"HS_NADEX","trailingStop":false,"trailingStopDistanceFormatted":null,"trailingStopIncrementFormatted":null,"dma":true,"dmaData":{"orderType":"'+ DIRECTION_NUMBER + '","timeInForce":"1","originalSize":' + HOW_MANY_CONTRACTS + ',"pseudoPosition":false},"currencyData":{"code":"$.","name":"USD","symbol":"$","ticketDefault":false,"exchangeRate":null,"baseExchangeRate":null,"isDefault":false},"sizeFormatted":"1","submitOrderType":5,"requestType":"UL","limitDistanceFormatted":"","stopDistanceFormatted":null,"trailingTriggerStopDistanceFormatted":null,"trailingTriggerStepDistanceFormatted":null,"goodTillData":null,"channel":null,"triggerLevel":' + TP_PRICE + ',"timeStamp":' + the_time + ',"lsServerName":"https://net-mdp1a.igindex.co.uk","timeInForce":"GoodTillCancelled","orderType":"MarketLimit"}'

    response = requests.delete(url, headers=headers, data=data)

    return response.json()


if __name__ == "__main__":
    delete_a_working_order(deal_id, deal_reference, SECTOKEN, DIRECTION, TP_PRICE, username)
