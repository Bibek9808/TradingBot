import MetaTrader5 as  mt5
import pandas as pd
import pytz
from datetime import datetime


def SetTimeZone():
    # set time zone to UTC
    timezone = pytz.timezone("US/Eastern") 
 # Define the timezone for UTC-4 (Eastern Daylight Time)

# Get the current time in UTC-4
    utc_from = datetime(2023, 5, 10, tzinfo=timezone)
    utc_to = datetime(2023, 5, 19, tzinfo=timezone)
    GetRates(utc_from, utc_to)

def GetRates(dateFrom,utcTo):
    rates = mt5.copy_rates_range("GBPJPY", mt5.TIMEFRAME_D1, dateFrom, utcTo) 
    # create DataFrame out of the obtained data
    rates_frame = pd.DataFrame(rates)
   # convert time in seconds into the datetime format
    rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')     
    # display data
    print("\nDisplay dataframe with data")
    print(rates_frame.head(24))      
