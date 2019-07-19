import jsonlines

# LOCAL IMPORTS
from login import login


def update_x_security_token():
    
    L = login()

    new_token = L.cookies['X-SECURITY-TOKEN']

    updated_values = dict()

    with jsonlines.open(r'C:\Users\Nubonix\pyscripts3\trading\nadex\Assets\nadex_credentials.json','r') as reader:
        for obj in reader:
            username = obj['username']
            password = obj['password']
            x_security_token = obj['x-security-token']

    updated_values['username'] = username
    updated_values['password'] = password
    updated_values['x-security-token'] = new_token

    print(updated_values['x-security-token'])

    with jsonlines.open(r'C:\Users\Nubonix\pyscripts3\trading\nadex\Assets\nadex_credentials.json','w') as writer:
        print('Obtaining a new X-SECURITY-TOKEN...')
        writer.write(updated_values)

   
if __name__ == "__main__":
    update_x_security_token()
