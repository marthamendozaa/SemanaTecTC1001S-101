"""
Martha Mendoza Alfaro A01284654
Mariel Perez Ferrusquía A00832811
"""

from random import randrange
from turtle import *
from freegames import square, vector

food = vector(50, 10)
snake = [vector(10, 0)]
aim = vector(0, -10)

#pto4 = pto1
#pto4.x = 700 
#se modifica pto1 a travez del pto4
"""
pto1 = vector(100,100)
pto2 = vector(200,100)
pto4 = pto2.copy()
pto4.x = 1000
pto4.y = 1000
"""

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
        foodCircle.clear()
    else:
        snake.pop(0) #elimina 0 de la lista, simula el movimiento el 0 es el primer vector dentro de la lista snake

    clear()
    #foodCircle.clear() 

    for body in snake:
        square(body.x, body.y, 9, 'black')

    #square(food.x, food.y, 9, 'green')
    foodCircle.up()
    xCircle = food.x + 4.5
    yCircle = food.y + 4.5
    foodCircle.setpos(xCircle, yCircle)
    foodCircle.dot(9, "purple")
    update()
    ontimer(move, 100) #aqui se cambia la rapidez


foodCircle = Turtle(visible=False)

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

