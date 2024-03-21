"""
Equipo 10
Martha Mendoza Alfaro A01284654
Mariel Perez Ferrusquía A00832811
"""

from random import randrange
from turtle import *
from freegames import square, vector
from random import randrange, choice

food = vector(50, 10)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Lista random de colores
colores = ["navy", "green", "purple", "pink", "black", "yellow", "blue", "DarkOrange", "cyan", "magenta", "OliveDrab"]


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim) #mueve

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head) #añade

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        #elimina la comida
        foodCircle.clear()
        # elige un color random para food y snake
        colorFood = choice(colores)
        colorSnake = choice(colores)
        # guarda nuevo color
        snakeSquare.pencolor(colorSnake)
        foodCircle.pencolor(colorFood)
        
    else:
        snake.pop(0) #elimina 0 de la lista, simula el movimiento el 0 es el primer vector dentro de la lista snake

    clear()

    #aqui dibuja el snake
    for body in snake:
        color2 = snakeSquare.pencolor()
        square(body.x, body.y, 9, color2)

    # aqui dibuja a la comida
    foodCircle.up()
    xCircle = food.x + 4.5
    yCircle = food.y + 4.5
    foodCircle.setpos(xCircle, yCircle)
    #mantener color cada movement
    color = foodCircle.pencolor()
    foodCircle.dot(9, color)

    #actualiza la pantalla lo que tiene el buffer
    update()
    ontimer(move, 100) #aqui se cambia la rapidez

#Turtle para comida
foodCircle = Turtle(visible=False)
#Color inicializado, empieza en morado
foodCircle.pencolor("purple")

#Turtle para snake
snakeSquare = Turtle(visible=False)
#Color inicializado, empieza en negro
snakeSquare.pencolor("black")

#Dimensiones de la ventana - ancho, alto, 
setup(420, 420, 370, 0)

#Cambiar titulo de pantalla
screener = Turtle(visible= False)
screener.screen.title("Martha Mendoza y Mariel Pérez")

hideturtle()
tracer(False)

listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
# Se añadio para poder moverlo en mi computadora que no tiene una tecla
onkey(lambda: change(10, 0), 'd')
onkey(lambda: change(-10, 0), 'a')
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0, -10), 's')
move()
done()

