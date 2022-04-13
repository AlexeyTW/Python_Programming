from telebot import TeleBot
from collections import defaultdict

token = '5284544538:AAHYMdJ0uhmNkGDWD-2byon6XFgSAqovPaw'

bot = TeleBot(token)
START, MODEL, PRICE, CONFIRM = range(4)

USER_STATE = defaultdict(lambda: START)
PRODUCTS = defaultdict(lambda: {})

def get_user_state(message):
    return USER_STATE[message.chat.id]

def update_user_state(message, state):
    USER_STATE[message.chat.id] = state

def get_product(user_id):
    return PRODUCTS[user_id]

def update_product(user_id, key, value):
    PRODUCTS[user_id][key] = value

@bot.message_handler(func=lambda message: get_user_state(message) == START)
def handle_message(message):
    bot.send_message(message.chat.id, 'Type model')
    update_user_state(message, MODEL)

@bot.message_handler(func=lambda message: get_user_state(message) == MODEL)
def handle_title(message):
    update_product(message.chat.id, 'title', message.text)
    bot.send_message(message.chat.id, 'Set price')
    update_user_state(message, PRICE)

@bot.message_handler(func=lambda message: get_user_state(message) == PRICE)
def handle_price(message):
    update_product(message.chat.id, 'price', message.text)
    product = get_product(message.chat.id)
    bot.send_message(message.chat.id, f'Confirm goods: \n{product}')
    update_user_state(message, CONFIRM)

@bot.message_handler(func=lambda message: get_user_state(message) == CONFIRM)
def handle_confirmation(message):
    if 'yes' in message.text.lower():
        bot.send_message(message.chat.id, 'DONE!')
    update_user_state(message, START)

bot.polling()