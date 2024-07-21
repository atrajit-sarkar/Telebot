from PIL import Image
import telebot
import os
import time
from requests.exceptions import ConnectionError
from Atrmaths import TELEBOT_API

dir=os.getcwd()
bot=telebot.TeleBot(TELEBOT_API.READ_API())

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,"Upload your photo in file format to get started.....")

@bot.message_handler(content_types=['document'])
def handle_docs_photos(message):
    bot.reply_to(message,"Please wait while processing........")
    try:
        # For documents
        
        
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        global original_file_name
        original_file_name = message.document.file_name
        with open(f"{dir}/{original_file_name}", 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message,"what you wanna do? /resize,/compress")
    except:
        bot.reply_to(message,"It seems it is not a photo....")
@bot.message_handler(commands=['resize'])
def resize(message):
    bot.reply_to(message,"Enter your Width and Heigth respectively:(eg. 640 360)")
    bot.register_next_step_handler(message,resizephoto)
def resizephoto(message):
    dimension=message.text.split(" ")
    W=int(dimension[0])
    H=int(dimension[1])
    new_size = (W, H)
    try:
        with Image.open(f"{dir}/{original_file_name}") as img:
        # The new size (width, height)
        # Resize the image
            resized_img = img.resize(new_size)

        # Save the resized image
        resized_img.save(f"{dir}/{original_file_name}")
        with open(f"{dir}/{original_file_name}","rb") as f:
            bot.send_document(message.chat.id,f)
    except:
        bot.reply_to(message,"Photo can't be resized.")
    time.sleep(0.01)
    os.remove(f"{dir}/{original_file_name}")    

@bot.message_handler(commands=['compress'])
def com(message):
    bot.reply_to(message,"Enter your image quality in percentage(e.g. 85)")
    bot.register_next_step_handler(message,compress)
def compress(message):
    quality=int(message.text)
    try:
        with Image.open(f"{dir}/{original_file_name}") as img:
    # The output quality (1-95), lower might reduce file size
    # Save the image with reduced quality
            img.save(f"{dir}/{original_file_name}",quality=quality)

        with open(f"{dir}/{original_file_name}","rb") as f:
            bot.send_document(message.chat.id,f)
        
    except:
        bot.reply_to(message,"Image can't be compressed....")
    time.sleep(0.01)
    os.remove(f"{dir}/{original_file_name}")

print("BOT STARTED.....")
while True:
    try:
        bot.polling(none_stop=True)
    except ConnectionError as e:
        print(f"Connection error: {e}. Retrying...")
        # Implement your retry logic here or just pass to retry on the next loop iteration
    except Exception as e:
        print(f"An unexpected error occurred: {e}")