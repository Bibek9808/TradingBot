from Constants import messages
from authenticate import connect_to_metatrader

print(messages.welcome_message)

login = input(messages.yesNoDialogueBox)
if(login == "Yes"):
    userName = input(messages.enterLoginName)
    password = input(messages.enterPassword)
    connect_to_metatrader()
else:
    print(messages.byeMessage)
