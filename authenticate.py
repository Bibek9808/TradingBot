import MetaTrader5 as  mt5
from Constants import messages

def connect_to_metatrader(account, password):
    mt5.initialize()
    server="MetaQuotes-Demo"
# Login to the MT5 account

    # Enter your login and password . Server remains the same
    authorized = mt5.login(login=501341741201, server=server, password="hsiar5isasd")

    if authorized:
        print(messages.demoAccountConnect)
        account_info = mt5.account_info()
        print(account_info)
    elif not mt5.initialize():
            print(messages.demoAccountFailed,mt5.last_error())
            quit()         
    else:
        print(messages.demoAccountFailed)