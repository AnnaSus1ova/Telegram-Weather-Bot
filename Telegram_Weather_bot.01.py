from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import requests

updater = Updater(token='...', use_context=True)


dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Здравствуйте! Введите город, который вас интересует")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Возможные варианты, почему у вас не сработала программа:\n1) Вы ввели не город\n2) Такого города нет\n3) Не выполнены условия ввода')


help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)


def weather(update, context):
    city = update.message.text
    #if city in data:
    w = requests.get(f'https://wttr.in/{city}?format=3')
    context.bot.send_message(chat_id=update.effective_chat.id, text=w.text)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Для повторного запроса введите /start')
    #else:
    #    context.bot.send_message(chat_id=update.effective_chat.id, text='Упс! Кажется произошла ошибка! Повторите попытку или введите /help, чтобы узнать больше')


weather_handler = MessageHandler(Filters.text & (~Filters.command), weather)
dispatcher.add_handler(weather_handler)


updater.start_polling()
updater.idle()

