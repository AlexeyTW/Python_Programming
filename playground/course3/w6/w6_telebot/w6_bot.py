from telebot import TeleBot
from telebot.types import File
from collections import defaultdict
from telebot import types
import sqlite3
import re

token = '5284544538:AAHYMdJ0uhmNkGDWD-2byon6XFgSAqovPaw'

bot = TeleBot(token)

conn = sqlite3.connect('db/places.db', check_same_thread=False)
cursor = conn.cursor()

commands = ['/add', '/list', '/reset']
buttons = ['Yes', 'No']
START, SET_NAME, SET_COORDS, SET_PHOTO, ADD_PLACE = range(5)

places = defaultdict(lambda: [])
place = defaultdict(lambda: {})
user_state = defaultdict(lambda: START)

def place_to_db(user_id: int, name: str, coordinates: str, photo: str):
    cursor.execute('insert into places (user_id, name, coords, photo) values (?, ?, ?, ?)',
                   (user_id, name, coordinates, photo))
    conn.commit()


def place_from_db(name: str):
    cursor.execute('select * from places where name = "name"', name)

def get_user_state(message):
    return user_state[message.chat.id]


def update_user_state(message, state):
    user_state[message.chat.id] = state


def check_coordinates(message):
    text = message.text
    c = text.split(', ')[:2]
    try:
        coords = str(set(map(float, c)))[1:-1]
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


def store_place(message):
    keyboard = draw_buttons()
    bot.send_message(message.chat.id, f'Do you want to store this place: \n{dict(place)}',
                     reply_markup=keyboard)


def get_places_names(message):
    #user_places = places[message.chat.id][-10:]
    user_places = cursor.execute('select * from places where name = ?')
    #places_names = [item['name'] for item in user_places]
    #return places_names
    print(user_places.fetchall())
    #return user_places


def get_place_by_name(message, name):
    user = message.chat.id
    user_data = places[user]
    p = [item for item in user_data if item['name'] == name][0]
    return p


def list():
    pass


def reset():
    pass


def img_to_blob(photo: types.PhotoSize):
    if photo is not None:
        img = bot.get_file(photo.file_id)
        file = bot.download_file(img.file_path)
        return file


@bot.callback_query_handler(lambda x: True)
def callback_handler(callback):
    names = get_places_names(callback.message)
    if callback.data == 'Yes':
        places[callback.from_user.id].append(dict(place))
        place_to_db(callback.from_user.id,
                    place['name'],
                    place['coordinates'],
                    img_to_blob(place['photo'][0]))
        bot.send_message(chat_id=callback.from_user.id,
                         text=f'Place {place["name"]} has been added')
    if callback.data in names:
        print(place_from_db('c1'))
        plc = get_place_by_name(callback.message, callback.data)
        bot.send_message(callback.from_user.id, f'Place name: {plc["name"]},\n'
                                                f'Coordinates: {plc["coordinates"]}')
        if plc['photo'] is not None:
            file = bot.get_file(plc['photo'][0].file_id)
            img = bot.download_file(file.file_path)
            bot.send_photo(chat_id=callback.from_user.id,
                           photo=img)
    update_user_state(callback.message, START)
    bot.send_message(chat_id=callback.from_user.id,
                     text='Waiting for the next command')
    print(dict(places), get_user_state(callback.message))


@bot.message_handler(func=lambda message: get_user_state(message) == START,
                     commands=['add'])
def command_add(message):
    bot.send_message(message.chat.id, "Set cafe name")
    update_user_state(message, SET_NAME)


@bot.message_handler(commands=['list'])
def list_places(message):
    places_names = get_places_names(message)
    print(places_names)
    keyboard = types.InlineKeyboardMarkup()
    #btns = [types.InlineKeyboardButton(text=button, callback_data=button) for button in places_names]
    #keyboard.add(*btns)
    #bot.send_message(message.chat.id, f'Recent 10 stored places. Select one to get more details',
     #                reply_markup=keyboard)


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
    add('photo', message.photo)
    update_user_state(message, ADD_PLACE)
    if message.photo is None:
        bot.send_message(message.chat.id, f"Photo is not set for the place {place['name']}")
    store_place(message)


@bot.message_handler(func=lambda message: message.text not in commands)
def simple_message(message):
    bot.send_message(message.chat.id, 'Please type your command')



bot.polling()