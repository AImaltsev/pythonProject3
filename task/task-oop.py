# Создайте класс MenuItem, представляющий элемент меню в ресторане. У элемента меню должны быть следующие атрибуты:
# Название блюда.
# Описание блюда.
# Цена.
class MenuItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
# Создайте класс Menu, представляющий меню ресторана.
# Меню должно иметь методы для добавления новых элементов меню и вывода всего меню на экран.
#


class Menu:
    def __init__(self):
        self.menu_items = []  # Список для хранения элементов меню

    def add_item_menu(self, item):
        self.menu_items.append(item)

    def all_menu(self):
        for item in self.menu_items:
            print(f"{item.name}: {item.description} - ${item.price}")  # Вывод всего меню на экран

# Создайте класс Table, представляющий стол в ресторане. У стола должны быть следующие атрибуты:
# Номер стола.
# Список заказанных блюд.
# Счет (сумма заказанных блюд).


class Table:
    def __init__(self, number, list_order, check):
        self.number = number
        self.list_order = list_order
        self.check = check


# Создайте класс Order, представляющий заказ клиента. У заказа должны быть следующие атрибуты:
#
# Номер заказа.
# Список элементов заказа (блюд).
# Время заказа.
class Order:
    def __init__(self, number, list_itemmenu, time_order):
        self.number = number
        self.list_itemmenu = list_itemmenu
        self.time_order = time_order

# Создайте класс Customer, представляющий клиента ресторана. У клиента должны быть следующие атрибуты:
#
# Имя клиента.
# Список заказов клиента.
# Реализуйте методы для создания заказа, добавления элементов заказа, расчета счета для стола и клиента.


class Customer:
    def __init__(self, name, list_customer):
        self.name = name
        self.list_customer = list_customer

    def new_order(self):
        pass

    def add_item_order(self):
        pass

    def final_check(self):
        pass

# Создайте класс Restaurant, представляющий ресторан. У ресторана должны быть следующие атрибуты:
#
# Название ресторана.
# Список столов.
# Меню ресторана.
# Реализуйте методы для управления столами (резервирование, освобождение),
# обработки заказов и подсчета общего дохода ресторана.


class Restaurant:
    def __init__(self, brand, list_table, menu):
        self.brand = 'Лукошко у Антошки'
        self.list_table = []
        self.menu = menu

    def reserved_table(self):
        pass

    def clear_table(self):
        pass

    def order_processing(self):
        pass

    def all_babosiki(self):
        pass




# Создайте интерфейс командной строки или графический интерфейс пользователя для взаимодействия с системой управления рестораном.
#
# Протестируйте систему, создав несколько заказов, обрабатывая их и проверяя работу системы управления рестораном.

menu = Menu()

item1 = MenuItem('Абсолют', 'водочка вкусненькая', '10,99')
item2 = MenuItem('шашлык','шашлык из свиной шеи','15,47')

menu.add_item_menu(item1)
menu.add_item_menu(item2)

menu.all_menu()
