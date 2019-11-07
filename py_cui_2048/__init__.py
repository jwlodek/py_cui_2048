import py_cui
import random
import py_cui_2048.game as GAME

class CUI2048:

    def __init__(self, master):
        self.master = master
        self.positions = []
        for i in range (0,4):
            row = []
            for j in range(0,4):
                pos = self.master.add_button('0', i, j, command=None)
                row.append(pos)
            self.positions.append(row)
        self.initialize_new_game()
        self.master.add_block_label(self.get_logo_text(), 0, 4, row_span = 1, column_span=3)
        self.master.add_label('Score: 0', 1, 5)
        scroll_menu_options = ['New Game', 'Save Game', 'Exit']
        self.menu = self.master.add_scroll_menu('Menu', 2, 4, row_span = 2, column_span = 3)
        self.menu.add_item_list(scroll_menu_options)
        self.menu.add_key_command(py_cui.keys.KEY_ENTER, self.operate_on_menu_item)
        self.master.add_key_command(py_cui.keys.KEY_W_LOWER, self.shift_up)
        self.master.add_key_command(py_cui.keys.KEY_A_LOWER, self.shift_left)
        self.master.add_key_command(py_cui.keys.KEY_S_LOWER, self.shift_down)
        self.master.add_key_command(py_cui.keys.KEY_D_LOWER, self.shift_right)

    def shift_up(self):
        self.game_instance.game_board.process_columns('up')
        self.apply_board_state()

    def shift_left(self):
        self.game_instance.game_board.process_rows('left')
        self.apply_board_state()

    def shift_down(self):
        self.game_instance.game_board.process_columns('down')
        self.apply_board_state()

    def shift_right(self):
        self.game_instance.game_board.process_rows('right')
        self.master.stop()
        print(self.game_instance.game_board.board_positions)
        exit()
        #self.apply_board_state()


    def initialize_new_game(self):
        initial_placement = self.generate_initial_placement()
        self.game_instance = GAME.Game(initial_placement)
        self.apply_board_state()


    def operate_on_menu_item(self):
        operation = self.menu.get()
        if operation == 'New Game':
            self.initialize_new_game
        elif operation == 'Save Game':
            self.master.show_error_popup('Save Error', 'Saving has not yet been implemented')
        elif operation == 'Exit':
            exit()


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
                    self.positions[i][j].color = py_cui.WHITE_ON_BLACK
                elif val == 64:
                    self.positions[i][j].color = py_cui.WHITE_ON_BLACK
                elif val == 128:
                    self.positions[i][j].color = py_cui.WHITE_ON_BLACK
                elif val == 256:
                    self.positions[i][j].color = py_cui.WHITE_ON_BLACK
                elif val == 512:
                    self.positions[i][j].color = py_cui.WHITE_ON_BLACK
                elif val == 1024:
                    self.positions[i][j].color = py_cui.WHITE_ON_BLACK
                elif val == 2048:
                    self.positions[i][j].color = py_cui.WHITE_ON_BLACK



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