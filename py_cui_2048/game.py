class Game:

    def __init__(self, initial_placement):
        self.game_board = Board(initial_placement)
        self.score = 0
        self.turn = 0


    def check_victory(self):
        for row in self.game_board.board_positions:
            for elem in row:
                if elem == 2048:
                    return True

class Board:

    def __init__(self, initial_placement):

        initial_x1 = initial_placement[0][0]
        initial_y1 = initial_placement[0][1]
        initial_val1 = initial_placement[0][2]
        initial_x2 = initial_placement[1][0]
        initial_y2 = initial_placement[1][1]
        initial_val2 = initial_placement[1][2]
        self.board_positions = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.board_positions[initial_y1][initial_x1] = initial_val1
        self.board_positions[initial_y2][initial_x2] = initial_val2

    def process_columns(self, direction):
        for i in range(0, len(self.board_positions[0])):
            temp = []
            for j in range(0, len(self.board_positions)):
                temp.append(self.board_positions[j][i])
            if direction == 'up':
                temp = temp.reverse()
            self.update_nums(temp)
            if direction == 'up':
                temp.reverse()
            for j in range(0, len(self.board_positions)):
                self.board_positions[j][i] = temp[j]


    def process_rows(self, direction):
        for i in range(0, len(self.board_positions)):
            temp = self.board_positions[i]
            if direction == 'left':
                temp = temp.reverse()
            self.update_nums(temp)
            if direction == 'left':
                temp = temp.reverse()
            self.board_positions[i] = temp


    def update_nums(self, nums):
        counter = 0
        while counter < 3:
            if nums[counter] == nums[counter + 1]:
                nums[counter + 1] = 2 * nums[counter]
                nums[counter] = 0
                counter = counter + 1
            counter = counter + 1
        """
        counter = 3
        while counter >= 0:
            if nums[counter] == 0:
                i = counter - 1
                while i > 0:
                    nums[i] = nums[i - 1]
                    i = i - 1
            else:
                counter = counter - 1
        """


    def print_board(self):
        for i in range(0, len(self.board_positions)):
            print(self.board_positions[i])