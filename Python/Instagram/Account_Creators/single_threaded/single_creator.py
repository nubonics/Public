
"""
    author: Sylar
    INSTAGRAM Mass Account Creator
"""
import json
import requests
import jsonlines
from time import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from concurrent.futures import ThreadPoolExecutor

# local imports
from modules.random_email_generator import first, second, passwd, random_email_generator
from modules.config import ASSET_DIR


def creator():
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    
    email = random_email_generator()
    email.replace('drag and drop', '')
    password = passwd()
    username = first() + second()
    first_name = first()

    url = "https://www.instagram.com/accounts/web_create_ajax/"

    headers = {
        'accept': "*/*",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.8",
        'content-length': "241",
        'content-type': 'application/x-www-form-urlencoded',
        'origin': "https://www.instagram.com",
        'referer': "https://www.instagram.com/",
        #'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
        'x-csrftoken': "0TKjZA9W7DDrqBjQaShyrYbULZSfujDb",
        'x-instagram-ajax': "c7e210fa2eb7",
        'x-requested-with': "XMLHttpRequest",
        'Upgrade-Insecure-Requests':'1',
        'Cache-Control': "no-cache",
    }
    payload = {
        #'email': email, #'annfranklen@live.com',
        'email': "avcodtimt@mailnesia.com",
        'password': password, #'Wonderhowsecurethisis',
        'username': username, #'annfranklen',
        'first_name': first_name, #'ann franklen',
        'client_id': 'W6mHTAAEAAHsVu2N0wGEChTQpTfn',
        'seamless_login_enabled': '1',
        'gdpr_s': '%5B0%2C2%2C0%2Cnull%5D',
        'tos_version': 'row',
        'opt_into_one_tap': 'false'
    }
	
    # PROVIDE YOUR OWN PROXY IP / PORT HERE
    # PROXY FORMAT: ip:port 
    # Example: 123.123.213.211:8080
	
	the_proxy = "your_proxy_and_port_go_here"

    proxy = {f"http":"socks5://{the_proxy}", f"https":"socks5://{the_proxy}"}

    request = requests.post(url, data = payload, headers = headers, proxies = proxy)
    print(request.text)
    
    try:
        response = json.loads(request.text)
    except:
        return

    try:
        if response['account_created'] == True:
            print(str(response['account_created']))
            mydict = dict()
            mydict['account_created'] = response['account_created']
            mydict['user_id'] = response['user_id']
            mydict['status'] = response['status']
            mydict['email'] = email.replace('\n','')
            mydict['password'] = password
            mydict['username'] = username
            mydict['first_name'] = first_name
            mydict['time_of_creation'] = time()

            file_path = str(ASSET_DIR + '/accounts.json').replace('\\','/')

            with jsonlines.open(file_path, 'a') as writer:
                writer.write(mydict)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    while True:
		try:
			creator()
		except:
			pass
