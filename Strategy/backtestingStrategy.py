from backtesting import Backtest, Strategy
from backtesting.lib import resample_apply

class RsiOcillator(Strategy):
    def init(self):
        # return super().init()
        self.range_high = None
        self.range_low = None
        self.retest_candle = None
        self.is_range_broken = False
        pass
    def next(self):
        # return super().next()
        pass



