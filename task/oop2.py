class Parent:
    def show_message(self):
        print("Это метод из родительского класса.")

class Child(Parent):
    def show_message(self):
        super().show_message()  # Вызываем метод родительского класса
        print("Это метод из дочернего класса.")

child = Child()
child.show_message()