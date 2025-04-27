from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


updater = Updater(token='...', use_context=True)

dispatcher = updater.dispatcher

MAIN_KEYBOARD = [['Понедельник', 'Вторник'], ['Среда', 'Четверг'], ['Пятница']]

monday = '1'
tuesday = '2'
wednesday = '3'
thursday = '4'
friday = '5'


def send(bot, chat_id, text, keyboard=None):
    reply_keyboard = None
    if keyboard:
        reply_keyboard = ReplyKeyboardMarkup(
            keyboard=keyboard,
            reply_keyboard=True,
            one_time_keyboard=True
        )
    bot.send_message(
        chat_id=chat_id, text=text, reply_markup=reply_keyboard
    )


def start_action(update, context):
    cid = update.effective_chat.id
    send(context.bot, cid, 'Готов служить!', MAIN_KEYBOARD)


def text_action(update, context):
    text = update.message.text.lower()
    cid = update.effective_chat.id
    if text == 'понедельник':
        send(context.bot, cid, monday)

    elif text == 'вторник':
        send(context.bot, cid, tuesday)

    elif text == 'среда':
        send(context.bot, cid, wednesday)

    elif text == 'четверг':
        send(context.bot, cid, thursday)

    elif text == 'пятница':
        send(context.bot, cid, friday)

    else:
        send(context.bot, cid, 'Моя твоя не понимать')


start_handler = CommandHandler('start', start_action)
dispatcher.add_handler(start_handler)


text_handler = MessageHandler(Filters.text & (~Filters.command), text_action)
dispatcher.add_handler(text_handler)


updater.start_polling()
updater.idle()
