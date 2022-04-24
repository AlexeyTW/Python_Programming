from telebot import TeleBot
from collections import defaultdict
import re

token = '5284544538:AAHYMdJ0uhmNkGDWD-2byon6XFgSAqovPaw'

bot = TeleBot(token)

commands = ['/add', '/list', '/reset']
START, SET_NAME, SET_COORDS, SET_PHOTO = range(4)

places = defaultdict(lambda: {})
user_state = defaultdict(lambda: START)

def get_user_state(message):
    return user_state[message.chat.id]

def update_user_state(message):
    user_state[message.chat.id] += 1

def check_coordinates(message):
    text = message.text
    c = text.split(', ')[:2]
    try:
        coords = set(map(float, c))
        return coords
    except ValueError:
        return False

def add(user_id, param, value):
    places[user_id][param] = value

def list():
    pass

def reset():
    pass


@bot.message_handler(commands=['add'])
def command_add(message):
    print(places, user_state)
    bot.send_message(message.chat.id, "Set cafe name")
    update_user_state(message)

@bot.message_handler(func=lambda message: get_user_state(message) == SET_NAME)
def set_name(message):
    add(message.chat.id, 'name', message.text)
    bot.send_message(message.chat.id, "Set coordinates")
    update_user_state(message)
    print(places, user_state)

@bot.message_handler(func=lambda message: get_user_state(message) == SET_COORDS)
def set_coordinates(message):
    coords = check_coordinates(message)
    if not coords:
        bot.send_message(message.chat.id, 'Incorrect coordinates. Please use format "lat, long"')
    else:
        add(message.chat.id, 'coordinates', coords)
        bot.send_message(message.chat.id, "Set photo or type 'skip' to skip adding the photo")
        update_user_state(message)

@bot.message_handler(func=lambda message: get_user_state(message) == SET_PHOTO)
def set_photo(message):
    if message.text != 'skip':
        add(message.chat.id, 'photo', message.text)
        bot.send_message(message.chat.id, f'Item: \n{dict(places)}')
        user_state[message.chat.id] = 0
        print(places, user_state)
        return
    bot.send_message(message.chat.id, f'Item: \n{dict(places)}')
    user_state[message.chat.id] = 0
    print(places, user_state)

@bot.message_handler(func=lambda message: message.text not in commands)
def simple_message(message):
    bot.send_message(message.chat.id, 'Please type your command')


bot.polling()