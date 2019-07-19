import jsonlines
from telethon import TelegramClient


def load_credentials():
    with jsonlines.open(r'C:\Users\Nubonix\pyscripts3\trading\nadex\Assets\telegram_api_credentials.json', 'r') as reader:
        for obj in reader:
            return obj['api_id'], obj['api_hash']

api_id = load_credentials()[0]
api_hash = load_credentials()[1]

client = TelegramClient('autotradingaccount', api_id, api_hash)
client.start()

print(client)

dialogs = client.get_dialogs(name="AutoTrading")
print(client.get_messages())
"""
def part1():
    while True:
        try:
            for dialog in dialogs:

                if dialog.name == "AutoTrade":
                    msg = str(dialog.message.message)
                    print(msg)

                else:
                    continue
        except KeyboardInterrupt:
            break
                    
if __name__ == "__main__":
    part1()
"""