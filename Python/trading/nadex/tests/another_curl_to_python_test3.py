import requests


headers = {
    'x-device-user-agent': 'vendor=IG Group | applicationType=ig | platform=Puredeal | version=4.13.0',
    'Origin': 'https://trade.nadex.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'referrer': '/fe/module/ticket/ticket.html?mode=ticket&EPIC=NB.I.AUD-USD.OPT-260-6-19Jul19.IP&secToken=14c3575e57e9c03b7519a2a6dcd6a837045bf8e120cf656669369241128bf017&accountID=SPARROWSWORD&mode=ticket&openedFrom=dealingRates&EPIC=NB.I.AUD-USD.OPT-260-6-19Jul19.IP&secToken=14c3575e57e9c03b7519a2a6dcd6a837045bf8e120cf656669369241128bf017&accountID=SPARROWSWORD&ttv=0c0da221b46c65810de90d0fe6a80544',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Content-Type': 'application/json; charset=UTF-8',
    'X-SECURITY-TOKEN': '14c3575e57e9c03b7519a2a6dcd6a837045bf8e120cf656669369241128bf017',
    'Accept': 'application/json; charset=UTF-8',
    'Referer': 'https://trade.nadex.com/fe/module/ticket/ticket.html?mode=ticket&EPIC=NB.I.AUD-USD.OPT-260-6-19Jul19.IP&secToken=14c3575e57e9c03b7519a2a6dcd6a837045bf8e120cf656669369241128bf017&accountID=SPARROWSWORD&mode=ticket&openedFrom=dealingRates&EPIC=NB.I.AUD-USD.OPT-260-6-19Jul19.IP&secToken=14c3575e57e9c03b7519a2a6dcd6a837045bf8e120cf656669369241128bf017&accountID=SPARROWSWORD',
    'Connection': 'keep-alive',
    'DNT': '1',
}

data = '{"epic":"NB.I.AUD-USD.OPT-260-6-19Jul19.IP","direction":"+","orderSize":"1","orderLevel":"1.00","timeStamp":0,"lsServerName":"https://tra-upd.nadex.com","timeInForce":"GoodTillCancelled","orderType":"MarketLimit","pricePreference":null}'

response = requests.post('https://trade.nadex.com/iDeal/orders/workingorders/dma', headers=headers, data=data)

print(response.json())