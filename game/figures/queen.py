from game.figures.figure import Figure
from game.field import Field


class Queen(Figure):
    def validate_move(self, dest_field: Field):
        if not super().validate_move(dest_field):
            return False

        # Checks if it is crossed move
        is_cross_move = abs(self.field.x - dest_field.x) == abs(
            self.field.y - dest_field.y
        )
        # Checks if it is vertical and horizontal move
        is_vertical_horizontal_move = (
            self.field.x == dest_field.x or self.field.y == dest_field.y
        )
        if not (is_cross_move or is_vertical_horizontal_move):
            return False

        return True

    def list_available_moves(self):
        moves = []

        # Possible max moves
        moves_x = range(self.field.x - 7, self.field.x + 8)
        moves_y = range(self.field.y - 7, self.field.y + 8)

        for x in moves_x:
            for y in moves_y:
                dest_field = Field(x, y)
                if self.validate_move(dest_field):
                    moves.append(dest_field)

        return moves
