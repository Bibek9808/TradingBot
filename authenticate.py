import MetaTrader5 as  mt5
from Constants import messages

def connect_to_metatrader(account, password):
    mt5.initialize()
    server="MetaQuotes-Demo"
# Login to the MT5 account

    # Enter your login and password . Server remains the same
    authorized = mt5.login(login=5013417413, server=server, password="hsiaasdar5is")

    if authorized:
        print(messages.demoAccountConnect)
        
    else:
        print(messages.demoAccountFailed)