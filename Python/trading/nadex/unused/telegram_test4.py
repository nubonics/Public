import jsonlines
from time import sleep
from telethon.sync import TelegramClient


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


    def main_block():


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

                        if latest_message_id > previous_message_id:
                            print(dialog.message.message)
                            write_lastest_message_id()



            except KeyboardInterrupt:
                break

    if __name__ == "__main__":
        write_lastest_message_id()
        main_block()
