from telebot import TeleBot
from telebot.types import File
from collections import defaultdict
from telebot import types
import sqlite3
import re

token = '5284544538:AAHYMdJ0uhmNkGDWD-2byon6XFgSAqovPaw'
api_key = 'AIzaSyDcXR8kJ-AYp18yE-QHxnYgfTSm8gYK1So'

bot = TeleBot(token)

conn = sqlite3.connect('db/places.db', check_same_thread=False)
cursor = conn.cursor()

commands = ['/add', '/list', '/reset']
buttons = ['Да', 'Нет']
START, SET_NAME, SET_COORDS, SET_PHOTO, ADD_PLACE, USER_COORDS = range(6)

places = defaultdict(lambda: [])
place = defaultdict(lambda: {})
user_state = defaultdict(lambda: START)

def place_to_db(user_id, name, coordinates, photo):
    cursor.execute('insert into places (user_id, name, coords, photo) values (?, ?, ?, ?)',
                   (user_id, name, coordinates, photo))
    conn.commit()


def get_user_state(message):
    return user_state[message.chat.id]


def update_user_state(message, state):
    user_state[message.chat.id] = state


def check_coordinates(message):
    text = message.text
    c = text.split(', ')[:2]
    if len(c) != 2:
        return False
    try:
        coords = str(set(map(float, c)))[1:-1]
        return coords
    except ValueError:
        return False


def draw_buttons(btns_list):
    keyboard = types.InlineKeyboardMarkup()
    _btns = [types.InlineKeyboardButton(text=button, callback_data=button) for button in btns_list]
    keyboard.add(*_btns)
    return keyboard


def add(param, value):
    place[param] = value


def store_place(message):
    keyboard = draw_buttons(buttons)
    bot.send_message(message.chat.id, 'Вы хотите сохранить это место?',
                     reply_markup=keyboard)


def get_places_names(message):
    user_places = cursor.execute(f'select * from places where user_id = {message.chat.id}').fetchall()
    places_names = [item[1] for item in user_places]
    return places_names


def get_place_by_name(message, name):
    user = message.chat.id
    _places = cursor.execute(f'SELECT * FROM places WHERE user_id = {user}').fetchall()
    place = [i for i in _places if i[1] == name]
    return place[-1]


def img_to_db(photo):
    if photo is not None:
        file_id = bot.get_file(photo.file_id)
        return file_id

def calc_dist(origin, destination):
    x_orig, y_orig = list(map(float, origin.split(',')))
    x_dest, y_dest = list(map(float, destination.split(',')))
    dist = ((x_dest - x_orig) ** 2 + (y_dest - y_orig) ** 2) ** 0.5
    return dist

@bot.callback_query_handler(lambda callback: True)
def callback_handler(callback):
    names = get_places_names(callback.message)
    if callback.data == 'Да':
        place_to_db(callback.from_user.id,
                    place['name'],
                    place['coordinates'],
                    place['photo'][-1].file_id if place['photo'] else None)
        bot.send_message(chat_id=callback.from_user.id,
                         text=f'Место {place["name"]} добавлено')

    if callback.data == 'ОК':
        cursor.execute('delete from places where user_id = {}'.format(callback.from_user.id))
        conn.commit()
        bot.send_message(callback.from_user.id, 'Ваши места были удалены из хранилища данных')

    if callback.data in names:
        plc = get_place_by_name(callback.message, callback.data)
        bot.send_message(callback.from_user.id, f'Имя места: {plc[1]},\n'
                                                f'Координаты: {plc[2]}')
        if plc[3] is not None:
            file = bot.get_file(plc[3])
            img = bot.download_file(file.file_path)
            bot.send_photo(chat_id=callback.from_user.id,
                           photo=img)
        return

    if callback.data == 'Список 10 недавних мест':
        places_names = get_places_names(callback.message)[-10:]
        keyboard = draw_buttons(places_names)
        bot.send_message(callback.from_user.id, f'Недавние 10 мест. Выберите, чтобы получить детали',
                         reply_markup=keyboard)
        return

    if callback.data == 'Все места':
        places_names = get_places_names(callback.message)
        keyboard = draw_buttons(places_names)
        bot.send_message(callback.from_user.id, f'Недавние 10 мест. Выберите, чтобы получить детали',
                         reply_markup=keyboard)
        return

    if callback.data == 'Ближайшее ко мне':
        bot.send_message(callback.from_user.id, 'Введите ваши координаты')
        update_user_state(callback.message, USER_COORDS)
        return

    update_user_state(callback.message, START)
    bot.send_message(chat_id=callback.from_user.id,
                     text='Жду следующей команды')

