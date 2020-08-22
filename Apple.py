from GridObject import GridObject


class Apple(GridObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = (0, 255, 0)
        self.eaten = False
