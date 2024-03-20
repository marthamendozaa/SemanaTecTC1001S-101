"""
Martha Mendoza Alfaro A01284654
Mariel Perez Ferrusquía A00832811
"""

from turtle import *

from freegames import vector

# Escribe los nombres del equipo
def info_alumnos():
    writer.up()
    writer.goto(0,190)
    writer.color('blue')
    writer.write('Martha Mendoza Alfaro A01284654', align = 'left', font = ('Arial',10,'normal'))
    writer.goto(0,170)
    writer.color('pink')
    writer.write('Mariel Perez Ferrusquía A00832811', align = 'left', font = ('Arial',10,'normal'))



def line(start, end):
    """Draw line from start to end.
    start - vector (x,y)
    end - vector (x,y)
    up() - levanta la pluma
    down() - baja la pluma para dibujar"""

    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    #rellena el square
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    pass  # TODO


def rectangle(start, end):
    """Draw rectangle from start to end."""
    pass  # TODO


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    #rellena el square
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(60)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    # SOLO SE LLAMA CUANDO SE VA A MODIFICAR EL SHAPE
    state[key] = value

# Estado inicial del paint - Diccionario - start - indica si ya el usuario dio un click mouse - shape - linea
state = {'start': None, 'shape': square}
# tamaño de la pantalla - ancho, alto, x_esq. sup .izq_wind, y_esq.sup izq_win
setup(420, 420, 370, 0)
# registra la funcion que va a atender los eventos del mouse - te dirige a la función que atiende el click de mouse
onscreenclick(tap)
listen()

#Define que writer es otra turtle para escribir nombres
writer = Turtle(visible= False)
info_alumnos()

onkey(undo, 'u')
# onkey se usa lambda no tiene nombre y no hay parametro de entrada
onkey(lambda: color('black', 'purple'), 'P')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple','pink'), 'K')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
