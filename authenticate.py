import MetaTrader5 as  mt5
from Constants import messages
from Pages import navigate

def connect_to_metatrader(account, password):
    mt5.initialize()
    server="MetaQuotes-Demo"
# Login to the MT5 account

    # Enter your login and password . Server remains the same
    authorized = mt5.login(login=5013417401, server=server, password="hsiar5is")

    if authorized:
        print(messages.demoAccountConnect)
        account_info = mt5.account_info()
        print(account_info)
        navigate.SetTimeZone()


    elif not mt5.initialize():
            print(messages.demoAccountFailed,mt5.last_error())
            quit()         
    else:
        print(messages.demoAccountFailed)