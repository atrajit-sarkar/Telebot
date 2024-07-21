from telegram.ext import Updater, CommandHandler
import schedule
import time
import threading
from Atrmaths import TELEBOT_API
# Replace 'YOUR_TOKEN' with your actual bot token
updater = Updater(TELEBOT_API.READ_API(),update_queue=None)
dispatcher = updater.start_polling()

# Global variable to keep track of the notification state
notification_enabled = False

def enable(update, context):
    global notification_enabled
    notification_enabled = True
    update.message.reply_text('Notifications enabled.')

def disable(update, context):
    global notification_enabled
    notification_enabled = False
    update.message.reply_text('Notifications disabled.')

def send_notification(context):
    job = context.job
    context.bot.send_message(job.context, text='Hourly notification!')

def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)

def callback_hourly(context):
    global notification_enabled
    if notification_enabled:
        context.bot.send_message(chat_id=context.job.context,
                                 text='Hourly notification!')

# Handlers for enabling and disabling notifications
enable_handler = CommandHandler('enable', enable)
dispatcher.add_handler(enable_handler)

disable_handler = CommandHandler('disable', disable)
dispatcher.add_handler(disable_handler)

# Schedule the hourly notification
updater.job_queue.run_repeating(callback_hourly, interval=5, first=0)

# Start the bot
updater.start_polling()

# Start the schedule checker thread
threading.Thread(target=schedule_checker).start()

# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT.
updater.idle()
