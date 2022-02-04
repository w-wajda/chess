class Field:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def is_on_board(self):
        """Board is limited x from 'a' to 'h' and y from 1 to 8"""
        if ord("a") <= self.x <= ord("h") and 1 <= self.y <= 8:
            return True
        return False

    def __str__(self):
        return f"{chr(self.x)}{self.y}".upper()
