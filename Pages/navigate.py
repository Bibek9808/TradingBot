import MetaTrader5 as  mt5
import pandas as pd
import pytz
from datetime import datetime

def SetTimeZone():
    # set time zone to UTC
    timezone = pytz.timezone("Etc/UTC")
    # create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
    utc_from = datetime(2020, 1, 10, tzinfo=timezone)
