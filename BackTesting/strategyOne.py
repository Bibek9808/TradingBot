from backtesting import Strategy, Backtest

class StrategyOneBackTesting(Strategy, Backtest):
    # def __init__(self, hourly_rates_frame, quarter_mins_rates):
    #     super().__init__()
    #     self.hourly_rates_frame = hourly_rates_frame
    #     self.quarter_mins_rates = quarter_mins_rates
    def init(self):
        self.range_high = None
        self.range_low = None
        self.retest_candle = None
        self.is_range_broken = False
        pass        

    def next(self):
        # Implement your trading strategy logic here
        # You can access the hourly_rates_frame and quarter_mins_rates variables within this method

        # Example usage:
        # Accessing the 'time' column of hourly_rates_frame
        hourly_times = self.hourly_rates_frame['time']
        
        # Accessing the 'time' column of quarter_mins_rates
        quarter_mins_times = self.quarter_mins_rates['time']

        # Rest of your strategy implementation

# Create an instance of the StrategyOneBackTesting class and pass the required variables
# strategy = StrategyOneBackTesting("hourly_rates_frame", "quarter_mins_rates")

# Run the backtest using the strategy
# backtest = Backtest(...)
# results = backtest.run(strategy)
