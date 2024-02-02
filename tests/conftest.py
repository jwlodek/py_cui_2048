"""Pytest configuration script
    """

import pytest

from py_cui_2048.game import Game


# write a test class to group the test methods


@pytest.fixture
def initial_placement():
    """initial placement test fixture for testing game instantiation

    Returns:
        list[tuple[int,int,int],tuple[int,int,int]]: placement coordinates and value
    """
    # _    [(x, y, value), (x, y, value)]
    return [(2, 2, 2), (3, 1, 2)]


@pytest.fixture
def game_instance():
    """game instance fixture for unit test

    Returns:
        Game: instance class for 2048
    """
    return Game(initial_placement=[(0, 1, 2), (2, 3, 2)])
