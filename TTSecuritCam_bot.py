# TTSecurityCam_Bot for Telegram, need to fix problem with secret_files.py
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, Updater
from secret_files import TelegramIDs
# Telegram bot to send notifications to Telegram account for detections

updater = Updater(TelegramIDs.telegram_data["bot_api_token"])
bot = updater.bot

ownerIDs = TelegramIDs.telegram_data["owner_ids"]
for ownerID in ownerIDs:
    try:
        bot.sendMessage(chat_id=ownerID, text='Hello there, I\'m back!')
    except:
        # most likely network problem or user has blocked the bot
        print('Could not send hello to user %s:' % ownerID)
