import pyglet
from Button import Button


class CheckButton(Button):
    def __init__(self, font_size, text, checked=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.checked = checked
        self.checked_draw = pyglet.shapes.Rectangle(x=self.x + 15, y=self.y + 15, height=self.height - 30,
                                                    width=self.width - 30, color=(255, 255, 255))
        self.label = pyglet.text.Label(text, font_size=font_size, x=self.x + self.width + 10,
                                       y=((self.y + self.y + self.height) / 2.0), anchor_y='center')

    def button_draw(self):
        super().button_draw()
        self.label.draw()
        if self.checked:
            self.checked_draw.draw()
