from game.field import Field
from game.figures.knight import Knight


def test_can_l_move():
    current_field = Field(ord("c"), 5)
    dest_field = Field(ord("a"), 4)
    assert Knight(current_field).validate_move(dest_field)


def test_cannot_l_move_faraway():
    current_field = Field(ord("c"), 5)
    dest_field = Field(ord("f"), 6)
    assert not Knight(current_field).validate_move(dest_field)


def test_cannot_cross_move():
    current_field = Field(ord("c"), 5)
    dest_field = Field(ord("d"), 6)
    dest_far_away_field = Field(ord("e"), 7)
    assert not Knight(current_field).validate_move(dest_field)
    assert not Knight(current_field).validate_move(dest_far_away_field)


def test_cannot_horizontal_move():
    current_field = Field(ord("c"), 5)
    dest_field = Field(ord("d"), 5)
    dest_far_away_field = Field(ord("e"), 5)
    assert not Knight(current_field).validate_move(dest_field)
    assert not Knight(current_field).validate_move(dest_far_away_field)


def test_cannot_vertical_move():
    current_field = Field(ord("c"), 5)
    dest_field = Field(ord("c"), 6)
    dest_far_away_field = Field(ord("c"), 8)
    assert not Knight(current_field).validate_move(dest_field)
    assert not Knight(current_field).validate_move(dest_far_away_field)


def test_list_available_moves():
    current_field = Field(ord("h"), 5)
    assert len(Knight(current_field).list_available_moves()) == 4
