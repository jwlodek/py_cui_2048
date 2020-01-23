import py_cui
import random
import py_cui_2048.game as GAME

class CUI2048:

    def __init__(self, master):
        self.master = master
        self.positions = []
        self.prev_board = None
        self.prev_score = 0
        self.score_label = self.master.add_label('Score: 0, Turns: 0', 1, 4, column_span=3)
        for i in range (0,4):
            row = []
            for j in range(0,4):
                pos = self.master.add_button('0', i, j, command=None)
                row.append(pos)
            self.positions.append(row)
        self.master.add_block_label(self.get_logo_text(), 0, 4, row_span = 1, column_span=3)
        scroll_menu_options = ['New Game', 'Undo Move', 'Exit']
        self.menu = self.master.add_scroll_menu('Menu', 2, 4, row_span = 2, column_span = 3)
        self.menu.add_item_list(scroll_menu_options)
        self.menu.add_key_command(py_cui.keys.KEY_ENTER, self.operate_on_menu_item)
        self.menu.add_key_command(py_cui.keys.KEY_W_LOWER, self.shift_up)
        self.menu.add_key_command(py_cui.keys.KEY_A_LOWER, self.shift_left)
        self.menu.add_key_command(py_cui.keys.KEY_S_LOWER, self.shift_down)
        self.menu.add_key_command(py_cui.keys.KEY_D_LOWER, self.shift_right)
        self.initialize_new_game()


    def update_turns_scores(self):
        self.score_label.title = 'Score: {}, Turn: {}'.format(self.game_instance.score, self.game_instance.turn)


    def shift_up(self):
        self.prev_board = self.game_instance.game_board.board_positions
        self.prev_score = self.game_instance.score
        valid = self.game_instance.game_board.process_columns('up')
        if valid:
            out = self.game_instance.game_board.add_random_tile()
            if out:
                self.apply_board_state()

    def shift_left(self):
        self.prev_board = self.game_instance.game_board.board_positions
        self.prev_score = self.game_instance.score
        valid = self.game_instance.game_board.process_rows('left')
        if valid:
            out = self.game_instance.game_board.add_random_tile()
            if out:
                self.apply_board_state()

    def shift_down(self):
        self.prev_board = self.game_instance.game_board.board_positions
        self.prev_score = self.game_instance.score
        valid = self.game_instance.game_board.process_columns('down')
        if valid:
            out = self.game_instance.game_board.add_random_tile()
            if out:
                self.apply_board_state()

    def shift_right(self):
        self.prev_board = self.game_instance.game_board.board_positions
        self.prev_score = self.game_instance.score
        valid = self.game_instance.game_board.process_rows('right')
        if valid:
            out = self.game_instance.game_board.add_random_tile()
            if out:
                self.apply_board_state()


    def initialize_new_game(self):
        initial_placement = self.generate_initial_placement()
        self.game_instance = GAME.Game(initial_placement)
        self.apply_board_state()
        self.master.move_focus(self.menu)


    def operate_on_menu_item(self):
        operation = self.menu.get()
        if operation == 'New Game':
            self.initialize_new_game()
        elif operation == 'Undo Move':
            self.undo_move()
        elif operation == 'Exit':
            exit()

    
    def undo_move(self):
        if self.prev_board is not None:
            self.game_instance.game_board.board_positions = self.prev_board
            self.game_instance.turn = self.game_instance.turn - 1
            self.game_instance.score = self.prev_score
            self.apply_board_state()
            


    def get_logo_text(self):
        out = ""
        out = out + " _____  _____    ___  _____ \n"
        out = out + "/ __  \|  _  |  /   ||  _  |\n"
        out = out + "`' / /'| |/' | / /| | \ V / \n"
        out = out + "  / /  |  /| |/ /_| | / _ \ \n"
        out = out + "./ /___\ |_/ /\___  || |_| |\n"
        out = out + "\_____/ \___/     |_/\_____/\n"
        return out


    def apply_board_state(self):
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
        if response:
            self.initialize_new_game()
        else:
            exit()


    def generate_initial_placement(self):
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
    root = py_cui.PyCUI(4,7)
    root.set_title('2048')
    cui_2048 = CUI2048(root)
    root.start()