#Первый должен содержать число Пи в виде константы 3.14, и две функции,
# которые будут считать площадь круга и прямоугольника.
import math


def circle(r):
    return math.pi * (r ** 2)

def rectangle(l, w):
    return l * w

if __name__ == '__main__':
   # проверяем работоспособность функции, дальнейшая часть не будет импортирована
   assert circle(5) == 78.5  # если ответы будут отличаться, то будет вызвана ошибка
   assert rectangle(5, 4) == 20