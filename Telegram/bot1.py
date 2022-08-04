from telegram.ext import Updater , CommandHandler , MessageHandler , Filters

token = Updater('1863100350:AAFG0pG-P86ZDv9BE7lCd1sNa4rnxHnNTU4', use_context=True)

def echo(update , context):
    context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

token.dispatcher.add_handler(MessageHandler(Filters.text , echo))

token.start_polling()
token.idle()
