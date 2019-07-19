import jsonlines
from requests import Session


def load_credentials():
        with jsonlines.open(r'C:\Users\Nubonix\pyscripts3\trading\nadex\Assets\nadex_credentials.json', 'r') as reader:
            for obj in reader:
                return obj['username'].upper(), obj['password'], obj['x-security-token']


LC = load_credentials()


def login():
        urls = [
            "https://trade.nadex.com/dealing/pd/cfd/security?action=authenticate",
            "https://trade.nadex.com//dealing/pd/cfd/checkbrowser?action=authenticate&webSiteId=ndx&businessArea=F&locale=en_US&bhjs=-1",
            "https://trade.nadex.com//dealing/pd/cfd/index.htm"
        ]

        headers = {
            "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding" : "gzip, deflate, br",
            "Accept-Language" : "en-US,en;q=0.9",
            "Cache-Control" : "max-age=0",
            "Connection" : "keep-alive",
            "Content-Length" : "113",
            "Content-Type" : "application/x-www-form-urlencoded",
            "DNT" : "1",
            "Host" : "trade.nadex.com",
            "Origin" : "https://www.nadex.com",
            "Referer" : "https://www.nadex.com/login",
            "Upgrade-Insecure-Requests" : "1",
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            'X-SECURITY-TOKEN': LC[2]
        }

        payload = {
            "account_id" : LC[0],
            "password" : LC[1],
            "onlineDealerVersion" : "LS",
            "businessArea" : "F",
            "webSiteId" : "ndx",
            "locale" : "en_US"
        }

        query = {"action" : "authenticate"}

        s = Session()

        for url in urls:
            s.post( url, headers=headers, params=payload, data=query )

        return s


if __name__ == "__main__":
    login()
