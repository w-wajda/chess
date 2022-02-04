from game.field import Field


def test_is_on_board():
    pole = Field(ord("a"), 1)
    assert pole.is_on_board()


def test_is_not_on_board_x():
    pole = Field(ord("t"), 1)
    assert not pole.is_on_board()


def test_is_not_on_board_y():
    pole = Field(ord("b"), 9)
    assert not pole.is_on_board()
