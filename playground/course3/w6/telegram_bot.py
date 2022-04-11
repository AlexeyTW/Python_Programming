import telebot


token = '5284544538:AAHYMdJ0uhmNkGDWD-2byon6XFgSAqovPaw'

bot = telebot.TeleBot(token)
currencies = ['euro', 'dollar']


'''def get_currencies(message):
    for cur in currencies:
        if cur in message.text.lower():
            return True
    return False

def check_rates(message):
    rates = {'euro': 85, 'dollar': 78}
    for cur, val in rates.items():
        if cur in message.text.lower():
            return cur, val
    return None, None


@bot.message_handler(commands=['rate'])
@bot.message_handler(func=get_currencies)
def handle_currency(message):
    cur, val = check_rates(message)
    if cur:
        bot.send_message(chat_id=message.chat.id, text=f'{cur} rate is {val}')
    else:
        bot.send_message(chat_id=message.chat.id, text='Check currency rates')'''


@bot.message_handler(content_types=["location"])
def handle_location(message):
    print(message)
    bot.send_message(chat_id=message.chat.id, text=f"Location is {message.location}")


@bot.message_handler()
def handle_message(message):
    print(message)
    bot.send_message(chat_id=message.chat.id, text="Check currency rates")

bot.polling()



