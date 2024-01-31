""" Test
    """

from py_cui_2048.game import Game


# write a test class to group the test methods
class Test2048Game:
    """Test py cui 2048 game module"""

    # _                 [(x, y, value), (x, y, value)]
    initial_placement = [(0, 1, 2), (2, 3, 2)]

    game_instance = Game(initial_placement)

    def test_game_board_positions(self):
        """test `game_board` positions"""

        # _                                                 [y][x]
        assert self.game_instance.game_board.board_positions[1][0] == 2

        assert self.game_instance.game_board.board_positions[3][2] == 2

        assert self.game_instance.game_board.get_empty_pos_list() == [
            [0, 0],
            [0, 1],
            [0, 2],
            [0, 3],
            [1, 1],
            [1, 2],
            [1, 3],
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [3, 0],
            [3, 1],
            [3, 3],
        ]

        random_tile_success = self.game_instance.game_board.add_random_tile()

        while random_tile_success is False:
            random_tile_success = self.game_instance.game_board.add_random_tile()

        assert len(self.game_instance.game_board.get_empty_pos_list()) < 14

    def test_check_victory(self):
        """test `check_victory` method"""

        assert self.game_instance.check_victory() is None

        self.game_instance.game_board.board_positions[0][0] = 2048

        assert self.game_instance.check_victory() is True

    def test_check_defeat(self):
        """test check defeat method"""

        assert self.game_instance.check_defeat() is False

        self.game_instance.game_board.board_positions = [
            [2, 1024, 128, 16],
            [32, 64, 8, 256],
            [512, 4, 64, 128],
            [256, 512, 1024, 16],
        ]

        assert self.game_instance.check_defeat() is True
