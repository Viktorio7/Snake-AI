import pyglet
from GridObject import GridObject


class SnakeBody(GridObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = (255, 255, 255)

    def move_body(self, previous_body_part):
        self.set_position_x(previous_body_part.X)
        self.set_position_y(previous_body_part.Y)