import telebot
import time
from Atrmaths import TELEBOT_API


bot=telebot.TeleBot(TELEBOT_API.READ_API())

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,"Please enable notification services as given in the menu.")
@bot.message_handler(commands=['drinkingWater'])
def drinkingwater(message):
    bot.send_message(message.chat.id,"Want to enable or disable?")
    bot.register_next_step_handler(message,drinkwater)
def drinkwater(message):
    consent=message.text
    if consent=="enable":
        while True:
            bot.send_message(message.chat.id,"hwgdshhcchdbhdcbdhcb")
            break
print("Bot started......")    
bot.polling()        
# while True:
    # bot.polling()
