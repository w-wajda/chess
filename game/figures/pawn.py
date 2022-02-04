from game.figures.figure import Figure
from game.field import Field


class Pawn(Figure):
    def validate_move(self, dest_field: Field):
        if not super().validate_move(dest_field):
            return False

        # Horizontal moves
        if dest_field.x != self.field.x:
            return False

        # Vertical moves
        if dest_field.y > self.field.y + 1:
            return False
        if dest_field.y < self.field.y:
            return False

        return True

    def list_available_moves(self):
        moves = []

        # Possible max moves
        moves_x = self.field.x
        moves_y = self.field.y + 1

        dest_field = Field(moves_x, moves_y)
        if dest_field.is_on_board():
            moves.append(dest_field)

        return moves
