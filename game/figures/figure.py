from abc import ABC, abstractmethod
from game.field import Field


class Figure(ABC):
    def __init__(self, field: Field):
        self.field = field

    @abstractmethod
    def list_available_moves(self):
        pass

    def validate_move(self, dest_field: Field):
        # Limits figure position to vertical and horizontal
        if not dest_field.is_on_board():
            return False

        # Checks if new destination is in the same
        if self.field.x == dest_field.x and self.field.y == dest_field.y:
            return False
        return True
