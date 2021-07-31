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
    inline_btn = InlineKeyboardButton(text='inline button',callback_data='data')
    
    btn = InlineKeyboardMarkup(inline_keyboard=[[inline_btn]])


    update.message.reply_text("Use /start to test this bot.",
    reply_markup = btn
    )  

def get_data(update,context):
    query = update.callback_query
    print('get data:',query.data)

updater = Updater(TOKEN)
updater.dispatcher.add_handler(MessageHandler(Filters.text('1'), button))

# handler for callback data
updater.dispatcher.add_handler(CallbackQueryHandler(get_data))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.start_polling()
updater.idle()
