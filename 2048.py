"""
# 2048 Game

The 2048 game is a sliding tile puzzle game where the goal is to combine tiles with the same power of two until you reach 2048 or higher. 
The game is played on a 4x4 grid, where you can move all the tiles in one direction (up, down, left, or right) using the arrow keys or the WASD keys. 
When two tiles with the same value collide, they merge into one tile with double the value. 
Every move, a new tile with a value of 2 or 4 appears randomly on an empty cell. 
The game ends when there are no more moves possible or when you reach 2048 or higher.

## Rules:
    - The game is played on a 4x4 grid, where you can move all the tiles in one direction (up, down, left, or right) using the arrow keys or the WASD keys.
    - Every move, a new tile with a value of 2 or 4 appears randomly on an empty cell.
    - When two tiles with the same value collide while moving, they merge into one tile with double the value.
    - The resulting tile cannot merge with another tile again in the same move.
    - The game is won when a tile with a value of 2048 appears on the board. You can continue to play after reaching the goal, creating tiles with larger numbers.
    - The game ends when there are no more moves possible or when you reach 2048 or higher.
    
"""

possible_values = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]


class Tile:
    def __init__(self, value: int = 0) -> None:
        self.value = value

    def merge_to(self, neighbor: "Tile") -> int:
        result = 0
        if neighbor.value == self.value:
            neighbor.value += self.value
            self.value = result
            result = neighbor.value
            return result
        return result


class Board:
    def __init__(self) -> None:
        self.tiles = [[Tile() for _ in range(4)] for _ in range(4)]
        self.positions = {
            1: self.tiles[0][0],
            2: self.tiles[0][1],
            3: self.tiles[0][2],
            4: self.tiles[0][3],
            5: self.tiles[1][0],
            6: self.tiles[1][1],
            7: self.tiles[1][2],
            8: self.tiles[1][3],
            9: self.tiles[2][0],
            10: self.tiles[2][1],
            11: self.tiles[2][2],
            12: self.tiles[2][3],
            13: self.tiles[3][0],
            14: self.tiles[3][1],
            15: self.tiles[3][2],
            16: self.tiles[3][3],
        }

    def render(self):
        view = ""
        for rows in self.tiles:
            for columns in rows:
                view += "[ " + str(columns.value if columns.value != 0 else " ") + " ]"
            view += "\n"
        print(view)