@bot.message_handler(func=lambda message: get_user_state(message) == USER_COORDS)
def get_user_coordinates(message):
    origin = check_coordinates(message)
    if origin:
        dists = {}
        destinations = cursor.execute(f'select name, coords from places where user_id = {message.chat.id}').fetchall()
        for i in destinations:
            dists[calc_dist(origin, i[1])] = i[0]
        nearest_dist = min(dists.keys())
        nearest_place = dists[nearest_dist]
        bot.send_message(message.chat.id, f'Ближайшее к вам место: {nearest_place}\n'
                                          f'Жду следующей команды')
        update_user_state(message, START)
    else:
        bot.send_message(message.chat.id, 'Неверные координаты. Используй формат lat, long. Например:\n'
                                          '58.045966, 38.843106')
        update_user_state(message, USER_COORDS)


@bot.message_handler(func=lambda message: get_user_state(message) == START,
                     commands=['add'])
def command_add(message):
    bot.send_message(message.chat.id, "Задай имя места")
    update_user_state(message, SET_NAME)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я помогу тебе сохранить твои любимые места для посещения.\n'
                                      'Я поддерживаю следующие команды:\n'
                                      '/add - добавить новое место. Нужно предоставить имя и координаты (можно с фото)\n'
                                      '/list - Выбор режима отображения мест:\n'
                                      '- отобразить ближайшее к тебе место\n'
                                      '- отобразить список 10 недавних мест\n'
                                      '- отобразить все места\n'
                                      '/reset - удалить все твои места\n\n'
                                      'Прошу обратить внимание, что ближайшее место определяется путем вычисления\n'
                                      'кратчайшего расстояния по прямой, потому что сервис GoogleMaps API платный')


@bot.message_handler(commands=['list'])
def list_places(message):
    list_options = ['Ближайшее ко мне', 'Список 10 недавних мест', 'Все места']
    opts_keyboard = draw_buttons(list_options)
    bot.send_message(message.chat.id, f'Какие места вы хотите посмотреть?',
                     reply_markup=opts_keyboard)


@bot.message_handler(commands=['reset'])
def reset_places(message):
    keyboard = draw_buttons(['ОК', 'Отмена'])
    bot.send_message(message.chat.id, 'Действительно удалить все ваши места?',
                     reply_markup=keyboard)

@bot.message_handler(func=lambda message: get_user_state(message) == SET_NAME)
def set_name(message):
    add('name', message.text)
    bot.send_message(message.chat.id, "Задай координаты")
    update_user_state(message, SET_COORDS)


@bot.message_handler(func=lambda message: get_user_state(message) == SET_COORDS)
def set_coordinates(message):
    coords = check_coordinates(message)
    if not coords:
        bot.send_message(message.chat.id, 'Неверные координаты. Используй формат lat, long. Например:\n'
                                          '58.045966, 38.843106')
    else:
        add('coordinates', str(coords))
        bot.send_message(message.chat.id, "Задайте фото или введи 'skip' для пропуска шага")
        update_user_state(message, SET_PHOTO)


@bot.message_handler(content_types=['photo'])
@bot.message_handler(func=lambda message: get_user_state(message) == SET_PHOTO)
def set_photo(message):
    add('photo', message.photo)
    update_user_state(message, ADD_PLACE)
    if message.photo is None:
        bot.send_message(message.chat.id, f"Фото не задано для места {place['name']}")
    store_place(message)


@bot.message_handler(func=lambda message: message.text not in commands)
def simple_message(message):
    bot.send_message(message.chat.id, 'Введите корректную команду.\n /start для отображения списка команд')


while True:
    try:
        bot.polling(none_stop=True, interval=1)
    except Exception as ex:
        print(ex)
    finally:
        bot.polling(none_stop=True, interval=1)
