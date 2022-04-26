from telebot import TeleBot
from collections import defaultdict
from telebot import types
import re

token = '5284544538:AAHYMdJ0uhmNkGDWD-2byon6XFgSAqovPaw'

bot = TeleBot(token)

commands = ['/add', '/list', '/reset']
buttons = ['Yes', 'No']
START, SET_NAME, SET_COORDS, SET_PHOTO, ADD_PLACE = range(5)

places = defaultdict(lambda: [])
place = defaultdict(lambda: {})
user_state = defaultdict(lambda: START)


def get_user_state(message):
    return user_state[message.chat.id]


def update_user_state(message, state):
    user_state[message.chat.id] = state


def check_coordinates(message):
    text = message.text
    c = text.split(', ')[:2]
    try:
        coords = set(map(float, c))
        return coords
    except ValueError:
        return False


def draw_buttons():
    keyboard = types.InlineKeyboardMarkup()
    btns = [types.InlineKeyboardButton(text=button, callback_data=button) for button in buttons]
    keyboard.add(*btns)
    return keyboard


def add(param, value):
    place[param] = value


@bot.callback_query_handler(lambda x: True)
def callback_handler(callback):
    if callback.data == 'Yes':
        places[callback.from_user.id].append(dict(place))
        bot.send_message(chat_id=callback.from_user.id,
                         text=f'Place {place["name"]} has been added')
    update_user_state(callback.message, START)
    bot.send_message(chat_id=callback.from_user.id,
                     text='Waiting for the next command')
    print(dict(places), get_user_state(callback.message))


def store_place(message):
    keyboard = draw_buttons()
    bot.send_message(message.chat.id, f'Do you want to add this place: \n{dict(place)}',
                     reply_markup=keyboard)


def list():
    pass


def reset():
    pass


@bot.message_handler(func=lambda message: get_user_state(message) == START,
                     commands=['add'])
def command_add(message):
    bot.send_message(message.chat.id, "Set cafe name")
    update_user_state(message, SET_NAME)


@bot.message_handler(func=lambda message: get_user_state(message) == SET_NAME)
def set_name(message):
    add('name', message.text)
    bot.send_message(message.chat.id, "Set coordinates")
    update_user_state(message, SET_COORDS)


@bot.message_handler(func=lambda message: get_user_state(message) == SET_COORDS)
def set_coordinates(message):
    coords = check_coordinates(message)
    if not coords:
        bot.send_message(message.chat.id, 'Incorrect coordinates. Please use format "lat, long"')
    else:
        add('coordinates', str(coords))
        bot.send_message(message.chat.id, "Set photo or type 'skip' to skip adding the photo")
        update_user_state(message, SET_PHOTO)


@bot.message_handler(content_types=['photo'])
@bot.message_handler(func=lambda message: get_user_state(message) == SET_PHOTO)
def set_photo(message):
    if message.photo is not None:
        add('photo', message.photo)
        update_user_state(message, ADD_PLACE)
        store_place(message)
    bot.send_message(message.chat.id, f"Photo is not set for the place {place['name']}")
    update_user_state(message, ADD_PLACE)
    store_place(message)


@bot.message_handler(func=lambda message: message.text not in commands)
def simple_message(message):
    bot.send_message(message.chat.id, 'Please type your command')


bot.polling()