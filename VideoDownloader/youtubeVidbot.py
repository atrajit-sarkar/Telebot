import telebot
from pytube import YouTube
import instaloader
import os
import shutil
import time
import subprocess
from Atrmaths import TELEBOT_API

dir=os.getcwd()
bot=telebot.TeleBot(TELEBOT_API.READ_API('@VideoDownloader1729Bot'))

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,'''Welcome to Yt To Mp4 Bot.What platform video you want?
                 1. /youtube
                 2./instagram''')
# print("Bot Started.....")

#Youtube downloader section.........
@bot.message_handler(commands=['youtube'])
def link(message):
    bot.reply_to(message,"Enter your youtube link below.........")
    bot.register_next_step_handler(message,convert)
# @bot.message_handler(func=lambda msg: not msg.text.startswith("/"))
def convert(message):
    global chat_id
    chat_id=message.chat.id
    global link
    link=message.text
    try:
        link=YouTube(link)
        bot.reply_to(message,"Which format you want? 1. /mp3  2. /mp4")
    except:
        bot.reply_to(message,"Must provide a valide link of youtube.")
    # print(link)
    # bot.register_next_step_handler(message,conv)
@bot.message_handler(commands=["mp4"]) # fix normal text here
def mp4conv(message):
    
    try:
        bot.reply_to(message,"Plase wait while processing......")
        video=link.streams.get_highest_resolution()
        video.download(output_path="outfile")

        filename=os.listdir("outfile")

        os.rename(fr"{dir}/outfile/{filename[0]}",fr"{dir}/outfile/out.mp4")
        time.sleep(0.5)
        with open(fr"{dir}/outfile/out.mp4","rb") as f:
            bot.send_document(chat_id,f)
        bot.reply_to(message,'''Video coversion successful.Please submit feedback here: /feedback .''')
        bot.reply_to(message,''' Note: Developer has seen a discrepancy in terms of downloading your file. please after download you change the name of your video.Otherwise after you download another video it will be overwritten by the previous one. Sorry for inconvenience. We will try to fix it soon.''')
    except:
        bot.reply_to(message,'''Appologise for error! Your link seems to be a link outside youtube. Please enter a valid youtube link. If you feel that your link is a valid one please try with shorter length video. Submit feedback here: /feedback .''')
    time.sleep(0.5)
    if os.path.exists(fr"{dir}/outfile/out.mp4"):
        for i in os.listdir("outfile"):
            os.remove(fr"{dir}/outfile/{i}")
        os.rmdir("outfile")
     
@bot.message_handler(commands=['mp3'])
def mp3conv(message):
    try:
        bot.reply_to(message,"Please wait while processing......")
        audio=link.streams.filter(only_audio=True).first()
        audio.download(output_path="outfile")
        filename=os.listdir("outfile")

        os.rename(fr"{dir}/outfile/{filename[0]}",fr"{dir}/outfile/out.mp3")
        time.sleep(0.5)
        with open(fr"{dir}/outfile/out.mp3","rb") as f:
            bot.send_document(chat_id,f)
        bot.reply_to(message,'''Audio coversion successful.Please submit feedback here: /feedback .''')
        bot.reply_to(message,''' Note: Developer has seen a discrepancy in terms of downloading your file. please after download you change the name of your file.Otherwise after you download another file it will be overwritten by the previous one. Sorry for inconvenience. We will try to fix it soon.''')
    except:
        bot.reply_to(message,'''Appologise for error! Your link seems to be a link outside youtube. Please enter a valid youtube link. If you feel that your link is a valid one please try with shorter length video. Submit feedback here: /feedback .''')
    
    time.sleep(0.5)
    if os.path.exists(fr"{dir}/outfile/out.mp3"):
        for i in os.listdir("outfile"):
            os.remove(fr"{dir}/outfile/{i}")
        os.rmdir("outfile")

# Instagram Video Downloader Section......
@bot.message_handler(commands=['instagram'])
def instagram(message):
    bot.reply_to(message,"Enter your instagram video link.......")
    bot.register_next_step_handler(message,instamp4)
    
def instamp4(message):
    bot.reply_to(message,"please wait while processing......")
    global L
    L = instaloader.Instaloader()
    global shortcode
    # Load the post using the shortcode
    id=message.chat.id
    try:
        shortcode=message.text
        # shortcode=shortcode.split("/")
        # post = instaloader.Post.from_shortcode(L.context, shortcode[4])

        # # Download the video from the post
        # L.download_post(post, target=post.owner_username)
        with open("insta.py","w") as f:
            f.write(f'''
import instaloader

# Create an instance of Instaloader
L = instaloader.Instaloader()

# The shortcode is part of the video URL: https://www.instagram.com/p/SHORTCODE/
shortcode ="{message.text}"
shortcode=shortcode.split("/")
# print((shortcode[4]))
# Load the post using the shortcode
post = instaloader.Post.from_shortcode(L.context, shortcode[4])

# Download the video from the post
L.download_post(post, target=post.owner_username)
''')
        time.sleep(1)
        process=subprocess.Popen(fr"python insta.py",shell=True,text=True,stdout=subprocess.PIPE)
        
        process.wait()
        # output, _=process.communicate()
        # bot.send_document(message.chat.id,output)
        post = instaloader.Post.from_shortcode(L.context, shortcode[4])
        filename=os.listdir(f"{post.owner_username}")
        for i in filename:
            if i.endswith(".mp4"):
                os.rename(fr"{dir}/{post.owner_username}/{i}",fr"{dir}/{post.owner_username}/out.mp4")
        time.sleep(0.5)
        with open(fr"{dir}/{post.owner_username}/out.mp4","rb") as f:
            bot.send_document(id,f)
        bot.reply_to(message,"Video coversion successful......")
                


    except:
        bot.reply_to(message,"Enter valid link for instagram video!")

    time.sleep(0.5)
    try:
        if os.path.exists(f"{dir}/{post.owner_username}"):
            shutil.rmtree(f"{dir}/{post.owner_username}", ignore_errors=True)
    except:
        return 0





#Feedback section........
@bot.message_handler(commands=['feedback'])
def feedback(message):
    bot.reply_to(message,"To start writing: /write or to quite: /quite")
@bot.message_handler(commands=['write'])
def w(message):
    bot.send_message(message.chat.id,"Enter your issue below:")
    bot.register_next_step_handler(message, storeIssue)
# @bot.message_handler(func=lambda msg: not msg.text.startswith("/"))
def storeIssue(message):
    try:
        issue=message.text
        with open(fr"{dir}/issue.csv","a") as f:
            f.write(f"\n{message.chat.id},{message.chat.username},{issue}")
        with open(fr"{dir}/issue.csv","rb") as f:
            bot.send_document("",f) #Use you primary account chat id here.....
        bot.reply_to(message,"Thanks for your feedback. If there is any issue we will fix soon and if all is fine we are glad to have you. Keep sharing the bot and enjoy together.")
    except:
        bot.reply_to(message,"Please don't provide emojis and stickers.Thank you..")
@bot.message_handler(commands=['quite'])
def quite(message):
    bot.reply_to(message,"Have a nice day.To start again click /start or keep pasting links.")


print("Bot Started......")
# while True:
#     try:
#         bot.polling()
#     except:
#         print("")
bot.polling(long_polling_timeout=3600)
# time.sleep(2)
# os.remove("outfile")
