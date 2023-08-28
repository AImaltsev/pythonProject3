# Задание: Создание классов для геометрических фигур
# Создайте базовый класс Shape (Фигура), у которого будет метод area(),
# который будет возвращать площадь фигуры. Оставьте метод area() без реализации в базовом классе,
# так как каждая конкретная фигура будет его реализовывать по-своему.
#
# Создайте классы для различных геометрических фигур (например, Circle, Triangle, Rectangle, Square),
# которые будут наследоваться от класса Shape. В каждом из этих классов реализуйте метод area()
# для вычисления площади соответствующей фигуры.
#
# Создайте объекты разных геометрических фигур и выведите их площади.
import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

circle = Circle(5)
triangle = Triangle(2, 4)
rectangle = Rectangle( 4, 6)
square = Square(3)

print(circle.area())
print(triangle.area())
print(rectangle.area())
print(square.area())