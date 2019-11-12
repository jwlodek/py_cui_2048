import random


class Game:

    def __init__(self, initial_placement):
        self.game_board = Board(self, initial_placement)
        self.score = 0
        self.turn = 0


    def check_victory(self):
        for row in self.game_board.board_positions:
            for elem in row:
                if elem == 2048:
                    return True

class Board:

    def __init__(self, parent_instance, initial_placement):

        self.parent_instance = parent_instance
        initial_x1 = initial_placement[0][0]
        initial_y1 = initial_placement[0][1]
        initial_val1 = initial_placement[0][2]
        initial_x2 = initial_placement[1][0]
        initial_y2 = initial_placement[1][1]
        initial_val2 = initial_placement[1][2]
        self.board_positions = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
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
        try:
            possible_pos = self.get_empty_pos_list()
            rand_val = ((random.randint(1, 10) % 2) + 1) * 2
            rand_pos = possible_pos[random.randint(0, len(possible_pos) - 1)]
            self.board_positions[rand_pos[0]][rand_pos[1]] = rand_val
            return True
        except ValueError:
            return False


    def process_columns(self, direction):
        was_valid = False
        for i in range(0, len(self.board_positions[0])):
            temp = []
            for j in range(0, len(self.board_positions)):
                temp.append(self.board_positions[j][i])
            if direction == 'up':
                temp.reverse()
            valid, score = self.update_nums(temp)
            if valid:
                self.parent_instance.score = self.parent_instance.score + score
                was_valid = True
            if direction == 'up':
                temp.reverse()
            for j in range(0, len(self.board_positions)):
                self.board_positions[j][i] = temp[j]

        if was_valid:
            self.parent_instance.turn = self.parent_instance.turn + 1
        return was_valid


    def process_rows(self, direction):
        was_valid = False
        for i in range(0, len(self.board_positions)):
            temp = self.board_positions[i]
            if direction == 'left':
                temp.reverse()
            valid, score = self.update_nums(temp)
            if valid:
                self.parent_instance.score = self.parent_instance.score + score
                was_valid = True
            if direction == 'left':
                temp.reverse()
            self.board_positions[i] = temp

        if was_valid:
            self.parent_instance.turn = self.parent_instance.turn + 1

        return was_valid


    def update_nums(self, nums):
        valid_move = False
        score_gain = 0
        counter = 3
        while counter > 0:
            next_num = counter - 1
            while  next_num > 0 and nums[next_num] == 0:
                next_num = next_num - 1
            if nums[counter] == nums[next_num]:
                nums[next_num] = 2 * nums[counter]
                valid_move = True
                score_gain = score_gain + (nums[counter] * 2)
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
        for i in range(0, 4-non_zero):
            output_arr.append(0)
        for i in range(0, len(output_arr)):
            if nums[i] != output_arr[3-i]:
                valid_move = True
            nums[i] = output_arr[3-i]
        return valid_move, score_gain
        


    def print_board(self):
        for i in range(0, len(self.board_positions)):
            print(self.board_positions[i])