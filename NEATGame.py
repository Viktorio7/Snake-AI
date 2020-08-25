import pyglet
import random
from SnakeBody import SnakeBody
from SnakeHead import SnakeHead
from Apple import Apple
from DirectionalButton import DirectionalButton
from CheckButton import CheckButton

window = pyglet.window.Window(1440, 900, vsync=True)
window.set_location(30, 50)

apple = []
snake = [SnakeHead(17, 28), SnakeBody(16, 28), SnakeBody(15, 28)]

dir_buttons = [DirectionalButton(x=555, y=450, width=250, height=100, font_size=30, text='Right', direction=1),
               DirectionalButton(x=45, y=450, width=250, height=100, font_size=30, text='Left', direction=-1)]

check_button = CheckButton(x=45, y=100, width=50, height=50, font_size=20, text='Death wall')


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
                snake[0].snake_dead = True


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
    while 1:
        temp_x = random.randint(0, 34)
        temp_y = random.randint(0, 57)
        if free_space(temp_x, temp_y):
            apple.append(Apple(temp_x, temp_y))
            break


create_apple()
timing_control = False


@window.event
def on_mouse_press(x, y, button, modifiers):
    if check_button.button_clicked(x, y):
        if check_button.checked:
            check_button.checked = False
        else:
            check_button.checked = True
    global timing_control
    if not timing_control:
        for item in dir_buttons:
            if item.button_clicked(x, y):
                snake[0].direction += item.direction
                timing_control = True


@window.event
def on_draw():
    window.clear()
    draw_UI()
    check_button.button_draw()
    for item in dir_buttons:
        item.button_draw()
    for item in apple:
        item.draw()
    for item in snake:
        item.draw()


def update(dt):
    global snake
    snake[0].death_wall = check_button.checked
    if not apple:
        create_apple()

    for i in range(len(snake) - 1, 0, -1):
        snake[i].move_body(snake[i - 1])
        snake[i].position_part()
    snake[0].move_head()
    snake[0].position_part()

    death()
    if snake[0].snake_dead:
        snake = [SnakeHead(17, 28), SnakeBody(16, 28), SnakeBody(15, 28)]
    eaten_apple()
    global timing_control
    timing_control = False


if __name__ == '__main__':
    window.set_visible()
    pyglet.clock.schedule_interval(update, 1 / 120)
    pyglet.app.run()
