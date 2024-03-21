"""Memory, puzzle game of number pairs.
Equipo 10
Martha Mendoza Alfaro A01284654
Mariel Pérez Ferrusquía
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')

tiles ='''\U0001F43AMartha
\U0001F43AMariel Gisela
\U0001F43AVale
\U0001F43AGoyo
\U0001f600César Alejandro
-Gabriel
Calvin
Alvaro Alejandro
-José Daniel
Juan Pablo
Bryan Alejandro
-Miguel
Mario Raúl
Jinelle
Cristian Alejandro
Roberta Giovanna
Alejandro
Rodrigo
Omar Damián
César Antonio
Ramón Antonio
Oscar Ariel
Sebastián
Bella Elisabet
Alexa Jimena
Luis Ángel
Enmanuel
Ángela
Melissa Elvia
Ángel de Jesús
-Hannia
Leonardo
Messi'''

tiles = tiles.split('\n') * 2

#Inicializacion de las cartas del memorama
#tiles = list(range(32)) * 2 # range = secuencia de valores de 0 a 31, lo convertimos en lista y lo replicamos x 2 
#indica si ya tengo una carta destapada
state = {'mark': None}
#lista con True x 64 por la cant de cuadritos. todas los cuadritos estan escondidos al inicio
hide = [True] * 64

#Funcion para desplegar los nombres del equipo
def info_alumnos():
    color('purple')
    writer.hideturtle()
    writer.up()
    writer.goto(0,230)
    writer.color('honeydew')
    writer.write('Martha Mendoza Alfaro A01284654', align = 'left', font = ('Century',16,'normal'))
    writer.goto(0,210)
    writer.color('honeydew')
    writer.write('Mariel Perez Ferrusquía A00832811', align = 'left', font = ('Century',16,'normal'))


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    #(x,y) esq sup izq
    up()
    goto(x, y)
    down()
    color('white', 'MistyRose2')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    info_alumnos()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


#shuffle(tiles)
setup(620, 620, 370, 0)
bgcolor("LightPink")

writer = Turtle(visible= False)
info_alumnos()

#Cambiar titulo de pantalla
screener = Turtle(visible= False)
screener.screen.title("Martha Mendoza y Mariel Pérez")


addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()

done()
