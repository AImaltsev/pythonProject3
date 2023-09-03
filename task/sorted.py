import math

# Вычисляем 100!
factorial_100 = math.factorial(100)

# Преобразуем значение в строку
factorial_str = str(factorial_100)

# Подсчитываем количество символов
num_digits = len(factorial_str)

print("Количество цифр в 100!:", num_digits)
