
import datetime
class BankAccount:
    def __init__(self, account_number, balance, owner):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    # Реализуйте метод deposit(amount), который будет увеличивать баланс на указанную сумму.
    def deposit(self, amount):
        self.balance += amount

# Реализуйте метод withdraw(amount), который будет уменьшать баланс на указанную сумму,
# но не должен позволять снять больше, чем есть на счете.

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('На вашем балансе не достаточно средств')

# Создайте класс Transaction (транзакция), который будет представлять собой операцию по банковскому счету.
# Транзакции могут быть двух видов: "депозит" и "снятие".
# Класс Transaction должен иметь атрибуты date, amount, type (тип транзакции) и description (описание транзакции).

class Transaction:
    def __init__(self, amount, type_transaction, description):
        self.date = datetime.datetime.now()
        self.amount = amount
        self.type_transaction = type_transaction
        self.description = description

    def execute(self, account):
        if self.type_transaction == "депозит":
            account.deposit(self.amount)
        elif self.type_transaction == "снятие":
            account.withdraw(self.amount)

object1 = BankAccount(1111, 1000, "MaltsevAI")
object2 = BankAccount(1112, 9999, "YaropolovaAA")
object3 = BankAccount(1113, 4444, "SpitsynAA")
object4 = BankAccount(1114, 4443, "VoronkovAV")

transaction1 = Transaction(1000, 'депозит', "зарплата")
transaction1.execute(object1)

transaction2 = Transaction(5000, 'снятие', "покупка")
transaction2.execute(object2)

transaction3 = Transaction(1000, 'депозит', "зарплата")
transaction3.execute(object3)

transaction4 = Transaction(1000, 'депозит', "зарплата")
transaction4.execute(object4)

# print(object1)
# print(object2)
# print(object3)
# print(object4)
#
# print("Баланс всех счетов:")
# print(f"Счет {object1.account_number}, баланс: {object1.balance}, владелец {object1.owner}")
# print(f"Счет {object2.account_number}, баланс: {object2.balance}, владелец {object2.owner}")
# print(f"Счет {object3.account_number}, баланс: {object3.balance}, владелец {object3.owner}")
# print(f"Счет {object4.account_number}, баланс: {object4.balance}, владелец {object4.owner}")

all_object = [object1, object2, object3, object4]


print(21//4)

for i in all_object:
    print(f"Счет {i.account_number}, баланс: {i.balance}, владелец {i.owner}")

