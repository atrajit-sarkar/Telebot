import telebot
import time
from Atrmaths import TELEBOT_API

from mailtm import Email

def listener(message):
    to=message['to'][0]['address']
    with open("db.txt") as f:
        dblist=f.readlines()
        # print(dblist)
        for i in dblist:
            dblist=i.strip().split(":")
            # print(dblist)
            if dblist[1]==to:
                chatid=dblist[0]
                # print(chatid)
                break
    try:
        bot.send_message(chatid,f"To: {to}")
        bot.send_message(chatid,f"Sent from: Name: {message['from']['name']} \n email: {message['from']['address']}")
        bot.send_message(chatid,"\nSubject: " + message['subject'])
        bot.send_message(chatid,"Content: " + (message['text'] if message['text'] else message['html']))
    except:
        return 0
    
# Main Code Is Here.........................
bot=telebot.TeleBot(TELEBOT_API.READ_API('@TempMail691729Bot'))

@bot.message_handler(commands=['start'])
def start(message):
    # global chatid
    chatid=message.chat.id
    try:
        global test
        test = Email()
        # bot.send_message(message.chat.id,"\nDomain: " + test.domain)
        test.register()  # Make a new email address
        bot.send_message(chatid,"\nEmail Address: " + str(test.address))
        with open("db.txt","a") as f:
              f.write(f"{chatid}:{str(test.address)}\n")
        test.start(listener)
        # bot.register_next_step_handler(message,stop)
    except:
        bot.reply_to(message,"Service unavailable......")
@bot.message_handler(commands=['quite'])
def stop(message):
    bot.reply_to(message,"Which mail id you want to remove: ")
    bot.register_next_step_handler(message,remove)
def remove(message):
    with open("db.txt") as f:
        lines=f.readlines()
    j=0
    try:
        for i in lines:
            if i.rstrip().split(":")[1]==message.text:
                lines.pop(j)
                break
            else:
                j=j+1
        else:
            bot.reply_to(message,"Enter correct email id that you registered...")
        with open("db.txt","w") as f:
            f.writelines(lines)
    except:
        bot.reply_to(message,"Something went wrong.... Please try again.")
    bot.reply_to(message,"Temp Mail stopped listenning..../start to get a new one...")
    # test.stop()
    bot.stop_polling()
    # bot.reset_data()
    time.sleep(0.01)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'''
1. /start: You can take any number of email id by repeatedly pressing /start . But remember you can't then delete the previous ones. You only can delete the recent email id.
2. /quite: It is will delete only the recent email id.
''')

print("bot started......")
# while True:
#     try:
#         bot.polling()
#     except:
#         print("")
bot.polling()



