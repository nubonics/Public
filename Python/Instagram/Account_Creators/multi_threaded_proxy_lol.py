
"""
    author: Sylar
    INSTAGRAM Mass Account Creator
"""
import json
import queue
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
        'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
        'x-csrftoken': "0TKjZA9W7DDrqBjQaShyrYbULZSfujDb",
        'x-instagram-ajax': "c7e210fa2eb7",
        'x-requested-with': "XMLHttpRequest",
        'Upgrade-Insecure-Requests':'1',
        'Cache-Control': "no-cache",
    }
    payload = {
        'email': email,
        'password': password,
        'username': username,
        'first_name': first_name,
        'client_id': 'W6mHTAAEAAHsVu2N0wGEChTQpTfn',
        'seamless_login_enabled': '1',
        'gdpr_s': '%5B0%2C2%2C0%2Cnull%5D',
        'tos_version': 'row',
        'opt_into_one_tap': 'false'
    }

    # PROVIDE YOUR OWN PROXY IP / PORT HERE
    # PROXY FORMAT: ip:port 
    # Example: 123.123.213.211:8080
    
    proxy = {"http":"https://" + the_proxy_data, "https":"https://" + the_proxy_data}

    try:
        request = requests.post(url, data = payload, headers = headers, proxies = proxy, timeout = 25)
    except:
        return

    try:
        response = json.loads(request.text)
    except:
        return

    if "'account_created'" == request.text:
        return

    if response['account_created'] == 'false':
        return

    if response['message'] == 'Please wait a few minutes before you try again.':
        if response['status'] == 'fail':
            return

    try:
        if response['account_created'] == True:
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
            print("mydict: " + mydict)
            with jsonlines.open(file_path, 'a') as writer:
                writer.write(mydict)
    except Exception as e:
        print(e)


if __name__ == "__main__":

    q = queue.Queue()

    executor = ThreadPoolExecutor(max_workers=4)

    try:
        while True:
            a = executor.submit(creator)
    except:
        pass
