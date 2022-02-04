from game.figures.figure import Figure
from game.field import Field


class Knight(Figure):
    def validate_move(self, dest_field: Field):
        if not super().validate_move(dest_field):
            return False

        # The move is a shift in one axis by one and in the other by two
        diff_1x_2y = (
            abs(self.field.x - dest_field.x) == 1
            and abs(self.field.y - dest_field.y) == 2
        )
        diff_2x_1y = (
            abs(self.field.x - dest_field.x) == 2
            and abs(self.field.y - dest_field.y) == 1
        )

        if not (diff_1x_2y or diff_2x_1y):
            return False

        return True

    def list_available_moves(self):
        moves = []

        # Possible max moves
        moves_x = range(self.field.x - 2, self.field.x + 3)
        moves_y = range(self.field.y - 2, self.field.y + 3)

        for x in moves_x:
            for y in moves_y:
                dest_field = Field(x, y)
                if self.validate_move(dest_field):
                    moves.append(dest_field)

        return moves
