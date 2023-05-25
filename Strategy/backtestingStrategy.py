from backtesting import Backtest, Strategy
from backtesting.lib import resample_apply
import pandas_ta as pa
import pytz
from Pages import navigate
from datetime import datetime
from Pages.navigate import GetRatesHourly, GetDataForBackTesting
date_From = datetime(2021,1,1)
utc_To = datetime(2022,1,1)
candle_Information = GetRatesHourly(dateFrom=date_From, utcTo= utc_To)
time = candle_Information['time']
high = candle_Information['high']
close = candle_Information['close']
low = candle_Information['low']
class OneHourConditions(Strategy):
    def init(self,time,high,close,low):
        if time[0].strftime("%H:%M") == "01:00":
                self.firstHigh = high[0]
                self.firstLow = low[0]
        
        if time[1].strtime("%H:%M") == "02:00":
             self.secondHigh = high[1]
             self.secondLow = low[1]
        self.daily_Range_High = max(self.firstHigh,self.secondHigh )
        self.daily_Range_Low = min(self.firstLow,self.secondLow)
    def next(self):
        # return super().next()
        if close[-1]>self.daily_Range_High:
             return True
        elif close[-1] < self.daily_Range_Low:
            return True 
        pass



