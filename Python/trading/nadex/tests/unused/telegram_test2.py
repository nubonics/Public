import jsonlines
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


    dialogs = client.get_dialogs()

    def write_lastest_message_id():
        """ This is similar to reading an unread message through email, however this is for telegram instead. """
        for each_dialog in range(len(dialogs)):
                dialog = dialogs[each_dialog]
                if dialog.name == channel_name:
                    with open('lastest_message_id.txt','w') as writer:
                        # print(dialog.message.id)
                        writer.write(str(dialog.message.id))
    
    
    def get_latest_message_id():
        with open('lastest_message_id.txt','r') as reader:
            message_id = int(reader.readline())
            return message_id


    def single_block():
        get_latest_message_id()
        for each_dialog in range(len(dialogs)):
            dialog = dialogs[each_dialog]
        
            # Look for the latest message, and make sure we arent making calls on a message for than once (for trading purposes)
            if dialog.name == channel_name:
                # print(dialog.message.id)
                print(dialog.message.message)

    def expirimental_block():
        while True:
            for each_dialog in range(len(dialogs)):
                dialog = dialogs[each_dialog]
                if dialog.name == channel_name:
                    # print(dialog.message.id)
                    print(dialog.message.message)

    def main_block():
        while True:
            # for testing purposes we will use a try/except block, so that we cant exit the program via the keyboard
            try:
                for each_dialog in range(len(client.dialogs)):
                    dialog = dialogs[each_dialog]
                
                    # Look for the latest message, and make sure we arent making calls on a message for than once (for trading purposes)
                    if dialog.name == channel_name:
                        glmi = get_latest_message_id()
                        print(dialog.message.id, glmi)
                        if dialog.message.id > glmi:
                            #print(dialog.message.date)
                            print(dialog.message.message)
            except KeyboardInterrupt:
                break


    if __name__ == "__main__":
        write_lastest_message_id()
        # main_block()
        # single_block()
        expirimental_block()
