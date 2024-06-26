import telebot
#import openai
# from config import *
#from replit import db

#db["hello"]="hello"
#print(db["hello"])


bot=telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def start(message):
  bot.reply_to(message,'''Tell me what you want to ask:
               1. /rsh : To know how to reverse shell
               2. /ccna : To know contents of CCNA
               ''')
print("Bot started")

@bot.message_handler(commands=['link'])
def output(message):
  bot.reply_to(message,"ye le banchod!")

@bot.message_handler(commands=['ccna'])
def output(message):
  bot.reply_to(message,'''
1. /day01
2. /day02
''')

@bot.message_handler(commands=['rsh'])
def rsh(message):
    chat_id=message.chat.id
    with open(r"D:\downloads\HackingTools\reverseshell.md", 'rb') as f:
      bot.send_document(chat_id,f)
    bot.reply_to(message,"Do you Want to see the contents:(/rshY or /rshN) ")
@bot.message_handler(commands=['rshY'])
def rshYes(message):
  with open(r"D:\downloads\HackingTools\reverseshell.md", 'r') as f:
    content=f.read()
  bot.reply_to(message,content)
  
@bot.message_handler(commands=['rshN'])
def rshNo(message):
  bot.reply_to(message,"Thanks for using our bot.")
  
      


@bot.message_handler(commands=['day01'])
def rsh(message):
    chat_id=message.chat.id
    with open(r"D:\downloads\CCNA Course\Day01\MacAddressTable.md", 'rb') as f:
        bot.send_document(chat_id,f)
    bot.reply_to(message,"Do you Want to see the contents:(/d01Y or /d01N) ")

@bot.message_handler(commands=['d01Y'])
def d01Y(message):
  with open(r"D:\downloads\CCNA Course\Day01\MacAddressTable.md", 'r') as f:
    content=f.read()
  bot.reply_to(message,content)
  
@bot.message_handler(commands=['d01N'])
def d01N(message):
  bot.reply_to(message,"Thanks for using our bot.")
    



@bot.message_handler(commands=['help'])
def output(message):
  bot.reply_to(message,'''
1./start: Start the bot
2./help : Open this box
3./link : To get our official website

               ''')
bot.polling()
