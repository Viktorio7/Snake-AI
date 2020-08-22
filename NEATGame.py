import pyglet
import random
from SnakeBody import SnakeBody
from SnakeHead import SnakeHead
from Button import Button
from Apple import Apple

window = pyglet.window.Window(1440, 900, visible=False)
window.set_location(30, 50)

snake_dead = False
apple = []
snake = [SnakeHead(17, 28), SnakeBody(16, 28), SnakeBody(15, 28)]
snake[0].direction = 2

buttons = [Button(555, 450, 250, 100, 30, 'Right', 1), Button(45, 450, 250, 100, 30, 'Left', -1)]


def draw_UI():
    # Grid size 35x58
    x1 = 900
    x2 = 1425
    y1 = 15
    y2 = 885

    c = 30
    for i in range(1, 35):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', (x1 + i * 15, y1, x1 + i * 15, y2)),
                             ('c3B', (c, c, c, c, c, c)))

    for i in range(1, 58):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', (x1, y1 + i * 15, x2, y1 + i * 15)),
                             ('c3B', (c, c, c, c, c, c)))

    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', (x1, y1, x1, y2)))
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', (x1, y1, x2, y1)))
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', (x2, y1, x2, y2)))
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', (x1, y2, x2, y2)))


def death():
    for i in range(1, len(snake)):
        if snake[0].X == snake[i].X:
            if snake[0].Y == snake[i].Y:
                global snake_dead
                snake_dead = True


def eaten_apple():
    if apple:
        if snake[0].X == apple[0].X:
            if snake[0].Y == apple[0].Y:
                snake.append(SnakeBody(snake[-1].X, snake[-1].Y))
                apple.pop()


def free_space(x, y):
    for i in range(0, len(snake)):
        if snake[i].X == x:
            if snake[i].Y == y:
                return False
    return True


def create_apple():
    while (1):
        temp_x = random.randint(0, 34)
        temp_y = random.randint(0, 57)
        if free_space(temp_x, temp_y):
            apple.append(Apple(temp_x, temp_y))
            break


create_apple()
timing_control = False


@window.event
def on_mouse_press(x, y, button, modifiers):
    global timing_control
    if not timing_control:
        for item in buttons:
            if item.button_clicked(x, y):
                snake[0].direction += item.direction
                timing_control = True


@window.event
def on_draw():
    window.clear()
    draw_UI()
    for item in buttons:
        item.button_draw()
    for item in apple:
        item.draw()
    for item in snake:
        item.draw()


def update(dt):
    global snake
    if not apple:
        create_apple()

    for i in range(len(snake) - 1, 0, -1):
        snake[i].move_body(snake[i - 1])
        snake[i].position_part()
    snake[0].move_head()
    snake[0].position_part()

    death()
    global snake_dead
    if snake_dead:
        snake = [SnakeHead(17, 28), SnakeBody(16, 28), SnakeBody(15, 28)]
        snake_dead = False
    eaten_apple()
    global timing_control
    timing_control = False


if __name__ == '__main__':
    window.set_visible()
    pyglet.clock.schedule_interval(update, 1 / 10)
    pyglet.app.run()
