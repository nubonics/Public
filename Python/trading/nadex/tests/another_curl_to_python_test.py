import requests

headers = {
    'x-device-user-agent': 'vendor=IG Group | applicationType=ig | platform=Puredeal | version=4.13.0',
    'Origin': 'https://trade.nadex.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'referrer': '/fe/module/ticket/ticket.html?mode=ticket&EPIC=NB.D.AUD-JPY.OPT-29-11-19Jul19.IP&secToken=fffc511594145bd81c808910cc7ab0255d590de04676737cb56320470c75cf57&accountID=SPARROWSWORD&mode=ticket&openedFrom=dealingRates&EPIC=NB.D.AUD-JPY.OPT-29-11-19Jul19.IP&direction=-&openLevel=99.75&secToken=fffc511594145bd81c808910cc7ab0255d590de04676737cb56320470c75cf57&accountID=SPARROWSWORD&wow=4526.8692480619621000&wow=1563553773063&ttv=2d5cde3735789d4242330cc1df0758a0',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Content-Type': 'application/json; charset=UTF-8',
    'X-SECURITY-TOKEN': 'fffc511594145bd81c808910cc7ab0255d590de04676737cb56320470c75cf57',
    'Accept': 'application/json; charset=UTF-8',
    'Referer': 'https://trade.nadex.com/fe/module/ticket/ticket.html?mode=ticket&EPIC=NB.D.AUD-JPY.OPT-29-11-19Jul19.IP&secToken=fffc511594145bd81c808910cc7ab0255d590de04676737cb56320470c75cf57&accountID=SPARROWSWORD&mode=ticket&openedFrom=dealingRates&EPIC=NB.D.AUD-JPY.OPT-29-11-19Jul19.IP&direction=-&openLevel=99.75&secToken=fffc511594145bd81c808910cc7ab0255d590de04676737cb56320470c75cf57&accountID=SPARROWSWORD&wow=4526.8692480619621000&wow=1563553773063',
    'Connection': 'keep-alive',
    'DNT': '1',
}

data = '{"epic":"NB.D.AUD-JPY.OPT-29-11-19Jul19.IP","direction":"+","orderSize":"1","orderLevel":"1.00","timeStamp":1563553790,"lsServerName":"https://tra-upd.nadex.com","timeInForce":"GoodTillCancelled","orderType":"MarketLimit","pricePreference":null}'

response = requests.post('https://trade.nadex.com/iDeal/orders/workingorders/dma', headers=headers, data=data)

print(response.json())
