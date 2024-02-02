""" Test
    """


def test_game_board_positions(game_instance):
    """test `game_board` positions"""

    # _                                            [y][x]
    assert game_instance.game_board.board_positions[1][0] == 2

    assert game_instance.game_board.board_positions[3][2] == 2

    assert game_instance.game_board.get_empty_pos_list() == [
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

    random_tile_success = game_instance.game_board.add_random_tile()

    while random_tile_success is False:
        random_tile_success = game_instance.game_board.add_random_tile()

    assert len(game_instance.game_board.get_empty_pos_list()) < 14


def test_check_victory(game_instance):
    """test `check_victory` method"""

    assert game_instance.check_victory() is False

    game_instance.game_board.board_positions[0][0] = 2048

    assert game_instance.check_victory() is True


def test_check_defeat(game_instance):
    """test check defeat method"""

    assert game_instance.check_defeat() is False

    game_instance.game_board.board_positions = [
        [2, 1024, 128, 16],
        [32, 64, 8, 256],
        [512, 4, 64, 128],
        [256, 512, 1024, 16],
    ]

    assert game_instance.check_defeat() is True
