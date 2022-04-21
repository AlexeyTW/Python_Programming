from telebot import TeleBot
from collections import defaultdict

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
    print(places, user_state)
    bot.send_message(message.chat.id, "Set coordinates")
    update_user_state(message)

@bot.message_handler(func=lambda message: get_user_state(message) == SET_COORDS)
def set_coordinates(message):
    add(message.chat.id, 'coordinates', message.text)
    print(places, user_state)
    bot.send_message(message.chat.id, "Set photo")
    update_user_state(message)

@bot.message_handler(func=lambda message: get_user_state(message) == SET_PHOTO)
def set_photo(message):
    if message.text == 'skip':
        pass
    add(message.chat.id, 'photo', message.text)
    print(places, user_state)
    bot.send_message(message.chat.id, f'Item: \n{places}')
    user_state[message.chat.id] = 0
    print(places, user_state)

@bot.message_handler(func=lambda message: message.text not in commands)
def simple_message(message):
    print(places, user_state)
    bot.send_message(message.chat.id, 'Please type your command')


bot.polling()