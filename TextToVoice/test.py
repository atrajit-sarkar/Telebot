from text_to_speech import audio_converter
import telebot
import os
import time
from Atrmaths import TELEBOT_API

bot=telebot.TeleBot(TELEBOT_API.READ_API('@TTVCvnwjvhwvbceyBot'))

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,'''Enter your text,lang,tld,filename of output audio to convert it into audio file.......(.mp3 format)
example: Hi,how are you?$en$co.in$audio
language referrence:https://shorturl.at/bfJNO
top level domain referrence:https://shorturl.at/bfJNO ''')
    bot.register_next_step_handler(message,audio)
def audio(message):
    p_data=message.text.split('$')
    # print(p_data)
    try:
        if len(p_data)==1:
            audio_file=audio_converter(p_data[0],"en","co.in","audio")
        else:
            audio_file=audio_converter(p_data[0],p_data[1],p_data[2],p_data[3])
        bot.send_message(message.chat.id,"Please Wait while processing.......")
        try:
            with open(audio_file,"rb") as f:
                bot.send_document(message.chat.id,f)
            bot.reply_to(message,"Your audio created successfully... Enjoy.....")
        except:
            bot.send_message(message.chat.id,"Sorry for inconvenience.We are facing problems sending audio file right now.... Please try again /start")
    except:
        bot.reply_to(message,"Please see the example given and type in corrected format and try again........./start")
    time.sleep(0.01)
    for i in os.listdir(os.getcwd()):
        if i.endswith(".mp3"):
            os.remove(f"{os.getcwd()}/{i}")
print("Bot started......")
# while True:
#     try:
#         bot.polling()
#     except:
#         print("")
bot.polling()