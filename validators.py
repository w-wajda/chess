from exceptions import (
    InvalidFieldException,
    InvalidFigureException,
)

from game.field import Field
from game.figures.bishop import Bishop
from game.figures.king import King
from game.figures.knight import Knight
from game.figures.pawn import Pawn
from game.figures.queen import Queen
from game.figures.rook import Rook


FIGURES = {
    "rook": Rook,
    "queen": Queen,
    "king": King,
    "knight": Knight,
    "bishop": Bishop,
    "pawn": Pawn,
}


def validate_field(field: str):
    x = ord(field[0])

    try:
        y = int(field[1:])
    except ValueError:
        raise InvalidFieldException("Field does not exist.")

    field = Field(x, y)
    if not field.is_on_board():
        raise InvalidFieldException("Field does not exist.")

    return field


def validate_figure(figure: str, field: Field):
    try:
        figure_class = FIGURES[figure]
    except KeyError:
        raise InvalidFigureException("Figure does not exist.")

    return figure_class(field)
