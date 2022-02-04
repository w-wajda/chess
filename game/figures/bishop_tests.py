from game.field import Field
from game.figures.bishop import Bishop


def test_can_cross_move():
    current_field = Field(ord("a"), 1)
    dest_field = Field(ord("b"), 2)
    dest_far_away_field = Field(ord("g"), 7)
    assert Bishop(current_field).validate_move(dest_field)
    assert Bishop(current_field).validate_move(dest_far_away_field)


def test_cannot_horizontal_move():
    current_field = Field(ord("a"), 1)
    dest_field = Field(ord("b"), 1)
    dest_far_away_field = Field(ord("d"), 1)
    assert not Bishop(current_field).validate_move(dest_field)
    assert not Bishop(current_field).validate_move(dest_far_away_field)


def test_cannot_vertical_move():
    current_field = Field(ord("a"), 1)
    dest_field = Field(ord("a"), 2)
    dest_far_away_field = Field(ord("a"), 5)
    assert not Bishop(current_field).validate_move(dest_field)
    assert not Bishop(current_field).validate_move(dest_far_away_field)


def test_cannot_l_move():
    current_field = Field(ord("a"), 1)
    dest_field = Field(ord("b"), 3)
    dest_far_away_field = Field(ord("b"), 5)
    assert not Bishop(current_field).validate_move(dest_field)
    assert not Bishop(current_field).validate_move(dest_far_away_field)


def test_list_available_moves():
    current_field = Field(ord("e"), 5)
    assert len(Bishop(current_field).list_available_moves()) == 13
