# Задание: Создание класса "Прямоугольник"
# Создайте класс Rectangle, который будет представлять прямоугольник.
# У прямоугольника должны быть два атрибута: width (ширина) и height (высота).
#
# В классе Rectangle создайте метод area, который будет возвращать площадь прямоугольника (ширина * высота).
#
# Создайте метод perimeter, который будет возвращать периметр прямоугольника (2 * (ширина + высота)).
#
# Создайте объекты двух разных прямоугольников и используйте методы area и perimeter для расчетов.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def area(self):
        return self.width ** 2


rectangle1 = Rectangle(1, 2)
rectangle2 = Rectangle(5, 4)
square1 = Square(10)
print(rectangle1.area())
print(rectangle1.perimeter())
print(rectangle2.perimeter())
print(rectangle2.area())
print(square1.area())
print(square1.perimeter())
