import telebot
from tconf import telegram_token
from extensions import CurrencyConverter, APIException, translate_currency_name

bot = telebot.TeleBot(telegram_token)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Для конвертации валюты, отправьте сообщение в формате:\n"
                                      "<имя валюты 1> <имя валюты 2> <количество валюты 1>\n"
                                      "Например: доллар рубль 100")

@bot.message_handler(commands=['values'])
def handle_values(message):
    bot.send_message(message.chat.id, "Доступные валюты для конвертации: доллар, евро, рубль")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        input_text = message.text.lower()
        input_list = input_text.split()

        if len(input_list) != 3:
            raise APIException("Введен неверный формат")

        base_currency = translate_currency_name(input_list[0])
        quote_currency = translate_currency_name(input_list[1])
        amount = float(input_list[2])

        result = CurrencyConverter.get_price(base_currency, quote_currency, amount)

        response_text = f"{amount} {base_currency} = {result} {quote_currency}"

        bot.send_message(message.chat.id, response_text)

    except APIException as e:
        bot.send_message(message.chat.id, f"Ошибка: {e.message}")

    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")

bot.polling(none_stop=True)