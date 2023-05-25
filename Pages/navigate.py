import MetaTrader5 as  mt5
import pandas as pd
import pytz
from datetime import datetime
import json
from backtesting import Backtest, Strategy
from backtesting.lib import resample_apply

# from TestingStrategy.backtestingStrategy import StrategyOne



with open('botSettings.json') as config_file:
    config = json.load(config_file)

dateFrom = config['utc_from']
dateTo = config['utc_to']    

def GetDataForBackTesting():
    #Set Timezone
    timezone = pytz.timezone("US/Eastern") 
    utc_from = timezone.localize(datetime(*dateFrom)).astimezone(pytz.utc)
    utc_to = timezone.localize(datetime(*dateTo)).astimezone(pytz.utc)

    timestamp_from = int(utc_from.timestamp())
    timestamp_to = int(utc_to.timestamp())

    hourly_data = pd.DataFrame(GetRatesHourly(timestamp_from,timestamp_to))
    hourly_data['time']=pd.to_datetime(hourly_data['time'], unit='s')     

    quarter_mins_data = pd.DataFrame(GetRatesQuarterMins(timestamp_from,timestamp_to))
    quarter_mins_data['time']=pd.to_datetime(quarter_mins_data['time'], unit='s')       

    return hourly_data, quarter_mins_data

def StartBackTesting(hourlyData, quarterMinsData):
    print("\nDisplay dataframe with data for hourly candle")
    print(hourlyData)

    print("\nDisplay dataframe with data for 15 minutes candle")
    print(quarterMinsData)
    #connect the strategy class here
    # strategy = StrategyOne(hourlyData, quarterMinsData)
    

def GetRatesHourly(dateFrom,utcTo):
    hourly_rates = mt5.copy_rates_range("GBPJPY", mt5.TIMEFRAME_H1, dateFrom, utcTo)
    hourly_rates_frame = pd.DataFrame(hourly_rates)
    hourly_rates_frame['time']=pd.to_datetime(hourly_rates_frame['time'], unit='s')     
    #data preparation
    selected_columns_hourly_rates_frame = hourly_rates_frame[['time', 'open', 'high', 'low', 'tick_volume']]
    return selected_columns_hourly_rates_frame


def GetRatesQuarterMins(dateFrom,utcTo):
    #data rates of 15 minutes candle
    quarter_mins_rates = mt5.copy_rates_range("GBPJPY", mt5.TIMEFRAME_M15, dateFrom, utcTo)
    quarter_mins_rates = pd.DataFrame(quarter_mins_rates)
    quarter_mins_rates['time']=pd.to_datetime(quarter_mins_rates['time'], unit='s')     
    print("\nDisplay dataframe with data for 15 minutes candle")
    selected_columns_quarter_mins_rates = quarter_mins_rates[['time', 'open', 'high', 'low', 'tick_volume']]
    return selected_columns_quarter_mins_rates



