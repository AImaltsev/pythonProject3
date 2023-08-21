import random

class Ship:
    def __init__(self, size):
        self.size = size
        self.hits = 0
        self.coords = []

    def hit(self):
        self.hits += 1

    def is_sunk(self):
        return self.hits >= self.size

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
                self.add_ship(ship, x, y, orientation)
                break

    def can_place_ship(self, ship, x, y, orientation):
        if orientation == 'horizontal':
            for i in range(ship.size):
                if x + i >= self.size or self.grid[y][x + i] == '■':
                    return False
                for j in range(max(0, x + i - 1), min(self.size, x + i + 2)):
                    if y > 0 and self.grid[y - 1][j] == '■':
                        return False
                    if y < self.size - 1 and self.grid[y + 1][j] == '■':
                        return False
                    if self.grid[y][j] == '■':  # Проверка на отступы между кораблями по вертикали
                        return False
        elif orientation == 'vertical':
            for i in range(ship.size):
                if y + i >= self.size or self.grid[y + i][x] == '■':
                    return False
                for j in range(max(0, y + i - 1), min(self.size, y + i + 2)):
                    if x > 0 and self.grid[j][x - 1] == '■':
                        return False
                    if x < self.size - 1 and self.grid[j][x + 1] == '■':
                        return False
                    if self.grid[j][x] == '■':  # Проверка на отступы между кораблями по горизонтали
                        return False
        return True

    def add_ship(self, ship, x, y, orientation):
        self.ships.append(ship)
        if orientation == 'horizontal':
            for i in range(ship.size):
                self.grid[y][x + i] = '■'
        elif orientation == 'vertical':
            for i in range(ship.size):
                self.grid[y + i][x] = '■'

    def display(self, hide_ships=False):
        header = '   ' + ' | '.join(str(i + 1) for i in range(self.size))
        print(header)
        for i in range(self.size):
            row = f'{chr(65 + i)} | ' + ' | '.join(self.grid[i])
            print(row)

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
            x = ord(player_move[0]) - ord('A')
            y = int(player_move[1]) - 1

            if computer_board.grid[y][x] == '■':
                print("Вы подбили вражеский корабль!")
                for ship in computer_ships:
                    if (y, x) in ship.coords:
                        ship.hit()
                        if ship.is_sunk():
                            print("Вражеский корабль потоплен!")
                        computer_board.grid[y][x] = 'X'  # Изменяем символ на X для отображения попадания

            else:
                print("Мимо!")
                player_board.grid[y][x] = 'T'  # Изменяем символ на T для отображения промаха

            computer_move = (random.randint(0, 5), random.randint(0, 5))
            if player_board.grid[computer_move[0]][computer_move[1]] == '■':
                print("Компьютер попал по вашему кораблю!")
                for ship in player_ships:
                    if (computer_move[0], computer_move[1]) in ship.coords:
                        ship.hit()
                        if ship.is_sunk():
                            print("Ваш корабль потоплен!")
                        player_board.grid[computer_move[0]][
                            computer_move[1]] = 'X'  # Изменяем символ на X для отображения попадания
            else:
                print("Компьютер промахнулся!")
                player_board.grid[computer_move[0]][
                    computer_move[1]] = 'T'  # Изменяем символ на T для отображения промаха

            if all(ship.is_sunk() for ship in computer_ships):
                print("Поздравляю! Вы выиграли!")
                break

            if all(ship.is_sunk() for ship in player_ships):
                print("Компьютер выиграл!")
                break

        except Exception as e:
            print("Ошибка:", e)

if __name__ == "__main__":
    main()