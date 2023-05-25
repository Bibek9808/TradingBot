from backtesting.lib import crossover
from backtesting import Backtest, Strategy
from datetime import datetime, timedelta

from backtesting.test import SMA, GOOG
class OurStrategy(Strategy):
    def init(self):
        self.range_high = None
        self.range_low = None
        self.retest_candle = None
        self.is_range_broken = False

    def next(self):
        pass