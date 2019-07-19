# LOCAL IMPORTS
from login import login


def working_orders():
    ''' Acquire the deal_id\'s for all of the working orders on the account. '''

    L = login()

    url = 'https://trade.nadex.com//dealing/pd/cfd/index.htm'

    wo = set()

    response = L.get(url)

    content = response.content

    tree = html.fromstring(str(content))

    for working_orders in tree.xpath('//*[@class="ctrCell cellHide"]'):
        # Simply parse out the date/times the working orders were created, as they are not needed...
        if ' ' not in working_orders.text:
            wo.add(working_orders.text)

    return wo


if __name__ == "__main__":
    working_order()