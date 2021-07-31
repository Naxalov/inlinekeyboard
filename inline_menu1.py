from telegram.ext import Updater,MessageHandler,Filters,CallbackQueryHandler
from telegram import ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton
import telegram
TOKEN = '1602686596:AAE-FOfkyiIrIxqO7qWNF7eTlsqYomfU03c'
def echo(update,context):
   bot = context.bot
   text = update.message.text
   chat_id = update.message.chat_id
   bot.sendMessage(chat_id,text)

def button(update,context):
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data='2'),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Use /start to test this bot.",
    reply_markup = reply_markup
    )  

def get_data(update,context):
    query = update.callback_query
    query.answer('TXT')
    print('get data:',query.data)

updater = Updater(TOKEN)
updater.dispatcher.add_handler(MessageHandler(Filters.text('1'), button))

# handler for callback data
updater.dispatcher.add_handler(CallbackQueryHandler(get_data))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.start_polling()
updater.idle()
