from telegram.ext import Updater,MessageHandler,Filters
import telegram
TOKEN = '1602686596:AAE-FOfkyiIrIxqO7qWNF7eTlsqYomfU03c'
def echo(update,context):
   bot = context.bot
   text = update.message.text
   chat_id = update.message.chat_id
   bot.sendMessage(chat_id,text)
updater = Updater(TOKEN)
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.start_polling()
updater.idle()
