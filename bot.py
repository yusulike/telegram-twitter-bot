#!/user/bin/env python3
import common

from telegram.ext import Updater
from telegram.ext import CommandHandler

#command handlers
def subscribe(bot, update):
    if update.message.chat_id not in common.subscribers:
        common.subscribers.append(update.message.chat_id)
        bot.sendMessage(update.message.chat_id, text='Subscribed!')
        common.saveSubscribers(common.subscribers)
    else:
        bot.sendMessage(update.message.chat_id, text='Already Subscribed!')


def unsubscribe(bot, update):
    if update.message.chat_id in common.subscribers:
        common.subscribers.remove(update.message.chat_id)
        bot.sendMessage(update.message.chat_id, text='Unsubscribed!')
        common.saveSubscribers(common.subscribers)
    else:
        bot.sendMessage(update.message.chat_id, text='You need to subscribe first!')

def bot_main(bot_token=""):
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(bot_token)

    common.bot = updater.bot

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler('subscribe', subscribe))
    dp.add_handler(CommandHandler("unsubscribe", unsubscribe))

    # Start the Bot
    updater.start_polling(timeout=5)

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()
