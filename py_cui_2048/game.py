"""File containing game board logic and functions (written independantly of CUI)

Author: Jakub Wlodek
Created: Nov-12-2019
"""

# Use random lib for random cell placement
import random


class Game:
    """Game instance class for 2048

    Attributes
    ----------
    game_board : py_cui_2048.game.Board
        The game board object representation
    score : int
        The current game score
    turn : int
        The current turn counter

    Methods
    -------
    check_victory()
        Checks if user won
    check_defeat()
        Checks if no valid moves left
    """

    def __init__(self, initial_placement):
        """Constructor for game instace class object
        """

        self.game_board = Board(self, initial_placement)
        self.score = 0
        self.turn = 0


    def check_victory(self):
        """Checks if user won

        Returns
        -------
        won : bool
            True if 2048 tile found, false otherwise
        """

        for row in self.game_board.board_positions:
            for elem in row:
                if elem == 2048:
                    return True


    def check_defeat(self):
        """Checks if no valid moves left

        Either two neighbors are the same, or there is an empty location, otherwise
        no legal moves left

        Returns
        -------
        defeat : bool
            True if no moves left, otherwise false
        """

        for i in range(0, len(self.game_board.board_positions)):
            for j in range(0, len(self.game_board.board_positions[i])):
                if j > 0:
                    if self.game_board.board_positions[i][j] == self.game_board.board_positions[i][j-1]:
                        return False
                if i > 0:
                    if self.game_board.board_positions[i][j] == self.game_board.board_positions[i-1][j]:
                        return False
                if self.game_board.board_positions[i][j] == 0:
                    return False

        return True


class Board:
    """Class representing the game board itself, and operations on it

    Attributes
    ----------
    parent_instance : py_cui_2048.game.Game
        Parent game instance object
    board_positions : list of list of int
        2D array containing board values

    Methods
    -------
    get_empty_pos_list()
        Gets list of empty positions
    add_random_tile()
        Adds a new random tile (either 2 or 4) into an empty location after valid user move
    process_columns()
        Processes a vertical (up/down) movement
    process_rows()
        Processes a horizontal (left/right) movement
    update_nums()
        Top level update function called from 2048 client
    print_board()
        Debug function for printing board positions
    """

    def __init__(self, parent_instance, initial_placement):
        """Constructor for board class
        """

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
        """Function for getting list of empty cells in board

        Returns
        -------
        empty_pos_list : list of list of int
            list of coordinates of empty cells
        """

        empty_pos_list = []
        for i in range(0, len(self.board_positions)):
            for j in range(0, len(self.board_positions[i])):
                if self.board_positions[i][j] == 0:
                    empty_pos_list.append([i,j])
        return empty_pos_list


    def add_random_tile(self):
        """Function that adds a new tile to a random empty location

        Returns
        -------
        added : bool
            True if success, false otherwise
        """

        try:
            possible_pos = self.get_empty_pos_list()
            rand_val = ((random.randint(1, 10) % 2) + 1) * 2
            rand_pos = possible_pos[random.randint(0, len(possible_pos) - 1)]
            self.board_positions[rand_pos[0]][rand_pos[1]] = rand_val
            return True
        except ValueError:
            return False


    def process_columns(self, direction):
        """Processes a vertical (up/down) movement

        Parameters
        ----------
        direction : str
            Either up or down
        
        Returns
        -------
        was_valid : bool
            True if board changed, false otherwise
        """

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
        """Processes a horizontal (left/right) movement

        Parameters
        ----------
        direction : str
            Either left or right
        
        Returns
        -------
        was_valid : bool
            True if board changed, false otherwise
        """

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
        """Function that updates the numbers in a single column or row based on 2048 rules

        Always updates as if it is a row moving left to right. Caller functions convert to this format
        and convert back afterwords, so all use this function

        Parameters
        ----------
        nums : list of int
            The row or column to update
        
        Returns
        -------
        valid_move : bool
            True if row changed, false otherwise
        score_gain : int
            Amount of score the move gained
        """

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
        """Debug function for printing board
        """
        
        for i in range(0, len(self.board_positions)):
            print(self.board_positions[i])