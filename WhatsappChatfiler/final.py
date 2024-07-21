import telebot
import zipfile
import os
import time
import shutil
from requests.exceptions import ConnectionError
from Atr.Telebot import TELEBOT_API

dir=r"/home/ec2-user/WhatsappChatfilter/byebye"
# dir=r"D:\downloads\Python\Projects\Telebot\WhatsappChatfiler\byebye"
def checkfileEXT(dir,ext):
    for i in dir:
        if i.endswith(ext):
            return 1
    return 0



bot = telebot.TeleBot(TELEBOT_API.READ_API())
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,"Bot started and server side set up done. Now, send your zip file to filter it out..")
    if not os.path.exists(dir):
        os.mkdir(dir)

@bot.message_handler(content_types=['document', 'photo'])
def handle_docs_photos(message):
    bot.reply_to(message,"Please Wait while saving to server......")
    try:
        # For documents
        file_info = bot.get_file(message.document.file_id)
        # For photos, use message.photo[-1].file_id to get the highest quality
        # file_info = bot.get_file(message.photo[-1].file_id)

        downloaded_file = bot.download_file(file_info.file_path)
        global original_file_name
        original_file_name = message.document.file_name
        with open(f"{dir}/{original_file_name}", 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(message, "File has been saved successfully.")
        bot.reply_to(message, '''What you want to filter out :
                     1. /jpg
                     2. /png
                     3. /txt
                     4. /mp4
                     5. /mp3
                     6. /opus
                     7. /webp
                     8. /allfiles''')
        # bot.register_next_step_handler(message,goto)
    except:
        bot.reply_to(message, "Please /start the bot again......")
@bot.message_handler(commands=['opus'])
def opusfilter(message):
    bot.reply_to(message,"Please wait while filtering out........")
    try:
        with zipfile.ZipFile(f"{dir}/{original_file_name}", 'r') as zip_ref:
            os.mkdir(f"{dir}/extracted")
            zip_ref.extractall(f"{dir}/extracted")
        time.sleep(0.01)

        files=os.listdir(f"{dir}/extracted")
        for i in files:
            if i.endswith(".opus"):
                with open(f"{dir}/extracted/{i}","rb") as f:
                    bot.send_document(message.chat.id,f)

        if checkfileEXT(files,".opus")==1:
            bot.reply_to(message,"These are all .opus files.....")
        else:
            bot.reply_to(message,"There are no opus file......")
    except:
        bot.reply_to(message,"Send non-corrupted zip file.....")

    time.sleep(0.01)
    for i in dir:
        if os.path.isdir(f"{dir}/{i}"):
            shutil.rmtree(f"{dir}/{i}")
    bot.send_message(message.chat.id,"Server Cleaned Successfully for privacy and storage reasons.Please send another zip or the same zip to filterout more fileformats.....Thank you......")



@bot.message_handler(commands=['webp'])
def opusfilter(message):
    bot.reply_to(message,"Please wait while filtering out........")
    try:
        with zipfile.ZipFile(f"{dir}/{original_file_name}", 'r') as zip_ref:
            os.mkdir(f"{dir}/extracted")
            zip_ref.extractall(f"{dir}/extracted")
        time.sleep(0.01)

        files=os.listdir(f"{dir}/extracted")
        for i in files:
            if i.endswith(".webp"):
                with open(f"{dir}/extracted/{i}","rb") as f:
                    bot.send_document(message.chat.id,f)

        if checkfileEXT(files,".webp")==1:
            bot.reply_to(message,"These are all .webp files.....")
        else:
            bot.reply_to(message,"There are no webp file......")
    except:
        bot.reply_to(message,"Send non-corrupted zip file.....")

    time.sleep(0.01)
    for i in dir:
        if os.path.isdir(f"{dir}/{i}"):
            shutil.rmtree(f"{dir}/{i}")
    bot.send_message(message.chat.id,"Server Cleaned Successfully for privacy and storage reasons.Please send another zip or the same zip to filterout more fileformats.....Thank you......")


@bot.message_handler(commands=['jpg'])
def opusfilter(message):
    bot.reply_to(message,"Please wait while filtering out........")
    try:
        with zipfile.ZipFile(f"{dir}/{original_file_name}", 'r') as zip_ref:
            os.mkdir(f"{dir}/extracted")
            zip_ref.extractall(f"{dir}/extracted")
        time.sleep(0.01)

        files=os.listdir(f"{dir}/extracted")
        for i in files:
            if i.endswith(".jpg"):
                with open(f"{dir}/extracted/{i}","rb") as f:
                    bot.send_document(message.chat.id,f)

        if checkfileEXT(files,".jpg")==1:
            bot.reply_to(message,"These are all .jpg files.....")
        else:
            bot.reply_to(message,"There are no .jpg file......")
    except:
        bot.reply_to(message,"Send non-corrupted zip file.....")

    time.sleep(0.01)
    for i in dir:
        if os.path.isdir(f"{dir}/{i}"):
            shutil.rmtree(f"{dir}/{i}")
    bot.send_message(message.chat.id,"Server Cleaned Successfully for privacy and storage reasons.Please send another zip or the same zip to filterout more fileformats.....Thank you......")


@bot.message_handler(commands=['png'])
def opusfilter(message):
    bot.reply_to(message,"Please wait while filtering out........")
    try:
        with zipfile.ZipFile(f"{dir}/{original_file_name}", 'r') as zip_ref:
            os.mkdir(f"{dir}/extracted")
            zip_ref.extractall(f"{dir}/extracted")
        time.sleep(0.01)

        files=os.listdir(f"{dir}/extracted")
        for i in files:
            if i.endswith(".png"):
                with open(f"{dir}/extracted/{i}","rb") as f:
                    bot.send_document(message.chat.id,f)

        if checkfileEXT(files,".png")==1:
            bot.reply_to(message,"These are all .png files.....")
        else:
            bot.reply_to(message,"There are no png file......")
    except:
        bot.reply_to(message,"Send non-corrupted zip file.....")

    time.sleep(0.01)
    for i in dir:
        if os.path.isdir(f"{dir}/{i}"):
            shutil.rmtree(f"{dir}/{i}")
    bot.send_message(message.chat.id,"Server Cleaned Successfully for privacy and storage reasons.Please send another zip or the same zip to filterout more fileformats.....Thank you......")


@bot.message_handler(commands=['mp3'])
def opusfilter(message):
    bot.reply_to(message,"Please wait while filtering out........")
    try:
        with zipfile.ZipFile(f"{dir}/{original_file_name}", 'r') as zip_ref:
            os.mkdir(f"{dir}/extracted")
            zip_ref.extractall(f"{dir}/extracted")
        time.sleep(0.01)

        files=os.listdir(f"{dir}/extracted")
        for i in files:
            if i.endswith(".mp3"):
                with open(f"{dir}/extracted/{i}","rb") as f:
                    bot.send_document(message.chat.id,f)

        if checkfileEXT(files,".mp3")==1:
            bot.reply_to(message,"These are all .mp3 files.....")
        else:
            bot.reply_to(message,"There are no mp3 file......")
    except:
        bot.reply_to(message,"Send non-corrupted zip file.....")

    time.sleep(0.01)
    for i in dir:
        if os.path.isdir(f"{dir}/{i}"):
            shutil.rmtree(f"{dir}/{i}")
    bot.send_message(message.chat.id,"Server Cleaned Successfully for privacy and storage reasons.Please send another zip or the same zip to filterout more fileformats.....Thank you......")


@bot.message_handler(commands=['mp4'])
def opusfilter(message):
    bot.reply_to(message,"Please wait while filtering out........")
    try:
        with zipfile.ZipFile(f"{dir}/{original_file_name}", 'r') as zip_ref:
            os.mkdir(f"{dir}/extracted")
            zip_ref.extractall(f"{dir}/extracted")
        time.sleep(0.01)

        files=os.listdir(f"{dir}/extracted")
        for i in files:
            if i.endswith(".mp4"):
                with open(f"{dir}/extracted/{i}","rb") as f:
                    bot.send_document(message.chat.id,f)

        if checkfileEXT(files,".mp4")==1:
            bot.reply_to(message,"These are all .mp4 files.....")
        else:
            bot.reply_to(message,"There are no mp4 file......")
    except:
        bot.reply_to(message,"Send non-corrupted zip file.....")

    time.sleep(0.01)
    for i in dir:
        if os.path.isdir(f"{dir}/{i}"):
            shutil.rmtree(f"{dir}/{i}")
    bot.send_message(message.chat.id,"Server Cleaned Successfully for privacy and storage reasons.Please send another zip or the same zip to filterout more fileformats.....Thank you......")


@bot.message_handler(commands=['txt'])
def opusfilter(message):
    bot.reply_to(message,"Please wait while filtering out........")
    try:
        with zipfile.ZipFile(f"{dir}/{original_file_name}", 'r') as zip_ref:
            os.mkdir(f"{dir}/extracted")
            zip_ref.extractall(f"{dir}/extracted")
        time.sleep(0.01)

        files=os.listdir(f"{dir}/extracted")
        for i in files:
            if i.endswith(".txt"):
                with open(f"{dir}/extracted/{i}","rb") as f:
                    bot.send_document(message.chat.id,f)

        if checkfileEXT(files,".txt")==1:
            bot.reply_to(message,"These are all .txt files.....")
        else:
            bot.reply_to(message,"There are no txt file......")
    except:
        bot.reply_to(message,"Send non-corrupted zip file.....")

    time.sleep(0.01)
    for i in dir:
        if os.path.isdir(f"{dir}/{i}"):
            shutil.rmtree(f"{dir}/{i}")
    bot.send_message(message.chat.id,"Server Cleaned Successfully for privacy and storage reasons.Please send another zip or the same zip to filterout more fileformats.....Thank you......")


@bot.message_handler(commands=['allfiles'])
def opusfilter(message):
    bot.reply_to(message,"Please wait while filtering out........")
    try:
        with zipfile.ZipFile(f"{dir}/{original_file_name}", 'r') as zip_ref:
            os.mkdir(f"{dir}/extracted")
            zip_ref.extractall(f"{dir}/extracted")
        time.sleep(0.01)

        files=os.listdir(f"{dir}/extracted")
        for i in files:

            with open(f"{dir}/extracted/{i}","rb") as f:
                bot.send_document(message.chat.id,f)


        bot.reply_to(message,"These are all files.....")

    except:
        bot.reply_to(message,"Send non-corrupted zip file.....")

    time.sleep(0.01)
    for i in dir:
        if os.path.isdir(f"{dir}/{i}"):
            shutil.rmtree(f"{dir}/{i}")
    bot.send_message(message.chat.id,"Server Cleaned Successfully for privacy and storage reasons.Please send another zip or the same zip to filterout more fileformats.....Thank you......")

print("Bot started.......")
while True:
    try:
        bot.polling(none_stop=True)
    except ConnectionError as e:
        print(f"Connection error: {e}. Retrying...")
        # Implement your retry logic here or just pass to retry on the next loop iteration
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# bot.polling()