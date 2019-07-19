import os
import time
import jsonlines
from time import sleep
from telethon.sync import TelegramClient
from requests.exceptions import MissingSchema

# LOCAL IMPORTS
from epic import acquire_epic
from ttv import acquire_ttv
from deal_reference import deal_reference
from place_order_v3 import place_order_v3
from current_price import acquire_current_price
from acquire_working_orders import working_orders


def load_telegram_credentials():
    with jsonlines.open(r'C:\Users\Nubonix\pyscripts3\trading\nadex\Assets\telegram_api_credentials.json', 'r') as reader:
        for obj in reader:
            return obj['api_id'], obj['api_hash']

def load_nadex_credentials():
    with jsonlines.open(r'C:\Users\Nubonix\pyscripts3\trading\nadex\Assets\nadex_credentials.json', 'r') as reader:
        for obj in reader:
            return obj['username'], obj['x-security-token']


LC = load_telegram_credentials()
api_id = LC[0]
api_hash = LC[1]

NC = load_nadex_credentials()
username = NC[0]
x_security_token = NC[1]

channel_name = "AutoTrade"
account_name = 'autotradingaccount'


with TelegramClient(account_name, api_id, api_hash) as client:


    dialogs = client.iter_dialogs()

    def write_lastest_message_id():
        """ This is similar to reading an unread message through email, however this is for telegram instead. """
        for dialog in dialogs:
            if dialog.name == channel_name:
                with open('lastest_message_id.txt','w') as writer:
                    # print(dialog.message.id)
                    writer.write(str(dialog.message.id))
    
    
    def get_latest_message_id():
        with open('lastest_message_id.txt','r') as reader:
            message_id = int(reader.readline())
            return message_id

    def buy(asset, epic, price, strike):
        print('bought')
    
    def sell(asset, epic, price, strike):
        print('sold')
        #pass

    def close_buy(asset, epic, price, strike):
        print('closing buy')
        #pass

    def close_sell(asset, epic, price, strike):
        print('closing sell')
    
    def parse_price(price):
        ''' HAS NOT YET BEEN IMPLIMENTED '''
        return price

    def get_latest_message():

        message_filter = ['WORKING ORDER FOR ',
                    'SELL',
                    'BUY',
                    'FILLED',
                    'TP TARGET HIT ON THE',
                    'ALERT COMING',
        ]

        os.system('cls')
        print('Listening... for signals...')

        while True:
            # SLEEP IS REQUIRED!!!
            # Otherwise a single request could take up to a minute! INSTEAD of a 5 second delay!!!!!
            # We would rather have a 5 second delay on ALL messages received VS up to a minute delay!!!!!
            sleep(5)
            try:
                for dialog in dialogs:
                    if dialog.name == channel_name:
                        latest_message_id = dialog.message.id
                        previous_message_id = get_latest_message_id()

                        if latest_message_id > get_latest_message_id():
                            # Update the latest_message_id so that we dont act upon the same message multiple times
                            write_lastest_message_id()
                            
                            # DO SOMETHING WITH THE MESSAGE NOW
                            msg = str(dialog.message.message).upper()


                            # Acquire information / signal
                            if message_filter[2] in msg and message_filter[4] not in msg or message_filter[1] in msg and message_filter[4] not in msg:
                                ASSET = msg.split('(')[0]

                                # Make sure that we arent missing out on a trade because of 1 letter
                                if "P" in msg and "M" not in msg:
                                    msg.replace('P','PM')
                                if "A" in msg and "M" not in msg:
                                    msg.replace('A', 'AM')
                                TIMEFRAME = msg.split('(')[1].split(')')[0]
                                STRIKE = msg.split(')(')[2].split(')')[0]

                                if "BUY" in msg:
                                    DIRECTION = "+"

                                if "SELL" in msg:
                                    DIRECTION = "-"

                                # Create a record of trades made (even though this is already done by Nadex)
                                signal = dict()
                                signal['asset'] = str(ASSET)
                                signal['timeframe'] = str(TIMEFRAME)
                                signal['strike'] = str(STRIKE)
                                signal['direction'] = str(DIRECTION)
                                signal['timestamp'] = str(time.time())

                                print('singal was read')

                                with jsonlines.open('signal.json', 'a') as writer:
                                    writer.write(signal)

                                try:
                                    EPIC = acquire_epic(asset=ASSET, timeframe=TIMEFRAME, strike=STRIKE)
                                except MissingSchema:
                                    print(f'Please add the URL for {ASSSET} of the timeframe: {TIMEFRAME} to epic.py')
                                    continue

                                TTV = acquire_ttv(epic=EPIC)
                                CURRENT_PRICE = acquire_current_price(epic=EPIC)[0]

                            # Place the order
                            if message_filter[0] in msg:                                
                                PRICE = msg.split(message_filter[0])[1].split(' OR BETTER')[0].replace('$','')
                                if "+" in DIRECTION:
                                    place_order_v3(EPIC=EPIC,
                                                    DIRECTION = DIRECTION,
                                                    SECTOKEN = x_security_token,
                                                    USERNAME = username,
                                                    TTV = TTV,
                                                    # 1 Contract until a MINIMUIM OF A $1000 ACCOUNT BALANCE HAS BEEN REACHED
                                                    # 1.00 is for TESTING PURPOSES ONLY
                                                    HOW_MANY_CONTRACTS = str(1.00),
                                                    # 1.00 is for TESTING PURPOSES ONLY
                                                    # FOR LIVE USE ~> COMMENT OUT THE NEXT LINE AND ADD `PRICE_PER_CONTRACT=str( price() )`
                                                    PRICE_PER_CONTRACT = str(1),
                                                    CURRENT_PRICE = CURRENT_PRICE
                                    )

                                if "-" == DIRECTION:
                                    sell(asset=ASSET, epic=EPIC, price=PRICE, strike=STRIKE)

                            def order_was_never_filled_in_time():
                                """ TO BE IMPLIMENTED """
                                """ If the working order was placed, and was not filled within 27 minutes, close/cancel the working order """
                                pass

                            # MAKE SURE WE ARENT accidently placing an order instead of closing a trade

                            # HAS NOT YET BEEN IMPLIMENTED

                            # Take Profits
                            if message_filter[4] in msg:
                                if "+" in DIRECTION:
                                    close_buy(asset=ASSET, epic=EPIC, price=PRICE, strike=STRIKE)

                                if "-" in DIRECTION:
                                    close_sell(asset=ASSET, epic=EPIC, price=PRICE, strike=STRIKE)
          
            except KeyboardInterrupt:
                break

    def main():
        # write_latest_message_id() is required in order for get_latest_message() to work properly...
        # DO NOT DELETE the next line which is write_latest_message_id()
        write_lastest_message_id()
        get_latest_message()

    if __name__ == "__main__":
        main()
