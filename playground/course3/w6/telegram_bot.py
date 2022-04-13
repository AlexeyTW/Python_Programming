import telebot
from telebot import types

token = '5284544538:AAHYMdJ0uhmNkGDWD-2byon6XFgSAqovPaw'

bot = telebot.TeleBot(token)
currencies = ['euro', 'dollar']

def create_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [types.InlineKeyboardButton(text=cur, callback_data=cur) for cur in currencies]
    keyboard.add(*buttons)
    return keyboard


@bot.callback_query_handler(func=lambda x: True)
def callback_handler(callback_query):
    print(callback_query)
    message = callback_query.message
    text = callback_query.data
    cur, val = check_rates_callback(text)
    if cur:
        bot.answer_callback_query(callback_query.id, text=f'{cur} rate is {val}')
    else:
        print('CUR')
        bot.send_message(chat_id=message.chat.id, text="Check currency rates")


def get_currencies(message):
    for cur in currencies:
        if cur in message.text.lower():
            return True
    return False


def check_rates_callback(text):
    rates = {'euro': 85, 'dollar': 78}
    for cur, val in rates.items():
        if cur in text.lower():
            return cur, val
    return None, None


def check_rates(message):
    rates = {'euro': 85, 'dollar': 78}
    for cur, val in rates.items():
        if cur in message.text.lower():
            return cur, val
    return None, None


@bot.message_handler(commands=['rate'])
@bot.message_handler(func=check_rates)
def handle_currency(message):
    print('Currency')
    cur, val = check_rates(message)
    keyboard = create_keyboard()
    if cur:
        bot.send_message(chat_id=message.chat.id, text=f'{cur} rate is {val}', reply_markup=keyboard)
    else:
        print('CUR')
        bot.send_message(chat_id=message.chat.id, text="Check currency rates", reply_markup=keyboard)


bot.polling()



