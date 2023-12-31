import random
from dataclasses import dataclass


@dataclass
class Cell:
    x: int
    y: int


class Ship:
    def __init__(self, size, x, y, rotation):
        self.cell=Cell(x,y)
        self.size = size
        self.hp = size
        self.rotation = rotation
        self.coords = self._get_coords()
        self.aura = self._get_coords_aura()

    def _get_coords_aura(self):
        aura = []
        for cell in self.coords:
            for d in range(-1, 2):
                x = self.cell.x + d
                for i in range(-1, 2):
                    y=self.cell.y +i
                    aura.append(Cell(x,y))
        # print(f"Начало \n корды {self.coords} \n аура {aura} ,размер  \n  {self.size},\nнос {self.cell},\nповорот {self.rotation} \n конец")
        return tuple(aura)

    def _get_coords(self):
        coords = []
        if self.rotation == "up":
            for i in range(self.size):
                    x = self.cell.x
                    y = self.cell.y - i
                    coords.append(Cell(x, y))
        if self.rotation == "dawn":
            for i in range(self.size):
                x = self.cell.x
                y = self.cell.y + i
                coords.append(Cell(x, y))
        if self.rotation == "right":
            for i in range(self.size):
                x = self.cell.x- i
                y = self.cell.y
                coords.append(Cell(x, y))
        if self.rotation == "left":
            for i in range(self.size):
                x = self.cell.x +i
                y = self.cell.y
                coords.append(Cell(x, y))

        return tuple(coords)

    def hit(self):
        self.hp -= 1

    def destrou(self):
        return self.hp == 0




class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [["~" for i in range(size)] for i in range(size)]
        self.radar = [["~" for i in range(size)] for i in range(size)]
        self.ships_cords = []
        self.list_ships_cords= self._get_coords_ships()
        self.ships = []
        self.board_coords = self._get_coords_board()
        self.ship_vars = [1, 1, 1, 1, 2, 2, 3]
        print(self.ships_cords)
        print(self.ships)
    def _get_coords_ships(self):
        list = []
        for m in self.ships_cords:
            list.append(m[0])
        return list

    def _get_coords_board(self):
        coords = []
        for i in range(0, self.size):
            for d in range(0, self.size):
                coords.append(Cell(i, d))
        return tuple(coords)


    def ship_randomizer(self):
        count=0
        while count<=500:
            vars=self.ship_vars.copy()
            size = random.choice(vars)
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            rotation = random.choice(["left", "right", "up", "dawn"])
            ship = Ship(size, x, y, rotation)
            count+=1
            # надо спросить почему корды из экземпляра достать получилось а ауру нет
            if self.can_plays_ship(ship):
                if self.other_ship(ship):
                    self.add_ship(ship)
                    vars.remove(size)
                    return True
                else:
                    continue
            else:

                continue
        return False

    def can_plays_ship(self, ship):
        for i in ship.coords:
            if i in self.board_coords:
                pass
                if i in self.ships_cords:
                    return False
                else:
                    pass
            else:
                return False
        return True

    def other_ship(self, ship):
        for i in ship.aura:
            if i in self.ships_cords:

                return False
            else:

                pass#(2, 0), (2, 1), (2, 2) (0, 1), (4, 3), (4, 0), (5, 5), (2, 4), (2, 5), (0, 3), (0, 4)]
        return True
    def add_ship(self, ship):

        self.ships.append((ship.cell.x, ship.cell.y))
        for d in list(ship.coords):
            self.ships_cords.append(d)
            if ship.rotation == "left":
                for i in range(ship.size):
                    self.grid[ship.cell.x + i][ship.cell.y] = "■"


            elif ship.rotation == "right":
                for i in range(ship.size):
                    self.grid[ship.cell.x - i][ship.cell.y] = "■"


            elif ship.rotation == "up":
                for i in range(ship.size):
                    self.grid[ship.cell.x][ship.cell.y - i] = "■"


            elif ship.rotation == "dawn":
                for i in range(ship.size):
                    self.grid[ship.cell.x][ship.cell.y + i] = "■"

    def fill_the_field(self):
        counter = 0
        ships_left = len(self.ship_vars)  # Изначально оставшихся кораблей столько, сколько в ship_vars
        max_attempts = 500  # Максимальное количество попыток

        while counter < max_attempts and ships_left > 0:  # Продолжаем, пока не исчерпаны попытки или корабли
            counter += 1

            if self.ship_randomizer():
                ships_left -= 1  # Уменьшаем количество оставшихся кораблей

        # Проверяем, все ли корабли успешно размещены
        if ships_left == 0:
            return True  # Все корабли успешно размещены
        else:
            print("Невозможно разместить все корабли")
            """откатить все изменения или другие действия при неудаче"""
            return False


    # self.Ship.nose

    def fild(self):
        head = "    " + " | ".join(str(i + 1) for i in range(self.size))
        print(head)
        for i in range(self.size):
            f = f"{chr(65 + i)} | " + " | ".join(self.grid[i])
            print(f)

    def radar(self):
        head = "    " + " | ".join(str(i + 1) for i in range(self.size))
        print(head)
        for i in range(self.size):
            f = f"{chr(65 + i)} | " + " | ".join(self.radar[i])
            print(f)


