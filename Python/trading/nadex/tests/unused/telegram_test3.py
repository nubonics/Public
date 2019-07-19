import time
import jsonlines
from time import sleep
from telethon.sync import TelegramClient, events


def load_credentials():
    with jsonlines.open(r'C:\Users\Nubonix\pyscripts3\trading\nadex\Assets\telegram_api_credentials.json', 'r') as reader:
        for obj in reader:
            return obj['api_id'], obj['api_hash']

api_id = load_credentials()[0]
api_hash = load_credentials()[1]

channel_name = "AutoTrade"
account_name = 'autotradingaccount'


with TelegramClient(account_name, api_id, api_hash) as client:


    dialogs = client.iter_dialogs()

    def main_block():
        count = 1
        while True:
            # SLEEP IS REQUIRED!!!
            # Otherwise a single request could take up to a minute! INSTEAD of a 5 second delay!!!!!
            # We would rather have a 5 second delay on ALL messages received VS up to a minute delay!!!!!
            sleep(5)
            start = time.time()
            try:
                for x in dialogs:
                    if x.name == channel_name:
                        #print(x.message.message)
                        end = time.time()

                        total = end - start
                        if total > 1:
                            print(count, f'Took {total} seconds')

                        count += 1


            except KeyboardInterrupt:
                break

    if __name__ == "__main__":
        main_block()
