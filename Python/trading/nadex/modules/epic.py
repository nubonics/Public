"""
# Forex B==aries
import AUD_JPY
import AUD_USD

import EUR_GBP
import EUR_JPY
import EUR_USD

import GBP_JPY
import GBP_USD

import USD_CAD
import USD_CHF
import USD_JPY

# Commodity Binaries
import GOLD
import CRUDE_OIL
import SILVER
"""
import jsonlines
import xml.etree.cElementTree as ET

# LOCAL IMPORTS
from login import login


L = login()

def acquire_epic_url(asset, timeframe):

    if "AUD/JPY" == asset:
        if "10AM-12AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159145"
        if "11AM-1PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159147"
        if "12PM-2PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159149"
        if "1PM-3PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159151"
        if "DAILY-3AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159108"
        if "DAILY-7AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159109"
        if "DAILY-11AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159110"
        if "DAILY-3PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159106"
        if "DAILY-7PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159118"
        if "DAILY-11PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159107"
        if "WEEKLY" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159100"
    if "AUD/USD" == asset:
        if "10AM-12AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158043"
        if "11AM-1PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158044"
        if "12PM-2PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158047"
        if "1PM-3PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158048"
        if "DAILY-3AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159004"
        if "DAILY-7AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159001"
        if "DAILY-11AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159002"
        if "DAILY-3PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158956"
        if "DAILY-7PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159031"
        if "DAILY-11PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159003"
        if "WEEKLY" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158029"
    if "EUR/GBP" == asset:
        if "10AM-12AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159146"
        if "11AM-1PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159148"
        if "12PM-2PM" == timeframe:
            return False
        if "1PM-3PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159152"
        if "DAILY-3AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159105"
        if "DAILY-7AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159103"
        if "DAILY-11AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159104"
        if "DAILY-3PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159101"
        if "DAILY-7PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159117"
        if "DAILY-11PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159102"
        if "WEEKLY" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159098"
    if "EUR/JPY" == asset:
        if "10AM-12AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158328"
        if "11AM-1PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158334"
        if "12PM-2PM" == timeframe:
            return False
        if "1PM-3PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158340"
        if "2PM-4PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159311"
        if "8PM-10PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159299"
        if "9PM-11PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159300"
        if "DAILY-3AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158998"
        if "DAILY-7AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158999"
        if "DAILY-11AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159000"
        if "DAILY-3PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158961"
        if "DAILY-7PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159030"
        if "DAILY-11PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158997"
        if "WEEKLY" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158285"
    if "EUR/USD" == asset:
        if "10AM-12AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/157893"
        if "11AM-1PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/157932"
        if "12PM-2PM" == timeframe:
            return False
        if "1PM-3PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/157987"
        if "2PM-4PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159153"
        if "3PM-5PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159155"
        if "8PM-10PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159115"
        if "9PM-11PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159119"
        if "DAILY-3AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159024"
        if "DAILY-7AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159021"
        if "DAILY-11AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159022"
        if "DAILY-3PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158969"
        if "DAILY-7PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159036"
        if "DAILY-11PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159023"
        if "WEEKLY" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/157267"
    if "GBP/JPY" == asset:
        if "10AM-12AM" == timeframe:
            return False
        if "11AM-1PM" == timeframe:
            return False
        if "12PM-2PM" == timeframe:
            return False
        if "1PM-3PM" == timeframe:
            return False
        if "2PM-4PM" == timeframe:
            return False
        if "3PM-5PM" == timeframe:
            return False
        if "8PM-10PM" == timeframe:
            return False
        if "9PM-11PM" == timeframe:
            return False
        if "DAILY-3AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159010"
        if "DAILY-7AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159011"
        if "DAILY-11AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159012"
        if "DAILY-3PM" == timeframe:
            return False
        if "DAILY-7PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159032"
        if "DAILY-11PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159009"
        if "WEEKLY" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158283"
    if "GBP/USD" == asset:
        if "10AM-12AM" == timeframe:
            return False
        if "11AM-1PM" == timeframe:
            return False
        if "12PM-2PM" == timeframe:
            return False
        if "1PM-3PM" == timeframe:
            return False
        if "2PM-4PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159258"
        if "3PM-5PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159260"
        if "8PM-10PM" == timeframe:
            return False
        if "9PM-11PM" == timeframe:
            return False
        if "DAILY-3AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159026"
        if "DAILY-7AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159027"
        if "DAILY-11AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159028"
        if "DAILY-3PM" == timeframe:
            return False
        if "DAILY-7PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159033"
        if "DAILY-11PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159025"
        if "WEEKLY" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/157281"
    if "USD/CAD" == asset:
        if "10AM-12AM" == timeframe:
            return False
        if "11AM-1PM" == timeframe:
            return False
        if "12PM-2PM" == timeframe:
            return False
        if "1PM-3PM" == timeframe:
            return False
        if "2PM-4PM" == timeframe:
            return False
        if "3PM-5PM" == timeframe:
            return False
        if "8PM-10PM" == timeframe:
            return False
        if "9PM-11PM" == timeframe:
            return False
        if "DAILY-3AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159008"
        if "DAILY-7AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159005"
        if "DAILY-11AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159006"
        if "DAILY-3PM" == timeframe:
            return False
        if "DAILY-7PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159029"
        if "DAILY-11PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159007"
        if "WEEKLY" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/157261"
    if "USD/CHF" == asset:
        if "10AM-12AM" == timeframe:
            return False
        if "11AM-1PM" == timeframe:
            return False
        if "12PM-2PM" == timeframe:
            return False
        if "1PM-3PM" == timeframe:
            return false
        if "2PM-4PM" == timeframe:
            return False
        if "3PM-5PM" == timeframe:
            return False
        if "8PM-10PM" == timeframe:
            return False
        if "9PM-11PM" == timeframe:
            return False
        if "DAILY-3AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159020"
        if "DAILY-7AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159017"
        if "DAILY-11AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159018"
        if "DAILY-3PM" == timeframe:
            return False
        if "DAILY-7PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159034"
        if "DAILY-11PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159019"
        if "WEEKLY" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/157275"
    if "USD/JPY" == asset:
        if "10AM-12AM" == timeframe:
            return False
        if "11AM-1PM" == timeframe:
            return False
        if "12PM-2PM" == timeframe:
            return False
        if "1PM-3PM" == timeframe:
            return False
        if "2PM-4PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159154"
        if "3PM-5PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159156"
        if "8PM-10PM" == timeframe:
            return False
        if "9PM-11PM" == timeframe:
            return False
        if "DAILY-3AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159016"
        if "DAILY-7AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159013"
        if "DAILY-11AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159014"
        if "DAILY-3PM" == timeframe:
            return False
        if "DAILY-7PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159035"
        if "DAILY-11PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/159015"
        if "WEEKLY" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/157277"
    if "GOLD" == asset:
        if "10AM-12AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/157879"
        if "11AM-1PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/157919"
        if "12PM-2PM" == timeframe:
            return False
        if "1PM-3PM" == timeframe:
            return False
        if "2PM-4PM" == timeframe:
            return False
        if "3PM-5PM" == timeframe:
            return False
        if "8PM-10PM" == timeframe:
            return False
        if "9PM-11PM" == timeframe:
            return False
        if "DAILY-3AM" == timeframe:
            return False
        if "DAILY-7AM" == timeframe:
            return False
        if "DAILY-11AM" == timeframe:
            return False
        if "DAILY-1:30PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158968"
        if "DAILY-3PM" == timeframe:
            return False
        if "DAILY-7PM" == timeframe:
            return False
        if "DAILY-11PM" == timeframe:
            return False
        if "WEEKLY" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/157283"
    if "CRUDE OIL" == asset:
        if "9AM-11AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/157836"
        if "10AM-12AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/157878"
        if "11AM-1PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/157917"
        if "12PM-2PM" == timeframe:
            return False
        if "1PM-3PM" == timeframe:
            return False
        if "2PM-4PM" == timeframe:
            return False
        if "3PM-5PM" == timeframe:
            return False
        if "8PM-10PM" == timeframe:
            return False
        if "9PM-11PM" == timeframe:
            return False
        if "DAILY-3AM" == timeframe:
            return False
        if "DAILY-7AM" == timeframe:
            return False
        if "DAILY-11AM" == timeframe:
            return False
        if "DAILY-2:30PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158965"
        if "DAILY-3PM" == timeframe:
            return False
        if "DAILY-7PM" == timeframe:
            return False
        if "DAILY-11PM" == timeframe:
            return False
        if "WEEKLY" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/157256"
    if "SILVER" == asset:
        if "9AM-11AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/157841"
        if "10AM-12AM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/157880"
        if "11AM-1PM" == timeframe:
            return False
        if "12PM-2PM" == timeframe:
            return False
        if "1PM-3PM" == timeframe:
            return False
        if "2PM-4PM" == timeframe:
            return False
        if "3PM-5PM" == timeframe:
            return False
        if "8PM-10PM" == timeframe:
            return False
        if "9PM-11PM" == timeframe:
            return False
        if "DAILY-3AM" == timeframe:
            return False
        if "DAILY-7AM" == timeframe:
            return False
        if "DAILY-11AM" == timeframe:
            return False
        if "DAILY-1:25PM" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/158967"
        if "DAILY-3PM" == timeframe:
            return False
        if "DAILY-7PM" == timeframe:
            return False
        if "DAILY-11PM" == timeframe:
            return False
        if "WEEKLY" == timeframe:
            return "https://trade.nadex.com/iDeal/markets/navigation/157273"

def acquire_epic(asset, timeframe, strike):
    """ Acquire the epic from the provided url based upon the Asset & Timeframe provided """
    # Go to the url
    data = L.get(acquire_epic_url(asset, timeframe)).json()

    length = len(data['markets'])


    my_dict = dict()

    for strikes in range(length):
        data['markets'][strikes]
        raw_strike_price = data['markets'][strikes]['instrumentName']
        epic = data['markets'][strikes]['epic']
        strike_price = raw_strike_price.split('>')[1].split(' ')[0]

        if strike == strike_price:
            print(strike_price, epic)
            return epic

    """
    with jsonlines.open('epic.json', 'w') as writer:
        writer.write(data)
    """

if __name__ == "__main__":
    acquire_epic(asset, timeframe, strike)
