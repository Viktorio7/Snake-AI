import pyglet
from Button import Button


class DirectionalButton(Button):
    def __init__(self, font_size, text, direction, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.direction = direction
        self.label = pyglet.text.Label(text, font_size=font_size, x=(self.x + self.x + self.width) / 2.0,
                                       y=((self.y + self.y + self.height) / 2.0), anchor_x='center', anchor_y='center')

    def button_draw(self):
        super().button_draw()
        self.label.draw()
