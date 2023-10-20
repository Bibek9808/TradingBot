from backtesting import Backtest, Strategy
from backtesting.lib import resample_apply
import pandas as pd

class MyStrategy(Strategy):
    def init(self):
        super().init()     
        fifteenMinutesCandle = self.data.df
        # Resample 15-minute data into 1-hour candles with OHLC aggregation
        # mapping ohlc dictiionary as well
        ohlc_dict = {
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last',
            'volume': 'sum',
        }       
        fifteenMinutesCandle = fifteenMinutesCandle.rename(columns={
                                    'Open': 'open', 
                                    'High': 'high', 
                                    'Low': 'low', 
                                    'Close': 'close',
                                    'Volume': 'volume' 
                                })        
        
        # time as index conversion before applying the resample 
        fifteenMinutesCandle.set_index('time', inplace=True)
        self.resampled_data = fifteenMinutesCandle.resample('1H').apply(ohlc_dict)       
    
    def next(self):
        print("Data Ready for Adding the candle logic-- 1 hour candle")
        self.resampled_times = self.resampled_data.index
        oneHrResampledData = pd.to_datetime(self.resampled_times[0])
        resampled_time = oneHrResampledData.time()
        if resampled_time == pd.to_datetime('01:00:00').time():
            print("VAyooo")
        # print("--------------------------------------------------------------------")
        
        
        print("Data ready for testing: 15 mins candle")
        # print(self.data.df)
        #// Important Code hidden cause of Privacy