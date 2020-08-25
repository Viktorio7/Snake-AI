import pyglet
from SnakeBody import SnakeBody


class SnakeHead(SnakeBody):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = (255, 0, 0)
        self.direction = 2
        self.snake_dead = False
        self.death_wall = True

    def move_head(self):
        if self.direction < 1:
            self.direction = 4
        if self.direction > 4:
            self.direction = 1

        if self.direction == 1:  # up
            self.Y += 1
        elif self.direction == 2:  # right
            self.X += 1
        elif self.direction == 3:  # down
            self.Y -= 1
        elif self.direction == 4:  # left
            self.X -= 1

        if self.death_wall:
            if self.X > 34:
                self.snake_dead = True
            if self.X < 0:
                self.snake_dead = True
            if self.Y > 57:
                self.snake_dead = True
            if self.Y < 0:
                self.snake_dead = True
        else:
            if self.X > 34:
                self.X = 0
            if self.X < 0:
                self.X = 34
            if self.Y > 57:
                self.Y = 0
            if self.Y < 0:
                self.Y = 57
