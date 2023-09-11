import telebot
from tconf import a
TOKEN = a

bot = telebot.TeleBot(TOKEN)


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, f"Привет, {message.chat.username}")


@bot.message_handler(content_types=['photo'])
def handle_photo(message: telebot.types.Message):
    # Отправляем ответное сообщение с привязкой к картинке
    bot.send_message(message.chat.id, "Nice meme XDD", reply_to_message_id=message.message_id)


bot.polling(none_stop=True)