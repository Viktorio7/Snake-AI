import pyglet


class GridObject(pyglet.shapes.Rectangle):
    def __init__(self, x, y):
        self.X = x
        self.Y = y
        super().__init__(x=self.grid_to_position_x(self.X),
                         y=self.grid_to_position_y(self.Y),
                         height=12, width=12)
        self.color = (255, 255, 255)

    def grid_to_position_x(self, grid_x):
        return 901 + grid_x * 15

    def grid_to_position_y(self, grid_y):
        return 16 + grid_y * 15

    def set_position_x(self, x):
        self.X = x

    def set_position_y(self, y):
        self.Y = y

    def position_part(self):
        self.x = self.grid_to_position_x(self.X)
        self.y = self.grid_to_position_y(self.Y)
