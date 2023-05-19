import MetaTrader5 as  mt5
import pandas as pd
import pytz
from datetime import datetime


def SetTimeZone():
    # set time zone to UTC
    timezone = pytz.timezone("Etc/UTC")
    # create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
    utc_from = datetime(2020, 1, 10, tzinfo=timezone)
    GetRates(utc_from)
   # get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone

def GetRates(dateFrom):
    rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_H4, dateFrom, 10)  
    # create DataFrame out of the obtained data
    rates_frame = pd.DataFrame(rates)
   # convert time in seconds into the datetime format
    rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')     
    # display data
    print("\nDisplay dataframe with data")
    print(rates_frame)      
