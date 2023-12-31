#3 бессонных дня и вуаля. Готово!
# Вроде протестировал разные сценарии и всё должно работать как надо.
# Надеюсь быстро разберётесь.
# Постараюсь по маскимуму всё подробно откомментить

import random #сделал через Рандом.

#Сначала идёт представление кораблей
class Ship:
    def __init__(self, size):
        self.size = size
        self.hits = 0
        self.coords = set()

    def hit(self):
        self.hits += 1

    def is_sunk(self):
        return self.hits == self.size

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['О' for _ in range(size)] for _ in range(size)]
        self.ships = []

    def place_ship(self, ship):
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            orientation = random.choice(['horizontal', 'vertical'])

            if self.can_place_ship(ship, x, y, orientation):
                # Проверяем, что между кораблями на одну клетку есть отступ
                if orientation == 'horizontal':
                    if x > 0 and self.grid[y][x - 1] == '■':
                        continue
                    if x + ship.size < self.size and self.grid[y][x + ship.size] == '■':
                        continue
                elif orientation == 'vertical':
                    if y > 0 and self.grid[y - 1][x] == '■':
                        continue
                    if y + ship.size < self.size and self.grid[y + ship.size][x] == '■':
                        continue

                self.add_ship(ship, x, y, orientation)
                break

    def can_place_ship(self, ship, x, y, orientation):
        if orientation == 'horizontal':
            for i in range(ship.size):
                if x + i >= self.size or self.grid[y][x + i] == '■':
                    return False
                for j in range(max(0, y - 1), min(self.size, y + 2)):
                    if self.grid[j][x + i] == '■':
                        return False
        elif orientation == 'vertical':
            for i in range(ship.size):
                if y + i >= self.size or self.grid[y + i][x] == '■':
                    return False
                for j in range(max(0, x - 1), min(self.size, x + 2)):
                    if self.grid[y + i][j] == '■':
                        return False
        return True

    def add_ship(self, ship, x, y, orientation):
        self.ships.append(ship)
        if orientation == 'horizontal':
            for i in range(ship.size):
                self.grid[y][x + i] = '■'
                ship.coords.add((y, x + i))
                if y > 0:
                    self.grid[y - 1][x + i] = 'О'
                if y < self.size - 1:
                    self.grid[y + 1][x + i] = 'О'
            if x > 0:
                self.grid[y][x - 1] = 'О'  # Добавляем отступ слева от корабля
            if x + ship.size < self.size:
                self.grid[y][x + ship.size] = 'О'  # Добавляем отступ справа от корабля
        elif orientation == 'vertical':
            for i in range(ship.size):
                self.grid[y + i][x] = '■'
                ship.coords.add((y + i, x))
                if x > 0:
                    self.grid[y + i][x - 1] = 'О'
                if x < self.size - 1:
                    self.grid[y + i][x + 1] = 'О'
            if y > 0:
                self.grid[y - 1][x] = 'О'  # Добавляем отступ сверху от корабля
            if y + ship.size < self.size:
                self.grid[y + ship.size][x] = 'О'  # Добавляем отступ снизу от корабля

    def display(self, hide_ships=False):
        header = '   ' + ' | '.join(str(i + 1) for i in range(self.size))
        print(header)
        for i in range(self.size):
            row = f'{chr(65 + i)} | ' + ' | '.join(self.grid[i])
            print(row)

#в этой функции есть несколько элементов для отладки.
# Долго писал и не мог понять почему корабли убиты, а победы нет.
# Пришлось смотреть состояния кораблей после каждого хода. Не стал убирать эти строки
def main():
    player_board = Board(6)
    computer_board = Board(6)

    player_ships = [Ship(3), Ship(2), Ship(2), Ship(1), Ship(1), Ship(1), Ship(1)]
    computer_ships = [Ship(3), Ship(2), Ship(2), Ship(1), Ship(1), Ship(1), Ship(1)]

    for ship in player_ships:
        player_board.place_ship(ship)

    for ship in computer_ships:
        computer_board.place_ship(ship)

    player_moves = set()
    computer_moves = set()

    while True:
        print("Поле игрока!:")
        player_board.display()
        print("\nПоле компьютера!:")
        computer_board.display(hide_ships=True)

        try:
            player_move = input("Сделайте ход (например, A1): ").upper()
            if player_move in player_moves:
                raise Exception("Вы уже стреляли по этой ячейке.")

            player_moves.add(player_move)
            x = int(player_move[1]) - 1
            y = ord(player_move[0]) - ord('A')

            if computer_board.grid[y][x] == '■':
                print("Вы подбили вражеский корабль!")
                for ship in computer_ships:
                    if (y, x) in ship.coords:
                        ship.hit()
                        if ship.is_sunk():
                            print("Вражеский корабль потоплен!")
                            for coord in ship.coords:
                                computer_board.grid[coord[0]][coord[1]] = 'X'
                            computer_ships.remove(ship)
                        else:
                            computer_board.grid[y][x] = 'X'
            else:
                print("Мимо!")
                computer_board.grid[y][x] = 'T'

            for ship in player_ships:
                print(f"Игрок: Корабль размером {ship.size}, попаданий: {ship.hits}, координаты: {ship.coords}")

            while True:
                computer_move = (random.randint(0, 5), random.randint(0, 5))
                if computer_move not in computer_moves:
                    computer_moves.add(computer_move)
                    break

            if player_board.grid[computer_move[0]][computer_move[1]] == '■':
                print("Компьютер попал по вашему кораблю!")
                for ship in player_ships:
                    if computer_move in ship.coords:
                        ship.hit()
                        if ship.is_sunk():
                            print("Ваш корабль потоплен!")
                        player_board.grid[computer_move[0]][computer_move[1]] = 'X'
                        ship.coords.remove(computer_move)
            else:
                print("Компьютер промахнулся!")
                player_board.grid[computer_move[0]][computer_move[1]] = 'T'

            for ship in computer_ships:
                print(f"Компьютер: Корабль размером {ship.size}, попаданий: {ship.hits}, координаты: {ship.coords}")

            if all(ship.is_sunk() for ship in computer_ships):
                print("Поздравляю! Вы выиграли!")
                break

            if all(ship.is_sunk() for ship in player_ships):
                print("Компьютер выиграл!")
                break

            print("Состояние игры:")
            print("Корабли противника:")
            for ship in computer_ships:
                print(f"Корабль размером {ship.size}, потоплен: {ship.is_sunk()}")
            print("Ваши корабли:")
            for ship in player_ships:
                print(f"Корабль размером {ship.size}, потоплен: {ship.is_sunk()}")

        except Exception as e:
            print("Ошибка:", e)

if __name__ == "__main__":
    main()
