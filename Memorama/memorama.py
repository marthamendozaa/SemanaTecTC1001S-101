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
Leonardo'''

tiles = tiles.split('\n') * 2

#Inicializacion de las cartas del memorama
#tiles = list(range(32)) * 2 # range = secuencia de valores de 0 a 31, lo convertimos en lista y lo replicamos x 2 
#indica si ya tengo una carta destapada
state = {'mark': None}
#lista con True x 64 por la cant de cuadritos. todas los cuadritos estan escondidos al inicio
hide = [True] * 64
contador = 0
contador_casillas = 0

#Funcion para desplegar la cuenta de clicks
def info_taps():
    writer2.clear()
    writer2.hideturtle()
    writer2.up()
    writer2.goto(160, 250)
    writer2.color('honeydew')
    writer2.write('Contador: ' + str(contador), align='left', font=('Cascadia Mono', 14, 'normal'))

#Funcion para desplegar la informacion del equipo
def info_alumnos():
    writer.hideturtle()
    writer.up()
    writer.goto(-290, 270)
    writer.color('honeydew')
    writer.write('Martha Mendoza Alfaro A01284654', align='left', font=('Cascadia Mono', 14, 'normal'))
    writer.goto(-290, 250)
    writer.color('honeydew')
    writer.write('Mariel Perez Ferrusquía A00832811', align='left', font=('Cascadia Mono', 14, 'normal'))

#Funcion para desplegar el mensaje ganador
def info_ganador():
    writer3.hideturtle()
    writer3.up()
    writer3.goto(160, -250)
    writer3.color('honeydew')
    writer3.write('¡Felicidades!', align='left', font=('Cascadia Mono', 18, 'normal'))
    
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
    #Contadores globales
    global contador, contador_casillas
    #Incrementa el valor en uno cada vez que se presiona una casilla
    contador+=1
    #Verifica que las casillas esten sin destapar
    if contador_casillas < 32:
        info_taps()
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        #Incrementa el valor en uno del contador que tiene registro de las casillas que han sido descubiertas
        contador_casillas+=1
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    
    #Verifica el punto en el que el juego se gana
    if contador_casillas == 32:
        info_ganador()

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
        write(tiles[mark], font=('Leelawadee', 15, 'normal'))

    update()
    ontimer(draw, 100)


#shuffle(tiles)
setup(620, 620, 370, 0)
bgcolor("LightPink")

#Info de los alumnos
writer = Turtle(visible= False)
info_alumnos()

#Info de los clicks
writer2 = Turtle(visible= False)
info_taps()

#Mensaje ganador
writer3 = Turtle(visible= False)

#Cambiar titulo de pantalla
screener = Turtle(visible= False)
screener.screen.title("Martha Mendoza y Mariel Pérez")

addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
