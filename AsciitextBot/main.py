import pyfiglet
import telebot
from Atr.Telebot import TELEBOT_API



bot=telebot.TeleBot(TELEBOT_API.READ_API('@AsciiTextBot'))

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,"Please Enter your text to transform")
    bot.register_next_step_handler(message,convert)
def convert(message):
    text=message.text
    try:
        text=pyfiglet.figlet_format(text)
        bot.send_message(message.chat.id,text)
    except:
        bot.reply_to(message,"Please enter valid text.")
print("Bot running......")

# while True:
#     try:
#         bot.polling()
#     except Exception as e:
#         print(e)
#         break
bot.polling()