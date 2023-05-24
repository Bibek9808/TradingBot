import MetaTrader5 as  mt5
import pandas as pd
import pytz
from datetime import datetime
import json

from backtesting import Strategy, Backtest

from BackTesting.strategyOne import StrategyOneBackTesting

with open('botSettings.json') as config_file:
    config = json.load(config_file)

dateFrom = config['utc_from']
dateTo = config['utc_to']    

def SetTimeZone():
    # set time zone to UTC
    timezone = pytz.timezone("US/Eastern") 
 # Define the timezone for UTC-4 (Eastern Daylight Time)

# Get the current time in UTC-4
    # Convert dateFrom and dateTo to UTC timestamps
    utc_from = timezone.localize(datetime(*dateFrom)).astimezone(pytz.utc)
    utc_to = timezone.localize(datetime(*dateTo)).astimezone(pytz.utc)

    # # Convert UTC timestamps to integers
    timestamp_from = int(utc_from.timestamp())
    timestamp_to = int(utc_to.timestamp())
    dataForBackTesting = GetRates(timestamp_from, timestamp_to)
    # Access the first and second index values
    hourlyValue = dataForBackTesting[0]
    quarterminsValue = dataForBackTesting[1]    
    strategy = StrategyOneBackTesting(hourlyValue, quarterminsValue)

def GetRates(dateFrom,utcTo):

    hourly_rates = mt5.copy_rates_range("GBPJPY", mt5.TIMEFRAME_H1, dateFrom, utcTo)
    # create DataFrame out of the obtained data
    hourly_rates_frame = pd.DataFrame(hourly_rates)
   # convert time in seconds into the datetime format
    hourly_rates_frame['time']=pd.to_datetime(hourly_rates_frame['time'], unit='s')     
    print("\nDisplay dataframe with data for hourly candle")
    print(hourly_rates_frame)


    #data rates of 15 minutes candle
    quarter_mins_rates = mt5.copy_rates_range("GBPJPY", mt5.TIMEFRAME_M15, dateFrom, utcTo)
    quarter_mins_rates = pd.DataFrame(quarter_mins_rates)
    quarter_mins_rates['time']=pd.to_datetime(quarter_mins_rates['time'], unit='s')     
    print("\nDisplay dataframe with data for 15 minutes candle")
    print(quarter_mins_rates)

    return (hourly_rates_frame, quarter_mins_rates)

