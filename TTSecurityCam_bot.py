# TTSecurityCam_Bot for Telegram, need to fix problem with secret_files.py
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, Updater
from secret_files import TelegramIDs
import asyncio, datetime
# Telegram bot to send notifications to Telegram account for detections

import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

updater = Updater(TelegramIDs.telegram_data["bot_api_token"], 0)
bot = updater.bot

ownerIDs = TelegramIDs.telegram_data["owner_ids"]

application = ApplicationBuilder().token(TelegramIDs.telegram_data["bot_api_token"]).build()

async def start(update: Updater, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!"
    )

now = datetime.datetime.now()
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

#for ownerID in ownerIDs:
   # try:
  #      bot.sendMessage(chat_id=ownerID, text='Hello there, I\'m back!')
 #   except:
        # most likely network problem or user has blocked the bot
#        print('Could not send hello to user %s:' % ownerID)

application.run_polling()
#import requests

#def telegram_bot_sendtext(bot_message):
    
 #   bot_token = TelegramIDs.telegram_data["bot_api_token"]
  #  bot_chatID = ''
   # send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    #response = requests.get(send_text)

   # return response.json()
    

#test = telegram_bot_sendtext("ALERT ALERT")
#print(test)