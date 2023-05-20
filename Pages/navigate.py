import MetaTrader5 as  mt5
import pandas as pd
import pytz
from datetime import datetime


def SetTimeZone():
    # set time zone to UTC
    timezone = pytz.timezone("US/Eastern") 
 # Define the timezone for UTC-4 (Eastern Daylight Time)

# Get the current time in UTC-4
    utc_from = datetime(2022, 1, 1, tzinfo=timezone)
    utc_to = datetime(2023, 1, 1, tzinfo=timezone)
    GetRates(utc_from, utc_to)

def GetRates(dateFrom,utcTo):

    #data rates of 15 minutes candle 
    # quarter_mins_rates_frame = 
    #data rates of hourly candle
    hourly_rates = mt5.copy_rates_range("GBPJPY", mt5.TIMEFRAME_H1, dateFrom, utcTo)
    # create DataFrame out of the obtained data
    hourly_rates_frame = pd.DataFrame(hourly_rates)
   # convert time in seconds into the datetime format
    hourly_rates_frame['time']=pd.to_datetime(hourly_rates_frame['time'], unit='s')     
    print("\nDisplay dataframe with data for hourly candle")
    print(hourly_rates_frame.head(24))

    #data rates of 15 minutes candle
    quarter_mins_rates = mt5.copy_rates_range("GBPJPY", mt5.TIMEFRAME_M15, dateFrom, utcTo)
    quarter_mins_rates = pd.DataFrame(quarter_mins_rates)
    quarter_mins_rates['time']=pd.to_datetime(quarter_mins_rates['time'], unit='s')     
    print("\nDisplay dataframe with data for 15 minutes candle")
    print(quarter_mins_rates.head(24))

