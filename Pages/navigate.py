import MetaTrader5 as  mt5
import pandas as pd
import pytz
from datetime import datetime
import json
from backtesting import Backtest, Strategy
from backtesting.lib import resample_apply

# from TestingStrategy.backtestingStrategy import StrategyOne
from TestingStrategy.backtestingStrategy import MyStrategy



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

    quarter_mins_data = pd.DataFrame(GetRatesQuarterMins(timestamp_from,timestamp_to))
    quarter_mins_data['open'] = pd.to_numeric(quarter_mins_data['open'], errors='coerce')

    # quarter_mins_data['open'] = pd.to_numeric()
    quarter_mins_data['time']=pd.to_datetime(quarter_mins_data['time'], unit='s')       

    return quarter_mins_data

def StartBackTesting(quarterMinsData):
    # Print the provided 15-minute data
    print(quarterMinsData)
    print(type(quarterMinsData))
    # strategy = MyStrategy(broker= any,data= quarterMinsData, params=any)
    # strategy_params = {
    #     'broker': 'MetaQuotes-Demo',
    #     'data': quarterMinsData,
    #     'params': {}
    # }
    # strategy = MyStrategy(**strategy_params)
    
    # Now you can use the 'strategy' instance to run your backtest or perform other actions
    # For example, you can create a Backtest instance and run it using the 'strategy'
    
    # Define column names
    columns = ['time','open', 'high', 'low', 'close', 'tick_volume']
    # Convert quarterMinsData to pandas DataFrame
    df = pd.DataFrame(quarterMinsData, columns=columns)
    #mapping the dataframe
    # to do add time to the mapping as well 
    df = df.rename(columns={
                                'open': 'Open', 
                                'high': 'High', 
                                'low': 'Low', 
                                'close': 'Close', 
                                'tick_volume': 'Volume'
                            })
    bt = Backtest(data = df, strategy= MyStrategy)
    result = bt.run()
    
    # Print the results
    print(result)      
    

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
    selected_columns_quarter_mins_rates = quarter_mins_rates[['time', 'open', 'high', 'low','close','tick_volume']]
    return selected_columns_quarter_mins_rates



