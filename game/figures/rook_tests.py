from game.field import Field
from game.figures.rook import Rook


def test_can_horizontal_move():
    current_field = Field(ord("c"), 5)
    dest_field = Field(ord("d"), 5)
    dest_far_away_field = Field(ord("e"), 5)
    assert Rook(current_field).validate_move(dest_field)
    assert Rook(current_field).validate_move(dest_far_away_field)


def test_can_vertical_move():
    current_field = Field(ord("c"), 5)
    dest_field = Field(ord("c"), 6)
    dest_far_away_field = Field(ord("c"), 8)
    assert Rook(current_field).validate_move(dest_field)
    assert Rook(current_field).validate_move(dest_far_away_field)


def test_cannot_cross_move():
    current_field = Field(ord("c"), 5)
    dest_field = Field(ord("d"), 6)
    dest_far_away_field = Field(ord("e"), 7)
    assert not Rook(current_field).validate_move(dest_field)
    assert not Rook(current_field).validate_move(dest_far_away_field)


def test_cannot_l_move():
    current_field = Field(ord("d"), 4)
    dest_field = Field(ord("f"), 5)
    dest_far_away_field = Field(ord("g"), 5)
    assert not Rook(current_field).validate_move(dest_field)
    assert not Rook(current_field).validate_move(dest_far_away_field)


def test_list_available_moves():
    current_field = Field(ord("g"), 3)
    assert len(Rook(current_field).list_available_moves()) == 14
