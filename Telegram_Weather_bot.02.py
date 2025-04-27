from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from pyowm import OWM
from pyowm.utils import config

updater = Updater(token='...', use_context=True)

config_dict = config.get_default_config()
config_dict['language'] = 'ru'
API = '229ab9c67b33335982cea4be6bf1d6bf'
owm = OWM(API, config_dict)

dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Здравствуйте! Введите город, который вас интересует")


def weather(update, context):
    city = update.message.text
    #if city in data:
    context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Секундочку!')
    mrg = owm.weather_manager()
    observation = mrg.weather_at_place(city)
    w = observation.weather

    temp = w.temperature('celsius')['temp']
    hym = w.humidity
    detailed_status = w.detailed_status
    wind = w.wind()['speed']
    clouds = w.clouds
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='В городе {} сейчас температура {} по Цельсию, {}.'.format(city, temp, detailed_status))
    context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Влажность: {}%\nОблака: {}%\nСкорость ветра: {} м/с\n'.format(hym, clouds, wind))
    context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Хорошего дня!')
    context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Для повторного запроса введите /start')

    #else:
        #context.bot.send_message(chat_id=update.effective_chat.id, text='Упс! Кажется произошла ошибка! Повторите попытку или введите /help, чтобы узнать больше')


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Возможные варианты, почему у вас не сработала программа:\n1) Вы ввели не город\n2) Такого города нет\n3) Не выполнены условия ввода')


help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

weather_handler = MessageHandler(Filters.text & (~Filters.command), weather)
dispatcher.add_handler(weather_handler)


updater.start_polling()
updater.idle()
