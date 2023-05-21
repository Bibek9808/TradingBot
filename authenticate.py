import MetaTrader5 as  mt5
from Constants import messages
from Pages import navigate
import json

# Load the configuration from the file
with open('botSettings.json') as config_file:
    config = json.load(config_file)

# Access the configuration values
id = config['login']
login_password = config['password']
server = config['server']    

def connect_to_metatrader():
    mt5.initialize()
    authorized = mt5.login(login=id, server=server, password=login_password)    

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