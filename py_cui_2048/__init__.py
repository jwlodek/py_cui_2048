"""File containing main 2048 UI class and rendering logic

Author: Jakub Wlodek
Created: Nov-7-2019
"""

# We will use py_cui for the user interface
import py_cui

# Python utility libraries
import random
import copy

# The game module manages the game instance
import py_cui_2048.game as GAME


class CUI2048:
    """CUI 2048 class.

    Attributes
    ----------
    master : py_cui.PyCUI
        Main parent CUI object
    positions : list of py_cui.widgets.Button
        Buttons used to represent 2048 cells
    prev_board : list of list of int
        2D array representing previous board.
    prev_score : int
        Previous turns score
    undid_move : bool
        True if undo has just been used
    score_label : py_cui.widgets.Label
        label printing score and turn
    menu : py_cui.widgets.ScrollMenu
        Main CUI menu

    Methods
    -------
    update_turns_scores()
        Function that updates the score and turn counters as appropriate
    shift_up()
        Function that performs a move up (W) operation
    shift_down()
        Function that performs a move down (S) operation
    shift_left()
        Function that performs a move left (A) operation
    shift_right()
        Function that performs a move right (D) operation
    initialize_new_game()
        Function that creates a new game board
    operate_on_menu_item()
        Function that operates on the current selected menu item
    undo_move()
        Function that is used to undo/redo a move
    get_logo_text()
        Function tath gets ascii art 2048 logo
    apply_board_state()
        Function that applies the board state to the CUI.
    play_again()
        Function that asks user if they want to play again
    generate_initial_placement()
        Function that creates an initial board placement
    """

    def __init__(self, master):
        """Constructor for main 2048 CUI window object
        """

        self.master = master
        self.master.add_key_command(py_cui.keys.KEY_W_LOWER, self.shift_up)
        self.master.add_key_command(py_cui.keys.KEY_A_LOWER, self.shift_left)
        self.master.add_key_command(py_cui.keys.KEY_S_LOWER, self.shift_down)
        self.master.add_key_command(py_cui.keys.KEY_D_LOWER, self.shift_right)
        self.master.set_status_bar_text('Use WASD to move the board, Enter to enter the menu, and q to quit')
        
        self.positions = []
        self.prev_board = None
        self.prev_score = 0
        self.undid_move = False
        self.score_label = self.master.add_label('Score: 0, Turns: 0', 1, 4, column_span=3)
        for i in range (0,4):
            row = []
            for j in range(0,4):
                pos = self.master.add_button('0', i, j, command=None)
                row.append(pos)
            self.positions.append(row)
        self.master.add_block_label(self.get_logo_text(), 0, 4, row_span = 1, column_span=3)
        scroll_menu_options = ['New Game', 'Undo Move', 'Redo Move', 'Exit']
        self.menu = self.master.add_scroll_menu('Menu', 2, 4, row_span = 2, column_span = 3)
        self.menu.add_item_list(scroll_menu_options)
        self.menu.add_key_command(py_cui.keys.KEY_ENTER, self.operate_on_menu_item)
        self.menu.add_key_command(py_cui.keys.KEY_W_LOWER, self.shift_up)
        self.menu.add_key_command(py_cui.keys.KEY_A_LOWER, self.shift_left)
        self.menu.add_key_command(py_cui.keys.KEY_S_LOWER, self.shift_down)
        self.menu.add_key_command(py_cui.keys.KEY_D_LOWER, self.shift_right)
        self.menu.set_focus_text('Use WASD to move the board, arrows to select menu items, and enter to use a menu item')
        self.initialize_new_game()


    def update_turns_scores(self):
        """Function that updates the score and turn counters as appropriate
        """

        self.score_label.title = 'Score: {}, Turn: {}'.format(self.game_instance.score, self.game_instance.turn)


    def shift_up(self):
        """Function that performs a move up (W) operation
        """

        self.undid_move = False
        self.prev_board = copy.deepcopy(self.game_instance.game_board.board_positions)
        self.prev_score = self.game_instance.score
        valid = self.game_instance.game_board.process_columns('up')
        if valid:
            out = self.game_instance.game_board.add_random_tile()
            if out:
                self.apply_board_state()


    def shift_left(self):
        """Function that performs a move left (A) operation
        """

        self.undid_move = False
        self.prev_board = copy.deepcopy(self.game_instance.game_board.board_positions)
        self.prev_score = self.game_instance.score
        valid = self.game_instance.game_board.process_rows('left')
        if valid:
            out = self.game_instance.game_board.add_random_tile()
            if out:
                self.apply_board_state()

    def shift_down(self):
        """Function that performs a move down (S) operation
        """

        self.undid_move = False
        self.prev_board = copy.deepcopy(self.game_instance.game_board.board_positions)
        self.prev_score = self.game_instance.score
        valid = self.game_instance.game_board.process_columns('down')
        if valid:
            out = self.game_instance.game_board.add_random_tile()
            if out:
                self.apply_board_state()


    def shift_right(self):
        """Function that performs a move right (D) operation
        """

        self.undid_move = False
        self.prev_board = copy.deepcopy(self.game_instance.game_board.board_positions)
        self.prev_score = self.game_instance.score
        valid = self.game_instance.game_board.process_rows('right')
        if valid:
            out = self.game_instance.game_board.add_random_tile()
            if out:
                self.apply_board_state()


    def initialize_new_game(self):
        """Function that creates a new game board
        """

        self.prev_board = None
        self.prev_score = 0
        self.undid_move = False
        initial_placement = self.generate_initial_placement()
        self.game_instance = GAME.Game(initial_placement)
        self.apply_board_state()
        self.master.move_focus(self.menu)


    def operate_on_menu_item(self):
        """Function that operates on the current selected menu item
        """

        operation = self.menu.get()
        if operation == 'New Game':
            self.initialize_new_game()
        elif operation == 'Undo Move':
            self.undo_move(True)
        elif operation == 'Redo Move':
            self.undo_move(False)
        elif operation == 'Exit':
            exit()

    
    def undo_move(self, turn_up_down):
        """Function that is used to undo/redo a move

        Parameters
        ----------
        turn_up_down : bool
            Flag that specifies whether to perform undo or redo
        """

        if self.undid_move and turn_up_down:
            self.master.show_warning_popup('Warning', 'Only one Undo is allowed at a time!')
            return
        elif not self.undid_move and not turn_up_down:
            self.master.show_warning_popup('Warning', 'Cannot redo move that has not been undone!')
            return
        if self.prev_board is not None:
            temp_board = copy.deepcopy(self.game_instance.game_board.board_positions)
            self.game_instance.game_board.board_positions = copy.deepcopy(self.prev_board)
            self.prev_board = temp_board
            if turn_up_down:
                self.game_instance.turn = self.game_instance.turn - 1
                self.undid_move = True
            else:
                self.game_instance.turn = self.game_instance.turn + 1
                self.undid_move = False
            temp_score = self.game_instance.score
            self.game_instance.score = self.prev_score
            self.prev_score = temp_score
            self.apply_board_state()
        else:
            self.master.show_error_popup('Error', 'No move has been made!')


    def get_logo_text(self):
        """Function tath gets ascii art 2048 logo

        Returns
        -------
        out : str
            Ascii-art 2048 logo
        """

        out = ""
        out = out + " _____  _____    ___  _____ \n"
        out = out + "/ __  \|  _  |  /   ||  _  |\n"
        out = out + "`' / /'| |/' | / /| | \ V / \n"
        out = out + "  / /  |  /| |/ /_| | / _ \ \n"
        out = out + "./ /___\ |_/ /\___  || |_| |\n"
        out = out + "\_____/ \___/     |_/\_____/\n"
        return out


    def apply_board_state(self):
        """Function that applies the board state to the CUI.
        
        Certain values are assigned certain py_cui colors, and each cells value is written from the 
        game board
        """

        for i in range(0, 4):
            for j in range(0, 4):
                val = self.game_instance.game_board.board_positions[i][j]
                self.positions[i][j].title = str(val)
                if val == 0:
                    self.positions[i][j].color = py_cui.WHITE_ON_BLACK
                elif val == 2:
                    self.positions[i][j].color = py_cui.CYAN_ON_BLACK
                elif val == 4:
                    self.positions[i][j].color = py_cui.CYAN_ON_BLACK
                elif val == 8:
                    self.positions[i][j].color = py_cui.MAGENTA_ON_BLACK
                elif val == 16:
                    self.positions[i][j].color = py_cui.MAGENTA_ON_BLACK
                elif val == 32:
                    self.positions[i][j].color = py_cui.GREEN_ON_BLACK
                elif val == 64:
                    self.positions[i][j].color = py_cui.GREEN_ON_BLACK
                elif val == 128:
                    self.positions[i][j].color = py_cui.RED_ON_BLACK
                elif val == 256:
                    self.positions[i][j].color = py_cui.RED_ON_BLACK
                elif val == 512:
                    self.positions[i][j].color = py_cui.YELLOW_ON_BLACK
                elif val == 1024:
                    self.positions[i][j].color = py_cui.YELLOW_ON_BLACK
                elif val == 2048:
                    self.positions[i][j].color = py_cui.BLUE_ON_BLACK

        self.update_turns_scores()
        won = self.game_instance.check_victory()
        lost = self.game_instance.check_defeat()
        if won:
            self.master.show_yes_no_popup('Congratulations You Won! ! Play Again?', self.play_again)
        elif lost:
            self.master.show_yes_no_popup('Game Over, Score: {}. Play Again?'.format(self.game_instance.score), command=self.play_again)


    def play_again(self, response):
        """Function that asks user if they want to play again

        Parameters
        ----------
        response : bool
            User response to play again query
        """

        if response:
            self.initialize_new_game()
        else:
            exit()


    def generate_initial_placement(self):
        """Function that creates an initial board placement

        Returns
        -------
        initial_placement : list of list of int
            Two random coordinates for the initial values
        """

        initial_placement = []
        placement_1 = []
        placement_2 = []

        for i in range(0,2):
            placement_1.append(random.randint(0,3))
            placement_2.append(random.randint(0,3))

        placement_1.append(random.randint(1,2) * 2)
        placement_2.append(random.randint(1,2) * 2)

        initial_placement.append(placement_1)
        initial_placement.append(placement_2)
        return initial_placement


def main():
    """Program entrypoint, create CUI, wrapper object and start it
    """

    root = py_cui.PyCUI(4,7)
    root.set_title('2048')
    root.toggle_unicode_borders()
    cui_2048 = CUI2048(root)
    root.start()