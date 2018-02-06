import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
    update.effective_message.reply_text("Hi!")

def forwardThis(bot, update):
    bot.forwardMessage(chat_id='@csefeeder',from_chat_id=update.message.chat.id,message_id=update.message.reply_to_message.message_id)

if __name__ == "__main__":

    TOKEN = "YOUR_TOKEN"
    NAME = "YOUR_HEROKU_APP_NAME"
    PORT = int(os.environ.get('PORT','8443'))
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler("send",forwardThis))
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()
