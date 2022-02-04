from game.figures.figure import Figure
from game.field import Field


class Rook(Figure):
    def validate_move(self, dest_field: Field):
        if not super().validate_move(dest_field):
            return False

        # Checks if it is vertical and horizontal move
        if self.field.x != dest_field.x and self.field.y != dest_field.y:
            return False

        return True

    def list_available_moves(self):
        moves = []

        # Possible max moves
        moves_x = range(self.field.x - 7, self.field.x + 8)
        moves_y = range(self.field.y - 7, self.field.y + 8)

        for x in moves_x:
            dest_field = Field(x, self.field.y)
            if dest_field.is_on_board() and self.field.x != dest_field.x:
                moves.append(dest_field)

        for y in moves_y:
            dest_field = Field(self.field.x, y)
            if dest_field.is_on_board() and self.field.y != dest_field.y:
                moves.append(dest_field)

        return moves
