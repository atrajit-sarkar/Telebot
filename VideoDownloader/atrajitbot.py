import telebot

bot=telebot.TeleBot("")
bot=telebot.TeleBot("") #Use your API token Here

@bot.message_handler(commands=['start'])
def start(message):
  bot.reply_to(message,"Hello Sir, use /send command to get an image.")
print("Bot started")

@bot.message_handler(commands=["send"])
def send_files(message):
    # deleteWebhook
    # updates=bot.get_updates()
    
    chat_id= message.chat.id
    with open(r"some_file.txt", "rb") as f:
        bot.send_document(chat_id, f)
bot.polling(long_polling_timeout=3600)