# функиця мейн для тестов не забудь написать свою логику
def main():
    player_board = Board(6)
    computer_board = Board(6)
    success = False
    while success is False:
        success = player_board.fill_the_field()

    player_board.fild()

    player_board.fild()
    print(player_board.ships_cords)
    print(player_board.ships)

    # size_ship_vars = ["1", "1", "1", "1", "2", "2", "3"]
    # player_ships = size_ship_vars
    # comp_ships = size_ship_vars
    # for ship_vars in player_ships:
    #     player_board.ship_randomizer(ship_vars)
    #
    # for ship_vars in comp_ships:
    #     computer_board.ship_randomizer(ship_vars)
    #
    # player_moves = set()
    # computer_moves = set()
    #
    # while True:
    #     print("Поле игрока!:")
    #     player_board.fild()
    #     print("\nПоле компьютера!:")
    #     computer_board.fild()
    #
    #     try:
    #         player_move = input("Сделайте ход (например, A1): ").upper()
    #         if player_move in player_moves:
    #             raise Exception("Вы уже стреляли по этой ячейке.")
    #
    #         player_moves.add(player_move)
    #         x = int(player_move[1]) - 1
    #         y = ord(player_move[0]) - ord('A')
    #
    #         if computer_board.grid[y][x] == '■':
    #             print("Вы подбили вражеский корабль!")
    #             for ship in comp_ships:
    #                 if (y, x) in ship.coords:
    #                     ship.hit()
    #                     if ship.destrou():
    #                         print("Вражеский корабль потоплен!")
    #                         for coord in ship.coords:
    #                             computer_board.grid[coord[0]][coord[1]] = 'X'
    #                         comp_ships.remove(ship)
    #                     else:
    #                         computer_board.grid[y][x] = 'X'
    #         else:
    #             print("Мимо!")
    #             computer_board.grid[y][x] = 'T'
    #
    #         for ship in player_ships:
    #             print(f"Игрок: Корабль размером {ship.size}, попаданий: {ship.hit}, координаты: {ship.coords}")
    #
    #         while True:
    #             computer_move = (random.randint(0, 5), random.randint(0, 5))
    #             if computer_move not in computer_moves:
    #                 computer_moves.add(computer_move)
    #                 break
    #
    #         if player_board.grid[computer_move[0]][computer_move[1]] == '■':
    #             print("Компьютер попал по вашему кораблю!")
    #             for ship in player_ships:
    #                 if computer_move in ship.coords:
    #                     ship.hit()
    #                     if ship.destrou():
    #                         print("Ваш корабль потоплен!")
    #                     player_board.grid[computer_move[0]][computer_move[1]] = 'X'
    #                     ship.coords.remove(computer_move)
    #         else:
    #             print("Компьютер промахнулся!")
    #             player_board.grid[computer_move[0]][computer_move[1]] = 'T'
    #
    #         for ship in comp_ships:
    #             print(f"Компьютер: Корабль размером {ship.size}, попаданий: {ship.hit}, координаты: {ship.coords}")
    #
    #         if all(ship.destrou() for ship in comp_ships):
    #             print("Поздравляю! Вы выиграли!")
    #             break
    #
    #         if all(ship.destrou() for ship in player_ships):
    #             print("Компьютер выиграл!")
    #             break
    #
    #         print("Состояние игры:")
    #         print("Корабли противника:")
    #         for ship in comp_ships:
    #             print(f"Корабль размером {ship.size}, потоплен: {ship.destrou()}")
    #         print("Ваши корабли:")
    #         for ship in player_ships:
    #             print(f"Корабль размером {ship.size}, потоплен: {ship.destrou()}")
    #
    #     except Exception as e:
    #         print("Ошибка:", e)
    #

main()