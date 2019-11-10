import random


class Game:

    def __init__(self, initial_placement, board_size = 4):
        self.game_board = Board(initial_placement, board_size)
        self.score = 0
        self.turn = 0


    def check_victory(self):
        for row in self.game_board.board_positions:
            for elem in row:
                if elem == 2048:
                    return True

class Board:

    def __init__(self, initial_placement, board_size):

        initial_x1 = initial_placement[0][0]
        initial_y1 = initial_placement[0][1]
        initial_val1 = initial_placement[0][2]
        initial_x2 = initial_placement[1][0]
        initial_y2 = initial_placement[1][1]
        initial_val2 = initial_placement[1][2]
        self.board_size = board_size
        self.board_positions = []
        temp = []
        for i in range(0, board_size):
            temp.append(0)
        for i in range(0, board_size):
            self.board_positions.append(temp)
        self.board_positions[initial_y1][initial_x1] = initial_val1
        self.board_positions[initial_y2][initial_x2] = initial_val2


    def get_empty_pos_list(self):
        empty_pos_list = []
        for i in range(0, len(self.board_positions)):
            for j in range(0, len(self.board_positions[i])):
                if self.board_positions[i][j] == 0:
                    empty_pos_list.append([i,j])
        return empty_pos_list

    def add_random_tile(self):
        possible_pos = self.get_empty_pos_list()
        rand_val = ((random.randint(1, 10) % 2) + 1) * 2
        rand_pos = possible_pos[random.randint(0, len(possible_pos) - 1)]
        self.board_positions[rand_pos[0]][rand_pos[1]] = rand_val


    def process_columns(self, direction):
        for i in range(0, len(self.board_positions[0])):
            temp = []
            for j in range(0, len(self.board_positions)):
                temp.append(self.board_positions[j][i])
            if direction == 'up':
                temp.reverse()
            self.update_nums(temp)
            if direction == 'up':
                temp.reverse()
            for j in range(0, len(self.board_positions)):
                self.board_positions[j][i] = temp[j]


    def process_rows(self, direction):
        for i in range(0, len(self.board_positions)):
            temp = self.board_positions[i]
            print(temp)
            if direction == 'left':
                temp.reverse()
            self.update_nums(temp)
            if direction == 'left':
                temp.reverse()
            self.board_positions[i] = temp


    def update_nums(self, nums):
        counter = 0
        while counter < (self.board_size - 1):
            next_num = counter + 1
            while  next_num < (self.board_size - 1) and nums[next_num] == 0:
                next_num = next_num + 1
            if nums[counter] == nums[next_num]:
                nums[next_num] = 2 * nums[counter]
                nums[counter] = 0
                counter = next_num
            counter = next_num
        
        output_arr = []
        counter = 3
        non_zero = 0
        while counter >= 0:
            if nums[counter] != 0:
                output_arr.append(nums[counter])
                non_zero = non_zero + 1
            counter = counter - 1
        for i in range(0, self.board_size-non_zero):
            output_arr.append(0)
        for i in range(0, len(output_arr)):
            nums[i] = output_arr[self.board_size - 1 - i]
        


    def print_board(self):
        for i in range(0, len(self.board_positions)):
            print(self.board_positions[i])