from game.field import Field
from game.figures.figure import Figure


def test_validate_move_move():
    class FigureImpl(Figure):
        def list_available_moves(self):
            return []

    current_field = Field(ord("f"), 2)
    dest_field = Field(ord("b"), 2)
    assert FigureImpl(current_field).validate_move(dest_field)


def test_cannot_cross_move_out_of_board():
    class FigureImpl(Figure):
        def list_available_moves(self):
            return []

    current_field = Field(ord("f"), 1)
    dest_field = Field(ord("i"), 5)
    assert not FigureImpl(current_field).validate_move(dest_field)
