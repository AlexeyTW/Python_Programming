import telebot


token = '5284544538:AAHYMdJ0uhmNkGDWD-2byon6XFgSAqovPaw'

bot = telebot.TeleBot(token)

@bot.message_handler()
def handle_message(message):
    bot.send_message(chat_id=message.chat.id, text='Check currency rates')

bot.polling()



