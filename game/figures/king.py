from game.figures.figure import Figure
from game.field import Field


class King(Figure):
    def validate_move(self, dest_field: Field):
        if not super().validate_move(dest_field):
            return False

        # Horizontal moves
        if dest_field.x > self.field.x + 1 or dest_field.x < self.field.x - 1:
            return False

        # Vertical moves
        if dest_field.y > self.field.y + 1 or dest_field.y < self.field.y - 1:
            return False

        return True

    def list_available_moves(self):
        moves = []

        # Possible max moves
        moves_x = range(self.field.x - 1, self.field.x + 2)
        moves_y = range(self.field.y - 1, self.field.y + 2)

        for x in moves_x:
            for y in moves_y:
                dest_field = Field(x, y)
                if dest_field.is_on_board():
                    if not (
                        self.field.x == dest_field.x and self.field.y == dest_field.y
                    ):
                        moves.append(dest_field)

        return moves
