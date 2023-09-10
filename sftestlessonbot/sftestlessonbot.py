import telebot

TOKEN = "6379299948:AAGcv7L5KIyOKwyGA2Cy1kksDoUT-cDcmqM"

bot = telebot.TeleBot(TOKEN)


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, f"Привет, {message.chat.username}")


bot.polling(none_stop=True)