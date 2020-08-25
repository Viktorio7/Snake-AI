import pyglet


class Button:
    # for clockwise direction use 1, for anticlockwise -1
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.outer = pyglet.shapes.Rectangle(x=x, y=y, height=height, width=width, color=(255, 255, 255))
        self.inner = pyglet.shapes.Rectangle(x=x + 10, y=y + 10, height=height - 20, width=width - 20, color=(0, 0, 0))

    def button_draw(self):
        self.outer.draw()
        self.inner.draw()

    def button_clicked(self, mouse_x, mouse_y):
        if self.x < mouse_x < self.width + self.x:
            if self.y < mouse_y < self.height + self.y:
                return True
        return False
