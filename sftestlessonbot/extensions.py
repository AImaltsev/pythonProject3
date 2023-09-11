import requests
import json
from tconf import api_currency

# Словарь для преобразования названий валют на русском в английский
currency_names = {
    'доллар': 'USD',
    'рубль': 'RUB',
    'евро': 'EUR',
}

# Функция для преобразования названия валюты из русского в английский
def translate_currency_name(name):
    return currency_names.get(name.lower(), name)

class APIException(Exception):
    def __init__(self, message):
        self.message = message

class CurrencyConverter:
    BASE_URL = "https://api.currencyapi.com/v3/latest"

    @staticmethod
    def get_price(base, quote, amount):
        params = {
            "apikey": api_currency,
        }

        response = requests.get(CurrencyConverter.BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            raise APIException("Не удалось получить данные из  API")

        if base not in data["data"] or quote not in data["data"]:
            raise APIException("Ошибка названия валюты")

        base_rate = data["data"][base]["value"]
        quote_rate = data["data"][quote]["value"]
        exchange_rate = quote_rate / base_rate
        converted_amount = amount * exchange_rate
        return converted_amount