import pyglet
import neat
import NEATGameClasses as GC

window = pyglet.window.Window(1440,900)

square = pyglet.shapes.Rectangle(x=200, y=200, width=200, height=200, color=(200, 200, 200))
classSquare=GC.SnakeBody(x=250, y=250, width=200, height=200)
classHead=GC.SnakeHead(x=-200, y=250, width=200, height=200)
#label = pyglet.text.Label('Hello, world', font_name='Times New Roman', font_size=36, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    square.draw()
    classSquare.draw()
    classHead.draw()


def update(dt):
    classHead.update(dt)

if __name__=='__main__':
    pyglet.clock.schedule_interval(update, 1/1.5)
    pyglet.app.run()